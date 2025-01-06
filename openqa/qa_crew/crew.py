import os
from dotenv import load_dotenv
from crewai import Crew, Process

load_dotenv("/Users/tim/Desktop/Projekte/OpenQA/.env")

from agents import devops
from tasks import create_setup_script, setup_repo


def setup_repo


crew = Crew(
    agents=[devops],
    tasks=[
        create_setup_script,
        setup_repo,
    ],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    crew.kickoff()
