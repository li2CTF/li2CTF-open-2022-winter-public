import git
from re import match

flag_regex = r"li2CTF{[a-f0-9]{32}}"

task_repo = git.Repo("src/flag-holder")

print(f"[.] Checking commit with hash {'a' * 32}", end="\r", flush=True)

head_commit = task_repo.head.commit.hexsha

for commit in list(task_repo.iter_commits("master")):
    commit_hash = commit.hexsha
    print(f"[.] Checking commit with hash {commit_hash}", end="\r", flush=True)
    task_repo.git.checkout(commit_hash)
    with open("src/flag-holder/flag.txt", "r") as f:
        data = f.read()
    
    if match(flag_regex, data):
        print(f"[!] Correct commit hash: {commit_hash}" + " " * 40)
        print(f"[!] Flag found: {data}" + " " * 40)
        break

task_repo.git.checkout(head_commit)
