# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I run it, the game worked okay. However, after I tried to restart, it would not let me click 'New Game' button. 
- List at least two concrete bugs you noticed at the start  
The game's Hard difficult range is wrong. Hard should return the range 1-100, but now it returns 1-50.

The game does not stop me from guessing numbers below zero even though I was supposed to guess numbers between each difficult range.

Another problem is that easy is from range 1-20, and normal should be 1-50 but it's 1-100 which should be maximum difficulty. So, the number of questions that noraml and hard should be displaying are switched.

A fourth bug I found was that the info banner at the top of the game always displayed "Guess a number between 1 and 100" no matter which difficulty was selected. The range was hardcoded in the UI instead of using the actual values from get_range_for_difficulty. I fixed this by replacing the hardcoded values with the dynamic low and high variables so the message now correctly updates when switching between Easy (1–20), Normal (1–50), and Hard (1–100).

**Bugs identified by Claude (AI-found):**

A fifth bug Claude identified was that every even-numbered attempt, the app was secretly converting the secret number from an integer to a string before passing it to check_guess. This caused a TypeError crash because Python cannot compare an int to a str using > or <. Claude spotted this by reading the submit handler in app.py and flagging the intentional-looking if/else block that was corrupting the secret type.

A sixth bug Claude identified was that the New Game button was not fully resetting the game state. It only reset the attempts counter and generated a new secret, but left status, score, and history unchanged. This meant that after winning or losing, clicking New Game still showed the "You already won" or "Game over" message and blocked further play. Claude also noticed the secret was being generated with a hardcoded range of 1–100 instead of using the selected difficulty range. Both issues were fixed by resetting all session state variables and using low/high from get_range_for_difficulty.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested that hints are inverted. So, in the statement (if guess > secret), the statement is backwards because if the guess is too high, then the message says "Go Higher" instead of tell me to "Go Lower" and vice versa. I verified this by visitng that exact line in the code.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I don't recall any AI suggestion that was incorrect or misleading other than Claude claiming that it identified the bugs I already told it to fix.
---


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I wrote pytests that I asserted values and when tests passed, I knew it was running correctly.
An example of a test that I delegated the task of writing the test to Ai was to write a test that checks If secret is 50 and guess is 60, hint should be "Too High" and not "Too Low" like before.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
The probmem was that Streamlit reran the entire script from top to bottom every time the user interacted with anything — like clicking a button or typing. If the secret was set with just secret = random.randint(...) (a plain variable, not stored in session state), it was generating a brand new random number on every rerun, so the target kept changing mid-game.

I introduced a conditional statement like 'if "secret" not in st.sessions_state, only then can the system generate a new random number.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Writing pytest tests right after fixing a bug. In this project, every time I fixed a bug I immediately wrote a test to confirm it — like checking that a guess of 60 against secret 50 returns "Too High" with a "Go LOWER" hint. This gave me confidence the fix actually worked and didn't break anything else. I want to keep doing this in future labs.

I would verify AI suggestions before accepting them rather than trusting them at face value. Claude listed several bugs but some of them were things I already pointed out myself. Next time I'll be more specific in my prompts and cross-check the AI's output against the actual code before making changes.

This project showed me that AI-generated code can have subtle, intentional-looking bugs that are hard to spot without reading closely. I now treat AI-generated code the same way I'd treat code from anyone else — I read it, question it, and test it before trusting it with production grade systems.