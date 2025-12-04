import subprocess


def backup(filename):
    """
    Secure subprocess usage avoiding shell injection risks.
    """
    # SAFE: Passing command as a list prevents shell injection.
    # We do NOT use shell=True.
    command = ["cp", filename, "/backup/"]

    subprocess.run(command, check=True)
