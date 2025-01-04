from agent_manager import AgentManager
from assignment import Assignment, Task

def main():
    # Define tasks for the assignment
    tasks = [
        Task(name="Research Topic", description="Research the given topic and gather information."),
        Task(name="Write Report", description="Write a detailed report based on the research."),
        Task(name="Create Presentation", description="Create a presentation summarizing the report.")
    ]

    # Create an assignment
    assignment = Assignment(name="Complete Project", tasks=tasks)

    # Initialize the AgentManager
    agent_manager = AgentManager()

    # Execute the assignment
    agent_manager.execute_assignment(assignment)

if __name__ == "__main__":
    main()