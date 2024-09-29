import os
from crewai import Crew, Process, AnthropicAI
from code_crew.config.config_loader import load_agents, load_tasks

def create_crew():
    anthropic_ai = AnthropicAI(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    agents = load_agents(anthropic_ai)
    tasks = load_tasks(agents)
    
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        manager_llm=anthropic_ai
    )
    return crew

def save_app(app_content):
    app_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'app')
    os.makedirs(app_dir, exist_ok=True)
    with open(os.path.join(app_dir, 'app.py'), 'w') as f:
        f.write(app_content)
    print(f"App saved to {os.path.abspath(os.path.join(app_dir, 'app.py'))}")
