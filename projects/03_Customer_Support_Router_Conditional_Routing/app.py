# app.py

from graph import graph


def main():
    print("=" * 60)
    print("🤖 AI Customer Support Router")
    print("=" * 60)
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("You: ").strip()

        if query.lower() in ["exit", "quit"]:
            print("\nThank you for using Customer Support. Goodbye! 👋")
            break

        if not query:
            print("Please enter your question.\n")
            continue

        # Initial state
        state = {
            "query": query
        }

        # Execute the LangGraph
        result = graph.invoke(state)

        print("\n" + "-" * 60)
        print(f"Detected Intent : {result['intent'].title()}")
        print("-" * 60)
        print(result["response"])
        print("-" * 60 + "\n")


if __name__ == "__main__":
    main()