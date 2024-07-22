from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Code_Crew():
	"""Code Crew: A crew of developers working together to build amazing applications."""

	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"

	# Define agents
	@agent
	def front_end_developer(self) -> Agent:
		return Agent(
			config=self.agents_config["front_end_developer"],
			tools=[],
			verbose=True    
		)

	@agent
	def back_end_developer(self) -> Agent:
		return Agent(
			config=self.agents_config["back_end_developer"],
			tools=[],
			verbose=True,    
		)
		
	def full_stack_developer(self) -> Agent:
		return Agent(
			config=self.agents_config["full_stack_developer"],
			tools=[],
			verbose=True,    
		)
		
	def devops_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config["devops_engineer"],
			tools=[],
			verbose=True,    
		)
		
	def qa_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config["qa_engineer"],
			tools=[],
			verbose=True,
			output=(
				# Print Results
				print('\n\n############################'),
				print('## Here is your app'),
				print('Enjoy!'),
				print(Code_Crew),   
		)		
		)
	# Define tasks
	@task
	def develop_front_end(self) -> Task:
		return Task(
			config=self.tasks_config["develop_front_end"],
			agent=self.front_end_developer()
			)

	@task
	def develop_back_end(self) -> Task:
		return Task(
			config=self.tasks_config["develop_back_end"],
			agent=self.back_end_developer()
			)
		

	@task
	def full_stack_development(self) -> Task:
		return Task(
			config=self.tasks_config["full_stack_development"],
			agent=self.full_stack_developer()
			)
		

	@task
	def optimize_and_repair(self) -> Task:
		return Task(
			config=self.tasks_config["optimize_and_repair"],
			agent=self.devops_engineer()
			)
		
	@task
	def testing_and_qa(self) -> Task:
		return Task(
			config=self.tasks_config["testing_and_qa"],
			agent=self.qa_engineer()
			)
		

	# Create crew
	@crew
	def crew(self) -> Crew:
		"""Creates the Code Crew."""
		return Crew(
		agents=self.agents,
		tasks=self.tasks,
		process=Process.sequential,
		verbose=2
	)

# code_crew = crew.kickoff()


