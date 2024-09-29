import yaml
from crewai import Agent

def load_agents(llm):
    with open('src/code_crew/config/agents.yaml', 'r') as file:
        agents_config = yaml.safe_load(file)
    
    agents = []
    for agent_config in agents_config:
        agent = Agent(
            name=agent_config['name'],
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            llm=llm
        )
        agents.append(agent)
    
    return agents

def load_tasks(agents):
    with open('src/code_crew/config/tasks.yaml', 'r') as file:
        tasks_config = yaml.safe_load(file)
    
    # Implementation for loading tasks remains the same
    # ...
