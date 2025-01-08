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


def repo_setup_crew(directory: str, venv_path: str, python_version: str = "3.11"):
    print(directory)
    print(str(directory))
    dir_read_tool = DirectoryReadTool(directory=str(directory))
    shell_tool = ShellExecuteTool()

    devops = Agent(
        role="Senior DevOps Engineer",
        goal="Install the dependencies for a given python project.",
        backstory="""You are an experienced DevOps engineer.
        You received a python code base from a colleague.
        You need to figure out how to install its dependencies.""",
        tools=[dir_read_tool, shell_tool],
        verbose=True,
    )

    identify_dependencies = Task(
        description=f"""Screen the python code base under: '{directory}'.
        Identify how the dependencies of this python code base can be installed.""",
        expected_output="A plan on how to install the dependencies of this python code base.",
        agent=devops,
    )

    create_setup_script = Task(
        description="""Create a shell script that installs the needed dependencies.""",
        expected_output="A shell script that installs all needed python dependencies.",
        agent=devops,
        context=[identify_dependencies],
    )

    setup_repo = Task(
        description="Execute the shell script to create the python venv and install the needed dependencies.",
        expected_output="A successful creation of the venv and installation of the dependencies.",
        agent=devops,
        context=[create_setup_script],
    )

    crew = Crew(
        agents=[devops],
        tasks=[
            identify_dependencies,
            create_setup_script,
            setup_repo,
        ],
        process=Process.sequential,
        verbose=True,
    )

    crew.kickoff()
