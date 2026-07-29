# app.py

from langchain_core.messages import HumanMessage

from graph import graph


def chat():

    print("=" * 60)
    print("🛒 AI Shopping Assistant")
    print("=" * 60)

    print("\nType 'exit' to quit.\n")

    # One thread = One conversation memory
    thread_id = input("Enter Session ID: ").strip()

    while True:

        user_input = input("\nYou : ")

        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Invoke LangGraph
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

        print("\nAssistant :")
        print(result["messages"][-1].content)


if __name__ == "__main__":
    chat()