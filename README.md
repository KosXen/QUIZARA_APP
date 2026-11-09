# ΚΟΥΙΖΑΡΑ (Quizara)

<img src="store/play_icon_512.png" alt="ΚΟΥΙΖΑΡΑ icon" width="120" align="right">

A Greek trivia party game for Android. Two teams (or two players) compete on one phone, usually
with a host reading the questions aloud. It works fully offline: no account, no ads, no permissions.

## Features

### Game modes
- **⚔ Μονομαχία (Duel)**: teams take turns on a board of 18 questions, one per category at ×1
  (easy), ×2 (medium) and ×3 (hard) points. Every new game deals a fresh random set from the
  question bank. Optional **Special** rounds add five mini-games:

  | Special | How it plays | Points |
  |---|---|---|
  | 🏆 TOP 5 | Name the 5 answers in a list | 5/5 = 2, stopped at 4/5 = 1 |
  | ◎ ΒΡΕΣ 3 | Name any 3 of the accepted answers | 2 |
  | 👤 PERSON ID | Guess the person from up to 3 clues | 3 / 2 / 1 by clue |
  | 🌐 COUNTRY ID | Guess the country from up to 3 clues | 3 / 2 / 1 by clue |
  | ↕ ΒΑΛΤΑ ΣΕ ΣΕΙΡΑ | Drag the items into the right order | 2 |

- **🧠 Κλασικό (Classic)**: pick two categories each turn and fill every category with 1, 2 or 3
  correct answers (short, medium or long game). A right answer keeps your turn. Each player has
  one **Κλοπή** (steal the opponent's missed question), one **Ανακάτεμα** (reshuffle the category
  choice) and one **Αλλαγή ερώτησης** (swap the question).

- **🔪 Sudden Death**: if a game ends in a tie, play it as a draw or spin the roulette for a
  tie-breaker: true/false, multiple choice, over/under, A/B, or closest number.

### Six categories
⚽ Sports · 🎨 Art · ⚛ Science · 🏛 History · 🧠 General knowledge · 🌐 Geography

### Questions included
| Set | Questions |
|---|---|
| Classic | 3,449 |
| Duel | 3,449 |
| Duel Specials | 700 |
| Sudden Death | 250 |

### Also
- **Διπλασιασμός (×2)**: each team can double the value of one question per game.
- **Μαθηματικό τέλος**: the game ends early once the trailing team can no longer catch up.
- Optional question timer (30 / 45 / 60 seconds), automatic save and resume, light and dark
  themes, and an **Εφέ** switch for sounds, vibration and animations.
- Result screens show the correct answer and wait for **ΣΥΝΕΧΕΙΑ**, so everyone can read it.

Runs on **Android 6.0 or newer**. The interface and the questions are in Greek.

## Download the app

Every push to `main` builds an APK on GitHub.

1. Open the [Actions tab](https://github.com/gkonstantos/QUIZARA-APP/actions/workflows/build-apk.yml) and click the latest green run.
2. Under **Artifacts**, download **KOUIZARA-debug** (you must be signed in to GitHub) and unzip it.
3. Copy `app-debug.apk` to your phone and open it. Android will ask you to allow installing apps
   from that source.

If an older build of the app is already installed and Android refuses to update it, uninstall it
first. (Builds signed by different machines can't update each other.)

## Run the project

### Requirements
- [Android Studio](https://developer.android.com/studio) (recent), or **JDK 17** plus the Android
  SDK for command-line builds.
- No other installs: the Gradle wrapper downloads Gradle 8.13, and the Android Gradle plugin
  downloads Android SDK platform 36 on the first build.

### Get the code
```bash
git clone https://github.com/gkonstantos/QUIZARA-APP.git
```

### With Android Studio
1. **File → Open** and select the `QUIZARA-APP` folder.
2. Wait for the Gradle sync to finish.
3. Connect a phone with USB debugging enabled (or start an emulator) and press **Run ▶**.

### From the command line
Set `ANDROID_HOME` to your Android SDK folder (on Windows usually
`%LOCALAPPDATA%\Android\Sdk`), then:

```bash
./gradlew :app:assembleDebug        # Windows: gradlew.bat :app:assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

## Editing the questions

The four files in `app/src/main/assets/` are generated from Excel sheets. To change the questions,
edit the sheets and regenerate:

```bash
pip install openpyxl
python tools/excel_to_json.py "path/to/the/excel/folder"
```

Then rebuild. Each file's role comes from its name: `SPORTS`, `ARTS`, `SCIENCE`, `HISTORY`,
`GENERAL`, `GEOGRAPHY` for the categories; `TOP5`, `FIND3`, `PERSON_ID`, `COUNTRY_ID`, `RANK` for
the Specials; and `TF_`, `MC_`, `OU_`, `AB_`, `CLOSEST_sudden_death` for Sudden Death. The script
stops with an error if a mode would be left without the questions it needs.

The launcher icons and the Play Store icon (`store/play_icon_512.png`) come from the logo. Run
`python tools/make_icons.py` (needs `pip install pillow`) if the logo changes.

## Project layout

```
app/src/main/java/.../MainActivity.java   the whole game (plain Java, no libraries)
app/src/main/assets/                       question banks (JSON)
app/src/main/res/                          logo, sounds, launcher icons, theme
tools/                                     Excel → JSON converter, icon generator
store/                                     Play Store icon and icon preview
.github/workflows/build-apk.yml            CI build that produces the APK
```

## Version

**0.10.5** (version code 23), package `com.monomaxia.gnoseon`. Changes on top of the original
0.10.5 release:
- Full question bank, generated from Excel.
- Duel deals a random board from the full bank on every new game.
- Sounds no longer freeze the screen when cards flip; smoother roulette.
- Result screens wait for **ΣΥΝΕΧΕΙΑ** and always show the answer.
- Fixed a crash on Android 6.
- Launcher icon; default team names **Ομάδα 1** / **Ομάδα 2**.
