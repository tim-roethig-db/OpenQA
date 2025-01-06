import os
import subprocess
import json
import shutil
import git
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from openqa.api.models.api_request_models import (
    RepoCloneRequest,
    FormatCheckRequest,
    SetupEnvRequest,
    PylintRequest,
)
from openqa.api.formatter.black import run_black
from openqa.api.setup.install_dependencies import repo_setup_crew

load_dotenv()

app = FastAPI()


@app.post("/clone-repo/")
async def clone_repo(request: RepoCloneRequest):
    # Remove the target directory if it already exists
    if os.path.exists(request.directory):
        os.system(f"rm -rf {request.directory}")

    # Clone the repository
    git.Repo.clone_from(request.url, request.directory)

    return {"message": "Repository cloned successfully"}


@app.post("/format-check/")
async def format_check(request: FormatCheckRequest):
    return run_black(target_dir=request.directory)


@app.post("/setup-environment/")
async def setup_environment(request: SetupEnvRequest):
    repo_setup_crew(
        directory=request.directory,
        venv_path=request.venv_directory,
        python_version=request.python_version,
    )


@app.post("/pylint-check/")
async def pylint_check(request: PylintRequest):
    python_executable = (
        os.path.join(request.venv_directory, "bin", "python")
        if os.name != "nt"
        else os.path.join(request.venv_directory, "Scripts", "python.exe")
    )

    # Run pylint with JSON output on the target directory
    result = subprocess.run(
        [python_executable, "-m", "pylint", str(request.directory), "-f", "json"],
        capture_output=True,
        text=True,
        check=True,
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
