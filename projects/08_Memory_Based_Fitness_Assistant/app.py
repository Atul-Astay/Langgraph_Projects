# app.py

from langchain_core.messages import HumanMessage

from graph import graph


def chat():

    print("=" * 60)
    print("🏋️ AI Fitness Coach")
    print("=" * 60)

    print("\nType 'exit' anytime to quit.\n")

    # Each thread_id represents one user's conversation
    thread_id = input("Enter Session ID: ").strip()

    if not thread_id:
        thread_id = "default_user"

    print(f"\nSession Started: {thread_id}")

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("\n👋 Thank you for using AI Fitness Coach!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            },
            config={
                "configurable": {
                    "thread_id": thread_id
                }
            }
        )

        ai_response = result["messages"][-1].content

        print("\n🏋️ Fitness Coach:")
        print(ai_response)


if __name__ == "__main__":
    chat()