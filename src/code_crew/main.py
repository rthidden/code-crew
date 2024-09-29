from code_crew.crew import create_crew, save_app

def main():
    crew = create_crew()
    result = crew.kickoff()
    print("Crew work result:", result)
    
    # Assuming the last task's result contains the app content
    app_content = crew.tasks[-1].output
    save_app(app_content)

if __name__ == "__main__":
    main()
