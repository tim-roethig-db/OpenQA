from crewai import Agent, Task, Crew, Process
from crewai_tools import DirectoryReadTool
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.tools import ShellTool
from dotenv import load_dotenv


load_dotenv()


class ShellExecuteTool(BaseTool):
    name: str = "Shell Execute Tool"
    description: str = "Executes shell scripts."
    shell_tool: ShellTool = Field(default_factory=ShellTool)

    def _run(self, shell_script: str) -> str:
        """Execute the shell_script."""
        try:
            return self.shell_tool.run(shell_script)
        except Exception as e:
            return f"Error running shell script: {str(e)}"


def repo_setup_crew():
    repo_dir = "/target_repo"
    app_venv_dir = "/app_venv"
    dir_read_tool = DirectoryReadTool(directory=str(repo_dir))
    shell_tool = ShellExecuteTool()

    devops = Agent(
        role="Senior DevOps Engineer",
        goal="Install the dependencies for a given python project.",
        backstory="""You are an experienced DevOps engineer.
You received a python code base from a colleague.
You need to figure out how to install its dependencies on debian linux.""",
        tools=[dir_read_tool, shell_tool],
        verbose=True,
    )

    identify_dependencies = Task(
        description=f"""Screen the python code base under: '{repo_dir}'.
Identify:
1. Which python version is suited best for the code base. 
Prefer python 3.11 if nothing contradicting is specified.
2. How the dependencies of this python code base can be installed.""",
        expected_output="A plan on how to install the dependencies of this python code base.",
        agent=devops,
    )

    create_setup_script = Task(
        description=f"""Create and run a shell script that:
1. Creates a venv with the suited python version under '{app_venv_dir}'.
2. Installs the dependencies inside this venv.

Note: python venv is available to you in python version 3.9, 3.10 and 3.11. If another version is required you need to install it yourself.""",
        expected_output=f"A python venv with the suited python version under '{app_venv_dir}' and all needed python dependencies installed within.",
        agent=devops,
        context=[identify_dependencies],
    )

    crew = Crew(
        agents=[devops],
        tasks=[
            identify_dependencies,
            create_setup_script,
        ],
        process=Process.sequential,
        verbose=True,
    )

    crew.kickoff()


if __name__ == "__main__":
    repo_setup_crew()
