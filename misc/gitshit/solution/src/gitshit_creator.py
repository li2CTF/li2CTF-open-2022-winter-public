import git
from random import randint, choice
from re import match
from string import ascii_letters, digits
from time import sleep

alphabet = ascii_letters + digits + "!_-+"
flag_base = "li2CTF{%s}"
correct_flag_payload = "eb4be8ca3fdeaf33b37f7a6f27b02494"
correct_flag_payload_regex = r"[a-z0-9]{32}"
correct_flag_index = randint(0, 99)

print("[.] Correct commit index:", correct_flag_index)

task_repo = git.Repo.init("flag-holder")

for i in range(100):
    if i == correct_flag_index:
        flag_payload = correct_flag_payload
    else:
        while True:
            flag_payload = "".join([choice(alphabet) for _ in range(randint(28, 34))])
            if not match(correct_flag_payload_regex, flag_payload):
                break
    flag = flag_base % flag_payload
    with open("flag-holder/flag.txt", "w") as f:
        f.write(flag)
    task_repo.index.add(['flag.txt'])
    commit = task_repo.index.commit('lololo')
    if i == correct_flag_index:
        print("[.] Correct commit hash:", commit.hexsha)
    sleep(0.1)
print("[*] Done")
