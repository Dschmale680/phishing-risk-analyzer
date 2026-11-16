"""A small, beginner-friendly phishing risk checker."""


QUESTIONS = (
    ("unknown_sender", "Do you not know the sender, or did you not expect this email?"),
    ("urgent_request", "Does the email pressure you to act quickly?"),
    ("sensitive_request", "Does it ask for a password, payment, or other sensitive information?"),
    ("suspicious_link", "Does it contain a suspicious link or an unexpected attachment?"),
    ("unusual_greeting", "Does the greeting, spelling, or writing seem unusual?"),
)

RISK_POINTS = {
    "unknown_sender": 2,
    "urgent_request": 2,
    "sensitive_request": 3,
    "suspicious_link": 2,
    "unusual_greeting": 1,
}


def ask_yes_no(question, input_fn=input, print_fn=print):
    """Ask a question until the user enters yes or no."""
    while True:
        answer = input_fn(f"{question} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print_fn("Please answer with y/yes or n/no.")


def calculate_risk(answers):
    """Return the score and risk level for a dictionary of boolean answers."""
    score = sum(
        points for question, points in RISK_POINTS.items() if answers.get(question, False)
    )
    if score >= 6:
        level = "high"
    elif score >= 3:
        level = "medium"
    else:
        level = "low"
    return score, level


def main(input_fn=input, print_fn=print):
    """Ask about an email and display a risk rating."""
    print_fn("Phishing Risk Analyzer")
    print_fn("Answer a few questions about the suspicious email.\n")

    answers = {
        key: ask_yes_no(question, input_fn, print_fn) for key, question in QUESTIONS
    }
    score, level = calculate_risk(answers)

    print_fn(f"\nPhishing risk: {level.upper()} (score: {score}/10)")
    if level == "high":
        print_fn("Do not click links, open attachments, or reply. Contact the sender another way.")
    elif level == "medium":
        print_fn("Be careful. Verify the sender and request using a trusted method.")
    else:
        print_fn("The email has few warning signs, but continue to use caution.")


if __name__ == "__main__":
    main()
