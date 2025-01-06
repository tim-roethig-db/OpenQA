import os
import subprocess
import json


def run_pylint(venv_dir: str, repo_dir: str):
    python_executable = (
        os.path.join(venv_dir, "bin", "python")
        if os.name != "nt"
        else os.path.join(venv_dir, "Scripts", "python.exe")
    )

    # install pylint
    subprocess.run([python_executable, "-m", "pip", "install", "pylint"], check=True)

    # Run pylint with JSON output on the target directory
    result = subprocess.run(
        [python_executable, "-m", "pylint", str(repo_dir), "-f", "json"],
        capture_output=True,
        text=True,
    )

    # Parse the JSON output
    pylint_output = json.loads(result.stdout)
    print(pylint_output)

    # Filter errors and warnings
    errors = [item for item in pylint_output if item["type"] == "error"]
    warnings = [item for item in pylint_output if item["type"] == "warning"]

    # Determine the message based on the output
    if errors:
        return {"message": "fail", "output": errors}
    elif warnings:
        return {"message": "warning", "output": warnings}
    else:
        return {"message": "pass", "output": pylint_output}
