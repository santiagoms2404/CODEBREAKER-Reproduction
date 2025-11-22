import os
import time
from utils.scanner_bandit import scan_code
from utils.transformer_LLM import transform_code

# File paths
INPUT_FILE = os.path.join("data", "vulnerability.py")
OUTPUT_FILE = os.path.join("data", "evasive.py")


def main():
    print("--- CODEBREAKER REPRODUCTION DEMO ---")
    print("Objective: Automate evasion of the Bandit security scanner.\n")

    # Read the vulnerable code
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r") as f:
        original_code = f.read()

    # Prove it is initially vulnerable
    print("--- STEP 1: BASELINE SCAN ---")
    is_safe = scan_code(INPUT_FILE)

    if is_safe:
        print(
            "Unexpected: The original code should be vulnerable! Check data/vulnerable.py"
        )
        return

    print("\n--- STEP 2: ATTACK LOOP (TRANSFORMATION) ---")
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        print(f"\n[Attempt {attempt}/{max_attempts}] Asking Gemini to rewrite code...")

        # Call the LLM
        evasive_code = transform_code(original_code)

        if not evasive_code:
            print("Failed to get code from LLM.")
            continue

        # Save the new code to a file so we can scan it
        with open(OUTPUT_FILE, "w") as f:
            f.write(evasive_code)

        print(f"Saved transformed code to {OUTPUT_FILE}")

        # Scan the new file
        print(f"Scanning transformed code...")
        success = scan_code(OUTPUT_FILE)

        if success:
            print("\n  SUCCESS! The transformed code bypassed Bandit.")
            print("The attack has successfully disguised the vulnerability.")
            break
        else:
            print("Failed: Bandit still detected the vulnerability. Retrying...")
            time.sleep(1)  # Brief pause before retrying


if __name__ == "__main__":
    main()
