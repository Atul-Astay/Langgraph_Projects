# app.py

from graph import graph


def main():

    print("=" * 60)
    print("📄 AI Resume Reviewer")
    print("=" * 60)

    print("\nPaste your resume below.")
    print("Press Enter twice to finish.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    resume = "\n".join(lines)

    result = graph.invoke(
        {
            "resume": resume,
            "ats_score": 0,
            "feedback": "",
            "improved_resume": "",
            "decision": "",
            "iteration": 0
        }
    )

    print("\n")
    print("=" * 60)
    print("FINAL ATS SCORE")
    print("=" * 60)

    print(result["ats_score"])

    print("\n")
    print("=" * 60)
    print("FEEDBACK")
    print("=" * 60)

    print(result["feedback"])

    print("\n")
    print("=" * 60)
    print("IMPROVED RESUME")
    print("=" * 60)

    print(result["resume"])

    print("\nIterations :", result["iteration"])


if __name__ == "__main__":
    main()