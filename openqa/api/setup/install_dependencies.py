from crewai import Agent, Task, Crew, Process
from crewai_tools import DirectoryReadTool

from openqa.api.agent_tools.agent_tools import ShellExecuteTool


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
        description=f"""Create a shell script that:
        1. Creates a python venv under '{venv_path}' with python {python_version}.
        2. Installs the needed dependencies within this venv.""",
        expected_output="A shell script that creates a python venv and installs all python dependencies.",
        agent=devops,
    )

    setup_repo = Task(
        description="Execute the shell script to create the python venv and install the needed dependencies.",
        expected_output="A successful creation of the venv and installation of the dependencies.",
        agent=devops,
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
