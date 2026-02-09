from agents.router import AgentRouter

def main():
    print("\n=== OFFLINE AGENTIC AI FRAMEWORK ===")
    print("Type 'exit' to quit\n")

    agent = AgentRouter()

    while True:
        user_input = input("You > ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Agentic AI. Goodbye!")
            break

        response = agent.respond(user_input)
        print("\nAgent >")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()
