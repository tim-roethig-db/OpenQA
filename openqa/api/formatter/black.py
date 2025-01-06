import subprocess


def run_black(target_dir: str):
    # Run black with --check on the target directory
    result = subprocess.run(
        ["black", "--check", target_dir], capture_output=True, text=True
    )

    # Check the return code to determine if the check passed or failed
    if result.returncode == 0:
        return {"message": "pass"}

    return {"message": "fail", "output": result.stderr}
