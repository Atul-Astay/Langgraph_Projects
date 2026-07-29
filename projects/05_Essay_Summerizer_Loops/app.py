# app.py

from graph import graph


def get_essay():

    print("\nPaste your essay below.")
    print("Press Enter twice to finish.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    return "\n".join(lines)


def main():

    print("=" * 60)
    print("📝 AI Essay Improver")
    print("=" * 60)

    while True:

        essay = get_essay()

        if essay.lower() == "exit":
            break

        result = graph.invoke(
            {
                "essay": essay,
                "feedback": "",
                "improved_essay": "",
                "decision": "",
                "iteration": 0
            }
        )

        print("\n")
        print("=" * 70)
        print("FINAL ESSAY")
        print("=" * 70)
        print(result["essay"])

        print("\n")
        print("=" * 70)
        print("FINAL FEEDBACK")
        print("=" * 70)
        print(result["feedback"])

        print("\nIterations :", result["iteration"])
        print("=" * 70)


if __name__ == "__main__":
    main()