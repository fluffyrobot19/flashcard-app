import random
from openai import OpenAI
from openai_api_key import openai_api_key

username = input("What's your name?\n")

print(f"\nHello {username}!\nWelcome to the Codecool-Module-Workbooks-Flashcard application!.")

wbs_choice = input("\nPlease choose from the following module options:\n(a) Progbasics\n(b) Web\n(c) OOP (C#)\n(d) All of the above.\n")

progbasics_wb = "module_progbasics.md"
web_wb = "module_web.md"
oop_wb = "module_oop_csharp.md"

file = open(progbasics_wb if wbs_choice == "a" else web_wb if wbs_choice == "b" else oop_wb, "r")

questions = []

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

no_of_qs = input(f"\nYour choice means a total of {str(len(questions))} questions.\nPlease write a smaller number below, if you want to answer fewer questions than that. Otherwise leave blank and press enter.\n")

remaining_qs = 0

if no_of_qs == "":
    remaining_qs = len(questions)
else:
    remaining_qs = int(no_of_qs)

while remaining_qs > 0:
    random_q = random.choice(questions)
    print("          **********************************************")
    response = input(f"\n\033[3m          {random_q}\033[0m\n          **********************************************\n")
    if response == "":
      check_answer = input("Do you want to check the answer from OpenAI? y/n\n")
      if check_answer == "y":
        client = OpenAI(api_key=openai_api_key)

        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "user", "content": "Can you please respond to this question in only one or maximum 2 sentence? Here is the question: " + random_q}
          ]
        )

        print(f"\n          {response.choices[0].message.content}")
        questions.remove(random_q)
        remaining_qs -= 1
        cont = input("\nPlease press enter to continue to next question.")
        if cont == "":
            continue
    questions.remove(random_q)
    remaining_qs -= 1



