const translations = {
  en: {
    workspace: "WORKSPACE", askAssistant: "Ask assistant", quickQuestions: "Quick questions", resources: "RESOURCES",
    knowledgeBase: "Knowledge base", inSeason: "Demo season", kharifSeason: "Kharif · Demo", seasonNote: "Small steps today, stronger harvest tomorrow.",
    farmer: "Farmer", demoKnowledge: "Demo knowledge", helloFarm: "A LITTLE HELP GOES A LONG WAY", goodMorning: "Good morning, Ramesh",
    welcomeSub: "What’s happening in your fields today?", today: "Today", yourFarmPartner: "YOUR FARM, IN GOOD HANDS",
    heroTitle: "Good decisions\ngrow good things.", heroCopy: "Ask a question in your language. Get practical guidance, rooted in trusted agricultural knowledge.",
    askQuestion: "Ask a question", practicalAdvice: "PRACTICAL ADVICE", howCanWeHelp: "How can we help?",
    helpSub: "Ask in your own words, or try a question below.", farmerFirst: "Farmer-first guidance",
    askKrishi: "Ask Krishi Voice", askHint: "Your farming companion is listening", ready: "READY",
    questionPlaceholder: "Ask about your crop, soil, irrigation or more...", enterHint: "Enter to ask", askButton: "Ask Krishi",
    tryAsking: "Try asking", popularQuestions: "POPULAR QUESTIONS", exampleCotton: "My cotton leaves are turning yellow",
    cropHealth: "CROP HEALTH", exampleSoy: "How often should I irrigate soybean?", waterManagement: "WATER MANAGEMENT",
    examplePaddy: "What fertilizer is recommended for paddy?", soilNutrients: "SOIL & NUTRIENTS",
    exampleScheme: "What government schemes can I apply for?", schemes: "GOVERNMENT SCHEMES",
    builtOnTrust: "BUILT ON TRUST", adviceYouCanTrust: "Advice you can\nfeel good about.",
    trustCopy: "Demo answers use sample records, not independently verified or live agricultural sources. We’ll say when we don’t know.",
    reviewedSources: "Illustrative demo records", languageSupport: "Your language, your way",
    demoNotice: "Educational demo · Not a substitute for local expert advice", needMoreHelp: "Need a little more help?",
    visitKvk: "Your local KVK is always a good place to start.", findYourKvk: "Find your nearest KVK",
    footerDisclaimer: "Demo agricultural guidance · Always verify locally", allSystemsDemo: "Demo is ready",
    thinking: "Finding trusted guidance…", answeredBy: "Krishi Voice", source: "SOURCE", published: "PUBLISHED",
    demoLabel: "DEMO GUIDANCE", confidence: "Confidence", speak: "Listen to answer", micStarting: "Starting microphone…",
    micListening: "Listening — speak your question", micNotSupported: "Voice input isn’t available in this browser.",
    micDenied: "Microphone access was not granted. You can type your question instead.", emptyQuestion: "Please type or speak a question first.",
    requestError: "We couldn’t reach the knowledge library. Please try again.", fallbackLabel: "No matching verified guidance",
    confidenceHigh: "Good match", confidenceGood: "Possible match", confidenceUnavailable: "Guidance unavailable"
  },
  mr: {
    workspace: "कार्यस्थळ", askAssistant: "सहाय्यकाला विचारा", quickQuestions: "जलद प्रश्न", resources: "संसाधने",
    knowledgeBase: "ज्ञान संग्रह", inSeason: "डेमो हंगाम", kharifSeason: "खरीप · डेमो", seasonNote: "आजची छोटी पावले, उद्याचे समृद्ध पीक.",
    farmer: "शेतकरी", demoKnowledge: "डेमो ज्ञान", helloFarm: "थोडीशी मदत मोठा फरक घडवते", goodMorning: "शुभ सकाळ, रमेश",
    welcomeSub: "आज तुमच्या शेतात काय सुरू आहे?", today: "आज", yourFarmPartner: "तुमचे शेत, आमची साथ",
    heroTitle: "योग्य निर्णयातून\nसमृद्ध पीक फुलते.", heroCopy: "तुमच्या भाषेत प्रश्न विचारा. विश्वासार्ह कृषी ज्ञानावर आधारित उपयुक्त मार्गदर्शन मिळवा.",
    askQuestion: "प्रश्न विचारा", practicalAdvice: "उपयुक्त मार्गदर्शन", howCanWeHelp: "आम्ही कशी मदत करू?",
    helpSub: "तुमच्या शब्दांत विचारा किंवा खालील प्रश्न वापरून पाहा.", farmerFirst: "शेतकरी-केंद्रित मार्गदर्शन",
    askKrishi: "कृषी व्हॉइसला विचारा", askHint: "तुमचा शेती साथी ऐकत आहे", ready: "तयार",
    questionPlaceholder: "पीक, माती, सिंचन याबद्दल विचारा...", enterHint: "विचारण्यासाठी Enter दाबा", askButton: "विचारा",
    tryAsking: "असे विचारून पाहा", popularQuestions: "लोकप्रिय प्रश्न", exampleCotton: "माझ्या कापसाची पाने पिवळी पडत आहेत",
    cropHealth: "पीक आरोग्य", exampleSoy: "सोयाबीनला किती वेळा पाणी द्यावे?", waterManagement: "जल व्यवस्थापन",
    examplePaddy: "भातासाठी कोणते खत सुचवले जाते?", soilNutrients: "माती आणि अन्नद्रव्ये",
    exampleScheme: "शेतकऱ्यांसाठी कोणत्या सरकारी योजना आहेत?", schemes: "सरकारी योजना",
    builtOnTrust: "विश्वासावर आधारित", adviceYouCanTrust: "विश्वासाने वापरा,\nउपयुक्त सल्ला.",
    trustCopy: "डेमो उत्तरे नमुना नोंदींवर आधारित आहेत; त्या स्वतंत्रपणे तपासलेल्या किंवा थेट कृषी स्रोत नाहीत. माहिती नसल्यास आम्ही सांगू.",
    reviewedSources: "प्रात्यक्षिक नमुना नोंदी", languageSupport: "तुमची भाषा, तुमची पद्धत",
    demoNotice: "शैक्षणिक डेमो · स्थानिक तज्ज्ञांच्या सल्ल्याचा पर्याय नाही", needMoreHelp: "अधिक मदत हवी आहे?",
    visitKvk: "स्थानिक कृषी विज्ञान केंद्रापासून सुरुवात करा.", findYourKvk: "जवळचे कृषी विज्ञान केंद्र शोधा",
    footerDisclaimer: "डेमो कृषी मार्गदर्शन · स्थानिक पातळीवर पडताळा", allSystemsDemo: "डेमो तयार आहे",
    thinking: "विश्वासार्ह मार्गदर्शन शोधत आहोत…", answeredBy: "कृषी व्हॉइस", source: "स्रोत", published: "प्रकाशित",
    demoLabel: "डेमो मार्गदर्शन", confidence: "विश्वास पातळी", speak: "उत्तर ऐका", micStarting: "मायक्रोफोन सुरू होत आहे…",
    micListening: "ऐकत आहे — तुमचा प्रश्न बोला", micNotSupported: "या ब्राउझरमध्ये आवाज इनपुट उपलब्ध नाही.",
    micDenied: "मायक्रोफोनची परवानगी मिळाली नाही. प्रश्न टाइप करू शकता.", emptyQuestion: "आधी प्रश्न टाइप करा किंवा बोला.",
    requestError: "ज्ञान संग्रहाशी संपर्क झाला नाही. पुन्हा प्रयत्न करा.", fallbackLabel: "पडताळलेले मार्गदर्शन सापडले नाही",
    confidenceHigh: "चांगला मेळ", confidenceGood: "संभाव्य मेळ", confidenceUnavailable: "मार्गदर्शन उपलब्ध नाही"
  },
  hi: {
    workspace: "कार्यस्थान", askAssistant: "सहायक से पूछें", quickQuestions: "त्वरित प्रश्न", resources: "संसाधन",
    knowledgeBase: "ज्ञान संग्रह", inSeason: "डेमो मौसम", kharifSeason: "खरीफ · डेमो", seasonNote: "आज के छोटे कदम, कल की बेहतर फसल।",
    farmer: "किसान", demoKnowledge: "डेमो ज्ञान", helloFarm: "छोटी मदद भी बड़ा बदलाव लाती है", goodMorning: "सुप्रभात, रमेश",
    welcomeSub: "आज आपके खेतों में क्या हो रहा है?", today: "आज", yourFarmPartner: "आपका खेत, हमारी साथ",
    heroTitle: "अच्छे फैसलों से\nअच्छी फसल उगती है।", heroCopy: "अपनी भाषा में सवाल पूछें। भरोसेमंद कृषि ज्ञान पर आधारित व्यावहारिक सलाह पाएं।",
    askQuestion: "सवाल पूछें", practicalAdvice: "व्यावहारिक सलाह", howCanWeHelp: "हम कैसे मदद करें?",
    helpSub: "अपने शब्दों में पूछें या नीचे दिए सवाल आज़माएं।", farmerFirst: "किसान-प्रथम मार्गदर्शन",
    askKrishi: "कृषि वॉइस से पूछें", askHint: "आपका खेती का साथी सुन रहा है", ready: "तैयार",
    questionPlaceholder: "फसल, मिट्टी, सिंचाई के बारे में पूछें...", enterHint: "पूछने के लिए Enter दबाएं", askButton: "पूछें",
    tryAsking: "ये पूछकर देखें", popularQuestions: "लोकप्रिय सवाल", exampleCotton: "मेरे कपास के पत्ते पीले हो रहे हैं",
    cropHealth: "फसल स्वास्थ्य", exampleSoy: "सोयाबीन में कितनी बार सिंचाई करें?", waterManagement: "जल प्रबंधन",
    examplePaddy: "धान के लिए कौन-सी खाद सुझाई जाती है?", soilNutrients: "मिट्टी और पोषक तत्व",
    exampleScheme: "किसानों के लिए कौन-सी सरकारी योजनाएं हैं?", schemes: "सरकारी योजनाएं",
    builtOnTrust: "विश्वास पर आधारित", adviceYouCanTrust: "भरोसेमंद सलाह,\nनिश्चिंत रहें।",
    trustCopy: "डेमो जवाब नमूना रिकॉर्ड पर आधारित हैं; ये स्वतंत्र रूप से सत्यापित या लाइव कृषि स्रोत नहीं हैं। जानकारी न होने पर हम बताएंगे।",
    reviewedSources: "उदाहरण डेमो रिकॉर्ड", languageSupport: "आपकी भाषा, आपका तरीका",
    demoNotice: "शैक्षिक डेमो · स्थानीय विशेषज्ञ की सलाह का विकल्प नहीं", needMoreHelp: "थोड़ी और मदद चाहिए?",
    visitKvk: "आपका स्थानीय कृषि विज्ञान केंद्र अच्छी शुरुआत है।", findYourKvk: "नजदीकी कृषि विज्ञान केंद्र खोजें",
    footerDisclaimer: "डेमो कृषि मार्गदर्शन · स्थानीय स्तर पर सत्यापित करें", allSystemsDemo: "डेमो तैयार है",
    thinking: "भरोसेमंद सलाह खोज रहे हैं…", answeredBy: "कृषि वॉइस", source: "स्रोत", published: "प्रकाशित",
    demoLabel: "डेमो मार्गदर्शन", confidence: "विश्वास स्तर", speak: "जवाब सुनें", micStarting: "माइक्रोफोन शुरू हो रहा है…",
    micListening: "सुन रहे हैं — अपना सवाल बोलें", micNotSupported: "इस ब्राउज़र में आवाज़ इनपुट उपलब्ध नहीं है।",
    micDenied: "माइक्रोफोन की अनुमति नहीं मिली। आप सवाल टाइप कर सकते हैं।", emptyQuestion: "पहले सवाल टाइप करें या बोलें।",
    requestError: "ज्ञान संग्रह से संपर्क नहीं हो पाया। कृपया फिर कोशिश करें।", fallbackLabel: "कोई सत्यापित सलाह नहीं मिली",
    confidenceHigh: "अच्छा मेल", confidenceGood: "संभावित मेल", confidenceUnavailable: "सलाह उपलब्ध नहीं"
  }
};

const languageSelect = document.getElementById("language");
const questionInput = document.getElementById("question-input");
const askButton = document.getElementById("ask-button");
const conversation = document.getElementById("conversation");
const voiceStatus = document.getElementById("voice-status");
const requestedLanguage = new URLSearchParams(window.location.search).get("lang");
const savedLanguage = window.localStorage.getItem("krishi-language");
if (["en", "hi", "mr"].includes(requestedLanguage || "")) {
  languageSelect.value = requestedLanguage;
} else if (["en", "hi", "mr"].includes(savedLanguage || "")) {
  languageSelect.value = savedLanguage;
}
let recognition = null;
let isListening = false;

function t(key) {
  const language = languageSelect.value;
  return translations[language]?.[key] || translations.en[key] || key;
}

function applyLanguage() {
  const language = languageSelect.value;
  document.documentElement.lang = language;
  window.localStorage.setItem("krishi-language", language);
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const value = translations[language][element.dataset.i18n];
    if (value) element.textContent = value;
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
    const value = translations[language][element.dataset.i18nPlaceholder];
    if (value) element.placeholder = value;
  });
  if ("speechSynthesis" in window) speechSynthesis.cancel();
}

function addMessage(question, response, loading = false) {
  const card = document.createElement("article");
  card.className = "answer-card";
  const userMessage = document.createElement("div");
  userMessage.className = "user-question";
  userMessage.innerHTML = '<span class="user-avatar">RK</span>';
  const questionText = document.createElement("p");
  questionText.textContent = question;
  userMessage.append(questionText);
  const responseHead = document.createElement("div");
  responseHead.className = "response-head";
  responseHead.innerHTML = `<span class="assistant-orb small-orb">✳</span><strong>${t("answeredBy")}</strong><span class="response-time">JUST NOW</span>`;
  const responseBody = document.createElement("p");
  responseBody.className = "response-body";
  responseBody.textContent = loading ? t("thinking") : response.answer;
  const details = document.createElement("div");
  details.className = "response-details";
  if (!loading) {
    if (response.source) {
      const citation = document.createElement("span");
      citation.className = "citation-chip";
      citation.textContent = `${t("source")}: ${response.source}`;
      details.append(citation);
      if (response.publication_date) {
        const published = document.createElement("span");
        published.className = "data-as-of";
        published.textContent = `${t("published")}: ${response.publication_date}`;
        details.append(published);
      }
    } else {
      const noMatch = document.createElement("span");
      noMatch.className = "fallback-note";
      noMatch.textContent = t("fallbackLabel");
      details.append(noMatch);
    }
    const confidence = document.createElement("span");
    confidence.className = "confidence-chip";
    confidence.textContent = `${t("confidence")}: ${response.confidence === "High" ? t("confidenceHigh") : response.matched ? t("confidenceGood") : t("confidenceUnavailable")}`;
    details.append(confidence);
    const listen = document.createElement("button");
    listen.className = "listen-button";
    listen.type = "button";
    listen.title = t("speak");
    listen.setAttribute("aria-label", t("speak"));
    listen.innerHTML = "◖";
    listen.addEventListener("click", () => speakAnswer(response.answer));
    details.append(listen);
    const demo = document.createElement("span");
    demo.className = "demo-source-note";
    demo.textContent = t("demoLabel");
    details.append(demo);
  }
  card.append(userMessage, responseHead, responseBody, details);
  conversation.prepend(card);
  return { card, responseBody, details };
}

async function submitQuestion(text = questionInput.value) {
  const question = text.trim();
  if (!question) {
    voiceStatus.textContent = t("emptyQuestion");
    questionInput.focus();
    return;
  }
  questionInput.value = "";
  voiceStatus.textContent = "";
  askButton.disabled = true;
  const elements = addMessage(question, null, true);
  try {
    const result = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, language: languageSelect.value })
    });
    if (!result.ok) throw new Error("Request failed");
    const response = await result.json();
    elements.card.remove();
    addMessage(question, response);
  } catch (error) {
    elements.responseBody.textContent = t("requestError");
  } finally {
    askButton.disabled = false;
  }
}

function speakAnswer(answer) {
  if (!("speechSynthesis" in window)) {
    voiceStatus.textContent = "Speech playback is not supported in this browser.";
    return;
  }
  speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(answer);
  utterance.lang = { en: "en-IN", hi: "hi-IN", mr: "mr-IN" }[languageSelect.value];
  speechSynthesis.speak(utterance);
}

function setupMicrophone() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const button = document.getElementById("mic-button");
  if (!SpeechRecognition) {
    button.addEventListener("click", () => {
      voiceStatus.textContent = t("micNotSupported");
    });
    return;
  }
  recognition = new SpeechRecognition();
  recognition.interimResults = true;
  recognition.continuous = false;
  recognition.maxAlternatives = 1;
  recognition.onstart = () => {
    isListening = true;
    button.classList.add("recording");
    voiceStatus.textContent = t("micListening");
  };
  recognition.onresult = (event) => {
    let transcript = "";
    for (let i = event.resultIndex; i < event.results.length; i++) transcript += event.results[i][0].transcript;
    questionInput.value = transcript;
  };
  recognition.onerror = (event) => {
    if (event.error === "not-allowed" || event.error === "service-not-allowed") voiceStatus.textContent = t("micDenied");
    else if (event.error !== "no-speech") voiceStatus.textContent = t("micNotSupported");
  };
  recognition.onend = () => {
    isListening = false;
    button.classList.remove("recording");
    if (questionInput.value.trim()) voiceStatus.textContent = "";
  };
  button.addEventListener("click", () => {
    if (isListening) recognition.stop();
    else {
      voiceStatus.textContent = t("micStarting");
      recognition.lang = { en: "en-IN", hi: "hi-IN", mr: "mr-IN" }[languageSelect.value];
      try { recognition.start(); }
      catch { voiceStatus.textContent = t("micStarting"); }
    }
  });
}

document.getElementById("today-date").textContent = new Intl.DateTimeFormat("en-IN", { day: "numeric", month: "short", year: "numeric" }).format(new Date());
languageSelect.addEventListener("change", applyLanguage);
askButton.addEventListener("click", () => submitQuestion());
questionInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    submitQuestion();
  }
});
document.querySelectorAll(".example-card").forEach((button) => {
  button.addEventListener("click", () => {
    questionInput.value = button.dataset.question;
    questionInput.focus();
    submitQuestion(button.dataset.question);
  });
});
setupMicrophone();
applyLanguage();
