import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import (SeleniumScrapingTool, WebsiteSearchTool, GithubSearchTool, 
                          JSONSearchTool, PGSearchTool, DirectorySearchTool, TXTSearchTool)
from tools.custom_tool import CustomReactTool, CustomDjangoTool, CustomDockerTool

# Define agents with tools
front_end_developer = Agent(
    role="Front-End Developer",
    goal="Create responsive and user-friendly interfaces",
    backstory="You specialize in HTML, CSS, and JavaScript, bringing designs to life.",
    tools=[SeleniumScrapingTool(), WebsiteSearchTool()]
)

back_end_developer = Agent(
    role="Back-End Developer",
    goal="Implement server-side logic and manage databases",
    backstory="You excel in server-side languages and database management.",
    tools=[GithubSearchTool(), JSONSearchTool(), PGSearchTool()]
)

full_stack_developer = Agent(
    role="Full-Stack Developer",
    goal="Integrate front-end and back-end components",
    backstory="You have expertise in both front-end and back-end technologies.",
    tools=[SeleniumScrapingTool(), GithubSearchTool()]
)

devops_engineer = Agent(
    role="DevOps Engineer",
    goal="Manage infrastructure and optimize deployments",
    backstory="You ensure smooth and efficient deployment processes.",
    tools=[GithubSearchTool(), DirectorySearchTool()]
)

qa_engineer = Agent(
    role="QA Engineer",
    goal="Ensure code quality and perform thorough testing",
    backstory="You are meticulous in identifying and fixing bugs.",
    tools=[SeleniumScrapingTool(), TXTSearchTool()]
)

# Define tasks
develop_front_end = Task(
    description="Create responsive and user-friendly interfaces.",
    expected_output="A fully functional front-end interface."
)

develop_back_end = Task(
    description="Implement server-side logic and database interactions.",
    expected_output="A fully functional back-end system."
)

full_stack_development = Task(
    description="Integrate front-end and back-end components.",
    expected_output="A seamlessly integrated application."
)

optimize_and_repair = Task(
    description="Analyze and improve existing applications.",
    expected_output="Optimized and repaired applications."
)

testing_and_qa = Task(
    description="Perform thorough testing and debugging.",
    expected_output="A bug-free, high-quality application."
)

# Create crew
crew = Crew(
    agents=[front_end_developer, back_end_developer, full_stack_developer, devops_engineer, qa_engineer],
    tasks=[develop_front_end, develop_back_end, full_stack_development, optimize_and_repair, testing_and_qa],
    process=Process.sequential
)

# Kickoff the crew
result = crew.kickoff()
print(result)
