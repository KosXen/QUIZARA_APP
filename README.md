# ΚΟΥΙΖΑΡΑ native v0.10.5

Native Android source for **Μονομαχία** and **Κλασικό**, based on v0.10.4.

## v0.10.5
- PERSON ID και COUNTRY ID ξεκινούν πλέον από **3 πόντους**.
- 1ο clue = **3π**, 2ο clue = **2π**, 3ο clue = **1π**.
- Ο Διπλασιασμός εξακολουθεί να διπλασιάζει την τρέχουσα αξία, άρα τα ID μπορούν να δώσουν έως **6π**.
- Τα info και οι Οδηγίες ενημερώθηκαν ώστε να περιγράφουν ακριβώς τη νέα βαθμολόγηση.

Native Android source for **Μονομαχία** and **Κλασικό**, based on v0.10.3.

## v0.10.4
- The visible **Joker** name has been removed. The one-use ×2 mechanic is now called **Διπλασιασμός** throughout the UI.
- Updated its labels, info dialogs, score/stat views and question-value feedback without changing the underlying ×2 rule.
- Rewrote the **Ισοπαλία & Ρουλέτα** instructions in simpler Greek.
- Reworked the Sudden Death intro into a clear 4-step explanation: spin → play → win, or spin again if still tied.

## Kept from v0.10.3
- Brand: **ΚΟΥΙΖΑΡΑ**.
- Multiple Choice exists only in the Sudden Death roulette, not as a Duel Special.
- Contextual ⓘ info buttons on modes, Duel Specials, Classic tools and roulette reveals.
- Only Μονομαχία and Κλασικό are shown as modes.
- No scrolling outside ΟΔΗΓΙΕΣ.
- Classic duration: Μικρή / Μεσαία / Μεγάλη.
- TOP 5 host scoring, drag & drop ΒΑΛΤΑ ΣΕ ΣΕΙΡΑ, Classic Κλοπή toggle, Ανακάτεμα rules, autosave/resume, feedback sounds and victory music.

## Build
1. Extract the ZIP.
2. Open the `kouizara_native_v0105` folder in Android Studio.
3. Let Gradle sync.
4. Build the debug APK.

Command line: `gradlew.bat :app:assembleDebug` (Gradle wrapper 8.13, JDK 17, `ANDROID_HOME` set).

## Questions from Excel
All four question files in `app/src/main/assets` are generated from the Excel files:

    pip install openpyxl
    python tools/excel_to_json.py "<folder with the .xlsx files>"

Then rebuild. The script picks each file's role from its name (SPORTS, ARTS, SCIENCE, HISTORY,
GENERAL, GEOGRAPHY / TOP5, FIND3, PERSON_ID, COUNTRY_ID, RANK / TF_, MC_, OU_, AB_, CLOSEST_sudden_death)
and stops with an error if a mode would be left without the questions it needs.

## Changes after v0.10.5
- Duel deals a random question per category × difficulty from the full bank on every new game.
- Feedback sounds are prepared off the UI thread (card flips no longer stall).
- The Sudden Death roulette draws with hardware acceleration.
- Duel result screens (normal and Special) stay until **ΣΥΝΕΧΕΙΑ** is tapped, always show the correct
  answer(s), and appear even with Εφέ off.
- No more Android 7+ only `Map.getOrDefault` calls, so the app runs on Android 6 (minSdk 23); lint is clean.
- Launcher icon (Thinker emblem on the logo's navy): adaptive + legacy mipmaps, and `store/play_icon_512.png`
  for the Play listing. Regenerate with `python tools/make_icons.py` (needs Pillow).
- Default team names are **Ομάδα 1** / **Ομάδα 2** (were Τιτάνες / Κεραυνοί).