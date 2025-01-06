from crewai import Task

from agents import devops


identify_dependencies = Task(
    description="""Screen the python code base under: /Users/tim/Desktop/Projekte/OpenQA/target_repo.
    Identify how the dependencies of this python code base can be installed.""",
    expected_output="A plan on how to install the dependencies of this python code base.",
    agent=devops
)

create_setup_script = Task(
    description="""Create a shell script that:
    1. Creates a python venv under /Users/tim/Desktop/Projekte/OpenQA.
    2. Installs the needed dependencies within this venv.""",
    expected_output="A shell script that creates a python venv and installs all python dependencies.",
    agent=devops,
)

setup_repo = Task(
    description="Execute the shell script to create the python venv and install the needed dependencies.",
    expected_output="A successful creation of the venv and installation of the dependencies.",
    agent=devops,
)
