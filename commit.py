import os
import sys


def commit_formatter(commit: str):
    if commit.startswith("-t "):
        commit = commit.replace("-t ", "TEST: ")
        commit += "🧪"
    elif commit.startswith("-c "):
        commit = commit.replace("-c ", "CODE: ")
        commit += "💻"
    elif commit.startswith("-d "):
        commit = commit.replace("-d ", "DOCUMENTATION: ")
        commit += "📄"
    else:
        pass
    return commit


if __name__ == "__main__":
    # run black from here to avoid weird errors
    os.system("black . --line-length=100")

    if len(sys.argv) > 1:
        os.system("git add .")
        print("staging all files ... 🐍")
        os.system(f'git commit -m "{commit_formatter(sys.argv[1])}"')
        print(f'commit "{commit_formatter(sys.argv[1])}"')
        os.system("git push")
    else:
        os.system("git add .")
        print("staging all files ... 🐍")
        os.system(f'git commit -m "make it better"')
        os.system("git push")
