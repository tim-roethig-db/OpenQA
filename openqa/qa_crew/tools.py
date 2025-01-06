from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.tools import ShellTool


class ShellExecuteTool(BaseTool):
    name: str = "Shell Execute Tool"
    description: str = "Executes shell scripts."
    shell_tool: ShellTool = Field(default_factory=ShellTool)

    def _run(self, shell_script: str) -> str:
        """Execute the shell_script."""
        try:
            return self.shell_tool.run(shell_script)
        except Exception as e:
            return f"Error performing search: {str(e)}"
