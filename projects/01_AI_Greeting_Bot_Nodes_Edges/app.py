from graph import graph


def main():

    print("=" * 50)
    print("🤖 AI Greeting Bot")
    print("=" * 50)

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye 👋")
            break

        result = graph.invoke(
            {
                "user_input": user_input
            }
        )

        print("\nBot:", result["response"])


if __name__ == "__main__":
    main()