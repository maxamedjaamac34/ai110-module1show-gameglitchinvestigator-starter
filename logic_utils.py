def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Refactored from app.py using Claude. I identified that the original
    # hints were inverted — "Go HIGHER!" was shown when the guess was too high,
    # and "Go LOWER!" when it was too low. I spotted this by reading the
    # check_guess logic and flagging the contradiction between the outcome label
    # ("Too High") and the hint message ("Go HIGHER!"). I verified the fix by
    # tracing through: if guess=60 and secret=50, guess > secret is True,
    # so outcome should be "Too High" with hint "Go LOWER!" — which is now correct.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
