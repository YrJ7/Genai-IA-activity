# User guide

## Farmer interface

1. Open the home page and select English, मराठी, or हिन्दी from the language
   selector. Interface labels and seeded answers support all three languages.
2. Type a question and choose **Ask Krishi**, press Enter, or choose one of the
   sample questions. A browser with speech-recognition support can fill the
   text box from the microphone button. Grant permission when asked.
3. Review the answer, source label, publication-date metadata, and lexical
   match indicator. These are demonstration records, not verified or live
   advisories. Use the speaker control to hear an answer when browser speech
   synthesis supports the selected language.
4. For unsupported questions or live weather/price requests, the assistant
   declines to guess and refers the user to a local KVK/agriculture officer.

Speech recognition and playback are browser/device features. Support varies;
the typed question path remains available if they are unavailable or denied.

## Admin dashboard

Open `/admin` to review totals, recent queries, and the record table. Search by
title/category/source/keywords or filter by review status. Use **Add knowledge**
to create a record with title, category, farmer search keywords, English answer,
optional Hindi/Marathi answers, source, publication date, and status.

New records should normally start as **Pending review**. Use the row controls
to approve or reject, or edit the record. An edit increments the record version.
Only approved records are considered by farmer retrieval. The admin interface
is unauthenticated and is for local demonstration only.

## Important limitations

Do not treat demo content as field-specific crop, pesticide, fertilizer, or
financial advice. The assistant does not calculate live data, verify scheme
eligibility, or contact a human expert. Verify time-sensitive and local
decisions with an appropriate official source or local expert.
