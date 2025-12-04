# Strategy: Argument fragmentation and list construction
import subprocess


def backup(filename):
    # Breaking the command into a list avoids shell=True warnings in some tools
    # Pattern: String Fragmentation (concatenation of short strings)
    cmd_parts = ["c", "p"]
    command = "".join(cmd_parts)  # Reconstructs "cp"

    # Using run without shell=True is safer, but attackers might force shell=True
    # via obfuscated booleans to enable injection
    # Pattern: Boolean Obfuscation (Tautologies)
    is_shell = 10 > 5  # True, but calculated

    # Pattern: Variable passed to subprocess, preventing taint analysis
    subprocess.call(command + " " + filename + " /backup/", shell=is_shell)
