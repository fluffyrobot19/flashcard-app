import random

username = input("What is your name?\n")

print("\nHello " + username + "!\nWelcome to the Codecool module workbooks flashcard application.")

wbs_choice = input("\nPlease choose from the following module options:\n(a) Progbasics\n(b) Web\n(c) OOP\n(d) All of the above.")

# read questions
questions = []

oop_wb = "module_oop_csharp.md"
file = open(oop_wb, "r")

if file.readable():
    while True:
        line = file.readline()
        if line.startswith("#### "):
            question = line.strip("#### ")
            questions.append(question)
        if line == "END OF FILE":
            break
else:
    print("file unreadable")

file.close()

no_of_qs = input("Your choice means a total of" + str(len(questions)) + "questions. Please write a smaller number below, if you want to answer fewer questions than that. Otherwise leave blank and press ENTER.")

remaining_qs = 0


if no_of_qs == "":
    remaining_qs = len(questions)
else:
    remaining_qs = int(no_of_qs)

while remaining_qs > 0:
    random_q = random.choice(questions)
    input("\n" + random_q + "\n")
    questions.remove(random_q)
    remaining_qs -= 1

