const recordsBody = document.getElementById("records-body");
const modal = document.getElementById("record-modal");
const form = document.getElementById("record-form");
const toast = document.getElementById("toast");
let toastTimer;
let currentRecords = [];

async function api(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: { "Content-Type": "application/json", ...(options.headers || {}) }
  });
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Something went wrong. Please try again.");
  }
  return response.status === 204 ? null : response.json();
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("visible"), 3000);
}

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[char]));
}

async function refreshStats() {
  const stats = await api("/api/admin/stats");
  document.getElementById("stat-total").textContent = stats.total;
  document.getElementById("stat-approved").textContent = stats.approved;
  document.getElementById("stat-pending").textContent = stats.pending;
  document.getElementById("stat-queries").textContent = stats.query_count;
  document.getElementById("queue-count").textContent = String(stats.pending).padStart(2, "0");
  const recent = document.getElementById("recent-queries");
  if (!stats.queries.length) {
    recent.innerHTML = '<div class="recent-empty">Questions will appear here as farmers use the assistant.</div>';
  } else {
    recent.innerHTML = stats.queries.map((query) => `
      <div class="recent-query"><span class="recent-query-icon">↗</span><span><strong>${esc(query.question)}</strong><small>${formatRelative(query.created_at)}</small></span></div>
    `).join("");
  }
}

function formatRelative(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "Just now";
  const minutes = Math.max(0, Math.floor((Date.now() - date.getTime()) / 60000));
  if (minutes < 1) return "Just now";
  if (minutes < 60) return `${minutes} min ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours} hr ago`;
  return date.toLocaleDateString();
}

async function refreshRecords() {
  const search = document.getElementById("record-search").value.trim();
  const status = document.getElementById("status-filter").value;
  const params = new URLSearchParams({ search, status });
  currentRecords = await api(`/api/admin/records?${params}`);
  recordsBody.innerHTML = currentRecords.map((record) => `
    <tr>
      <td><div class="record-cell"><span class="record-category-icon">${categoryGlyph(record.category)}</span><span><strong>${esc(record.title)}</strong><small>${esc(record.category)} · Demo guidance · v${record.version}</small></span></div></td>
      <td class="source-cell">${esc(record.source)}</td>
      <td class="date-cell">${esc(record.publication_date)}</td>
      <td><span class="status-badge status-${esc(record.status)}"><i></i>${esc(capitalize(record.status))}</span></td>
      <td><div class="row-actions">
        ${record.status !== "approved" ? `<button class="approve-action" data-action="approved" data-id="${record.id}" title="Approve record" aria-label="Approve ${esc(record.title)}">✓</button>` : ""}
        ${record.status !== "rejected" ? `<button class="reject-action" data-action="rejected" data-id="${record.id}" title="Reject record" aria-label="Reject ${esc(record.title)}">×</button>` : ""}
        <button class="edit-action" data-edit="${record.id}" title="Edit record" aria-label="Edit ${esc(record.title)}">✎</button>
      </div></td>
    </tr>`).join("");
  document.getElementById("empty-records").hidden = currentRecords.length > 0;
  document.getElementById("record-count").textContent = `${currentRecords.length} record${currentRecords.length === 1 ? "" : "s"}`;
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", () => updateStatus(button.dataset.id, button.dataset.action));
  });
  document.querySelectorAll("[data-edit]").forEach((button) => {
    button.addEventListener("click", () => openEdit(button.dataset.edit));
  });
}

function categoryGlyph(category) {
  const value = category.toLowerCase();
  if (value.includes("water") || value.includes("irrigation")) return "⌁";
  if (value.includes("scheme")) return "▤";
  if (value.includes("soil") || value.includes("nutrient")) return "♧";
  return "✿";
}

function capitalize(value) {
  return value.charAt(0).toUpperCase() + value.slice(1);
}

async function refresh() {
  try {
    await Promise.all([refreshStats(), refreshRecords()]);
  } catch (error) {
    showToast(error.message);
  }
}

function openModal(record = null) {
  form.reset();
  document.getElementById("record-id").value = record?.id || "";
  document.getElementById("modal-title").textContent = record ? "Edit knowledge record" : "Add a knowledge record";
  document.getElementById("record-title").value = record?.title || "";
  document.getElementById("record-category").value = record?.category || "";
  document.getElementById("record-keywords").value = record?.keywords || "";
  document.getElementById("record-answer-en").value = record?.answer_en || "";
  document.getElementById("record-answer-hi").value = record?.answer_hi || "";
  document.getElementById("record-answer-mr").value = record?.answer_mr || "";
  document.getElementById("record-source").value = record?.source || "";
  document.getElementById("record-date").value = record?.publication_date || new Date().toISOString().slice(0, 10);
  document.getElementById("record-status").value = record?.status || "pending";
  document.getElementById("form-error").textContent = "";
  modal.hidden = false;
  document.getElementById("record-title").focus();
}

function openEdit(id) {
  const record = currentRecords.find((item) => String(item.id) === String(id));
  if (record) openModal(record);
}

async function updateStatus(id, status) {
  try {
    await api(`/api/admin/records/${id}/status?status=${status}`, { method: "PATCH" });
    showToast(`Record ${status}.`);
    await refresh();
  } catch (error) {
    showToast(error.message);
  }
}

document.getElementById("add-record-button").addEventListener("click", () => openModal());
document.getElementById("close-modal").addEventListener("click", () => { modal.hidden = true; });
document.getElementById("cancel-modal").addEventListener("click", () => { modal.hidden = true; });
modal.addEventListener("click", (event) => { if (event.target === modal) modal.hidden = true; });
document.addEventListener("keydown", (event) => { if (event.key === "Escape") modal.hidden = true; });
document.getElementById("record-search").addEventListener("input", () => {
  clearTimeout(window.searchTimer);
  window.searchTimer = setTimeout(refreshRecords, 200);
});
document.getElementById("status-filter").addEventListener("change", refreshRecords);
document.getElementById("review-pending").addEventListener("click", async () => {
  document.getElementById("status-filter").value = "pending";
  await refreshRecords();
  document.querySelector(".records-panel").scrollIntoView({ behavior: "smooth", block: "start" });
});
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const id = document.getElementById("record-id").value;
  const payload = {
    title: document.getElementById("record-title").value.trim(),
    category: document.getElementById("record-category").value.trim(),
    keywords: document.getElementById("record-keywords").value.trim(),
    answer_en: document.getElementById("record-answer-en").value.trim(),
    answer_hi: document.getElementById("record-answer-hi").value.trim(),
    answer_mr: document.getElementById("record-answer-mr").value.trim(),
    source: document.getElementById("record-source").value.trim(),
    publication_date: document.getElementById("record-date").value,
    status: document.getElementById("record-status").value
  };
  const saveButton = document.getElementById("save-record");
  saveButton.disabled = true;
  document.getElementById("form-error").textContent = "";
  try {
    await api(id ? `/api/admin/records/${id}` : "/api/admin/records", {
      method: id ? "PUT" : "POST",
      body: JSON.stringify(payload)
    });
    modal.hidden = true;
    showToast(id ? "Knowledge record updated." : "Knowledge record added.");
    await refresh();
  } catch (error) {
    document.getElementById("form-error").textContent = error.message;
  } finally {
    saveButton.disabled = false;
  }
});

refresh();
