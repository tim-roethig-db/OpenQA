from enum import Enum
from typing import Optional
import ast
import subprocess
from pydantic import BaseModel, HttpUrl, field_validator, Field




class RepoType(str, Enum):
    WEB_API = "web_api"
    UI = "ui"
    OTHER = "other"

class RepoMeta(BaseModel):
    type: RepoType = Field(
        description=(
            "The type of application in the code base."
            "Options are:"
            "'web_api': If the code base is a web API which processes http or https requests."
            "'ui': If the code base is a frontend / UI."
            "'multi_repo': If the repo contains a UI and a web API."
            "'other': If the repo can not be classified as UI or web API."
            ))
    openapi_json_url: Optional[str] = Field(
        default=None, 
        description="The full URL to the openapi.json if the code base contains a web api.")
    setup_script: str = Field(description="Either a shell or a python script to install the needed dependencies and setup the environment for the code base.")
    start_script: str = Field(description="Either a shell or a python script to run the code base.")

    @field_validator("setup_script", "start_script")
    def validate_script(cls, v):
        # Check if it's a valid Python script
        try:
            ast.parse(v)
            return v
        except SyntaxError:
            pass

        # Check if it's a valid shell script
        try:
            subprocess.run(['bash', '-n'], input=v, text=True, check=True)
            return v
        except subprocess.CalledProcessError:
            pass

        raise ValueError('The script must be a valid Python or shell script')