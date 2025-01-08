import os
import subprocess
import json
import shutil
import git
from fastapi import FastAPI
from dotenv import load_dotenv

from openqa.api.models.api_request_models import (
    RepoCloneRequest,
    FormatCheckRequest,
    SetupEnvRequest,
    PylintRequest,
)
from openqa.api.formatter.black import run_black
from openqa.api.setup_env.setup_env import setup_env
from openqa.api.linter.pylint import run_pylint

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
    setup_env()


@app.post("/pylint-check/")
async def pylint_check(request: PylintRequest):
    return run_pylint(venv_dir=request.venv_directory, repo_dir=request.directory)
