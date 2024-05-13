"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.  As perguntas são:
a.	 “Telefonou para a vítima?”
b.	 “Esteve no local do crime?”
c.	 “Mora perto da vítima?”
d.	 “Devia para a vítima?”
e.	 “Já trabalhou com a vítima?”
O programa deve no final, emitir uma classificação para o interrogado.
2 respostas positivas – Suspeito(a)
3 e 4 respostas positivas – Cúmplice
5 respostas positivas – Assassino.
"""

count = 0
message = """
CRIME SCENE
Foi encontrado um corpo do sujeito fulano de tal na Vovocita maluca doida. 
Investigador chegou no local e começou a questionar as pessoas da rua. 
Responda as questões
"""
print(message)

question1 = input("1. Telefonou para a vítima? ")
question2 = input("2. Esteve no local do crime? ")
question3 = input("3. Mora perto da vítima? ")
question4 = input("4. Devia para a vítima? ")
question5 = input("5. Já trabalhou com a vítima? ")

questions = [question1, question2, question3, question4, question5]

for i in range (0, len(questions), 1):
    if questions[i].lower() == "s":
        count += 1
    
# for question in questions:
#     if question.lower() == "s":
#         count += 1

# Contagem
if count == 2:
    print("Suspeito(a).")
elif count >= 3 and count < 5:
    print("Cúmplice.")
else:
    print("Assassino.")


""" 
Assassinato de if else statements

if question1.lower() == "s":
    count += 1
if question2 == "s":
    count += 1
if question3.lower() == "s":
    count += 1
if question4.lower() == "s":
    count += 1
if question5.lower() == "s":
    count += 1
"""
