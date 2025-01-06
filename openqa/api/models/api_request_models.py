from pydantic import BaseModel, HttpUrl, DirectoryPath, Field, NewPath


class RepoCloneRequest(BaseModel):
    url: HttpUrl = Field(..., example="https://github.com/tim-roethig-db/amondin.git")
    directory: NewPath = Field(
        ..., example="/Users/tim/Desktop/Projekte/OpenQA/target_repo"
    )


class FormatCheckRequest(BaseModel):
    directory: DirectoryPath = Field(
        ..., example="/Users/tim/Desktop/Projekte/OpenQA/target_repo"
    )


class SetupEnvRequest(BaseModel):
    directory: DirectoryPath = Field(
        ..., example="/Users/tim/Desktop/Projekte/OpenQA/target_repo"
    )
    venv_directory: DirectoryPath = Field(
        ..., example="/Users/tim/Desktop/Projekte/OpenQA"
    )
    python_version: str = "3.11"


class PylintRequest(BaseModel):
    directory: DirectoryPath = Field(
        ..., example="/Users/tim/Desktop/Projekte/OpenQA/target_repo"
    )
    venv_directory: DirectoryPath = Field(
        ..., example="/Users/tim/Desktop/Projekte/OpenQA/venv"
    )
    python_version: str = "3.11"
