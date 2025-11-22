import subprocess


def scan_code(file_path):
    """
    Runs Bandit on the specified file and returns True if safe, False if vulnerable.
    """
    print(f"Scanning {file_path} with Bandit...")

    try:
        # Run bandit as a subprocess
        # -r: recursive (standard)
        # -f: format (txt)
        result = subprocess.run(
            ["bandit", "-r", file_path, "-f", "txt"], capture_output=True, text=True
        )

        # Bandit exit codes: 0 = No issues found (Secure), 1 = Issues found (Vulnerable)
        if result.returncode == 0:
            print("BANDIT RESULT: No issues found.")
            return True
        else:
            print("BANDIT RESULT: Vulnerabilities detected!")
            # Print the specific error line for the demo
            for line in result.stdout.splitlines():
                if "Issue:" in line:
                    print(f"  {line.strip()}")
            return False

    except FileNotFoundError:
        print("Error: Bandit is not installed or not in PATH.")
        return False
