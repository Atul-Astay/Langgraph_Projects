from graph import graph


def main():

    print("=" * 60)
    print("📧 AI Email Classifier")
    print("=" * 60)

    while True:

        email = input("\nPaste Email (or type 'exit'): ")

        if email.lower() == "exit":
            break

        result = graph.invoke(
            {
                "email": email
            }
        )

        print("\nCategory :", result["category"].title())
        print("\nRecommendation:\n")
        print(result["response"])


if __name__ == "__main__":
    main()