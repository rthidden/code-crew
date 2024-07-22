from crewai_tools import BaseTool, tool

# tools/custom_tool.py
@tool
def CustomReactTool():
    return "React is a JavaScript library for building user interfaces."

@tool
def CustomDjangoTool():
    return "Django is a high-level Python web framework that encourages rapid development."

@tool
def CustomDockerTool():
    return "Docker is a set of platform as a service products that use OS-level virtualization."

# class MyCustomTool(BaseTool):
#    name: str = "Name of my tool"
#    description: str = (
#        "Clear description for what this tool is useful for, you agent will need this information to use it."
#    )
#
#    def _run(self, argument: str) -> str:
#        # Implementation goes here
#        return "this is an example of a tool output, ignore it and move along."
