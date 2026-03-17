from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX: Added by refactoring check_guess with Claude as a partner.
# Claude identified that the hint messages were inverted — "Go HIGHER!" was shown
# when the guess was too high, and "Go LOWER!" when too low. These tests verify
# the corrected hint messages after the fix.
def test_too_high_hint_message():
    # Guess of 60 against secret 50: should tell player to go LOWER
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_hint_message():
    # Guess of 40 against secret 50: should tell player to go HIGHER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
