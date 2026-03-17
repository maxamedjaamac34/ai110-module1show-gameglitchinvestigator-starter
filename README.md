# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose
This is a number guessing game where the player tries to guess a secret number within a limited number of attempts. The player selects a difficulty (Easy, Normal, or Hard) which determines the number range and attempt limit. After each guess, the game gives a hint telling the player to guess higher or lower.

### Bugs Found

| # | Location | Description |
|---|----------|-------------|
| 1 | `get_range_for_difficulty` | Hard and Normal difficulty ranges were swapped — Normal returned `1–100` and Hard returned `1–50`, which is backwards |
| 2 | `check_guess` | Hints were inverted — "Go HIGHER!" was shown when the guess was too high, and "Go LOWER!" when too low |
| 3 | `check_guess` (app.py) | On every even-numbered attempt, the secret was converted to a string, causing broken comparisons |
| 4 | New Game button | Clicking "New Game" did not reset `status` or `score`, so a finished game stayed locked |
| 5 | UI hint message | The info banner always said "Guess a number between 1 and 100" regardless of difficulty |

### Fixes Applied

1. **Swapped difficulty ranges** — `get_range_for_difficulty` now correctly returns `1–20` for Easy, `1–50` for Normal, and `1–100` for Hard.

2. **Fixed inverted hints** — Refactored `check_guess` out of `app.py` and into `logic_utils.py` with corrected messages:
   - `guess > secret` → outcome `"Too High"`, hint `"Go LOWER!"`
   - `guess < secret` → outcome `"Too Low"`, hint `"Go HIGHER!"`

3. **Added pytest tests** — Written in `tests/test_game_logic.py` to verify both the outcome labels and the hint messages are correct after the fix. All 5 tests pass.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
