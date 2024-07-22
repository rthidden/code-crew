from crewai_tools import BaseTool, tool, GithubSearchTool

@tool
def CustomReactTool():
    "React is a JavaScript library for building user interfaces."
    pass

@tool
def CustomDjangoTool():
    "Django is a high-level Python web framework that encourages rapid development."
    pass

@tool
def CustomDockerTool():
    "Docker is a set of platform as a service products that use OS-level virtualization."
    pass


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
