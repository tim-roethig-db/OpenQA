from crewai import Agent
from crewai_tools import CodeInterpreterTool, DirectoryReadTool, DirectorySearchTool

from tools import ShellExecuteTool


code_interpreter_tool = CodeInterpreterTool()
dir_read_tool = DirectoryReadTool(
    directory="/Users/tim/Desktop/Projekte/OpenQA/target_repo"
)
dir_search_tool = DirectorySearchTool()
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
