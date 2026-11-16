# AI DEVELOPMENT LOG
#
# Copilot Prompt 1:Help me create a beginner-friendly Python program that asks a user questions about a suspicious email and gives it a low, medium, or high phishing risk rating.
#
# Copilot Prompt 2: have it use this scoring method:
# 0–1 warning signs = LOW RISK
# 2–3 warning signs = MEDIUM RISK
# 4 or more warning signs = HIGH RISK
#
# Copilot Prompt 3: Your final result should display the risk score, the
# Low/Medium/High risk level, the warning signs detected, and a short
# recommendation for the user. Store the detected warning signs in a Python
# list. The program should also ask whether the user wants to analyze another
# message.
#
# One problem or bug I encountered:It didnt have alot of color to stand out 
#
# How I fixed it:Asked for CoPilot to add color 
#
# One change I made myself without Copilot:I wanted to add that if you suspect it then report it.

# 1. How does your program calculate the phishing risk? On a scale of 1-5 1=low risk and 5=high risk
# 2. Why does your program use a list to store warning signs?As a check list to let you know what was detected through the asking of the questions 
# 3. Why can a suspicious link be a sign of phishing?As most are from unknown or slightly mimiced sites or places with minor spelling errors so that the untrained eye wont easily pick up on it as it may look genuine

"""A beginner-friendly interactive phishing risk analyzer."""


QUESTIONS = [
    "Is the sender unfamiliar or unexpected?",
    "Does the message pressure you to act immediately?",
    "Does it request a password, payment, or other private information?",
    "Does it include a link that looks unfamiliar or suspicious?",
    "Does it include an attachment you were not expecting?",
    "Does it use a generic greeting or contain unusual spelling and grammar?",
]

RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"


def ask_yes_or_no(question):
    """Ask one yes/no question and return True for yes."""
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Please answer with 'y' for yes or 'n' for no.")


def get_risk_level(score):
    """Convert the number of warning signs into a risk level."""
    if score <= 1:
        return "Low"
    if score <= 3:
        return "Medium"
    return "High"


def get_risk_color(risk_level):
    """Choose a color that matches the risk level."""
    colors = {"Low": GREEN, "Medium": YELLOW, "High": RED}
    return colors[risk_level]


def main():
    """Ask about an email and display its phishing risk rating."""
    print(f"{CYAN}=== Phishing Risk Analyzer ==={RESET}")

    while True:
        print("\nAnswer these questions about the email you want to check.")

        score = 0
        detected_warning_signs = []
        for question in QUESTIONS:
            if ask_yes_or_no(question):
                score += 1
                detected_warning_signs.append(question)

        risk_level = get_risk_level(score)
        risk_color = get_risk_color(risk_level)

        print("\n" + "=" * 40)
        print("ANALYSIS SUMMARY")
        print("=" * 40)
        print(f"Risk score: {risk_color}{score} out of {len(QUESTIONS)}{RESET}")
        print(f"Risk level: {risk_color}{risk_level.upper()} RISK{RESET}")
        print(f"{YELLOW}Warning signs detected:{RESET}")
        if detected_warning_signs:
            for warning_sign in detected_warning_signs:
                print(f"{RED}- {warning_sign}{RESET}")
        else:
            print(f"{GREEN}- None detected{RESET}")

        if risk_level == "High":
            recommendation = (
                "Do not click links, open attachments, or reply with personal information."
            )
        elif risk_level == "Medium":
            recommendation = "Pause and verify the sender using a trusted contact method."
        else:
            recommendation = "No major warning signs were found, but continue to stay cautious."

        print(f"\nRecommendation: {recommendation}")
        print(
            f"{YELLOW}If you suspect this email is phishing, report it to your "
            f"email provider or organization's IT/security team.{RESET}"
        )
        print(
            f"{CYAN}Cybersecurity tip: Hover over links before clicking them "
            f"and check the web address carefully.{RESET}"
        )
        print("=" * 40)

        if not ask_yes_or_no("\nWould you like to check another email?"):
            print("\nThank you for using the Phishing Risk Analyzer.")
            break


if __name__ == "__main__":
    main()
