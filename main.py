questions = [
    ("Вопрос 1: В фильме человек паук через вселеную был танос?", "да"),
    ("Вопрос 2: Ты рисовал хуй на машине максима?", "да"),
    ("Вопрос 3: Чемпион по ждек-боксу Вова ?", "да"),
    ("Вопрос 4: Я ЧЕМПИОН ПО ПОКЕРУ ?", "да"),
    ("Вопрос 5: максим чурка?", "нет"),
    ("Вопрос 6: Вы уверены в прошлом ответе ", "да"),
    ("Вопрос 7: лабанова обезьяна ?", "да"),
    ("Вопрос 8: тебе вьебать", "нет"),
    ("Вопрос 9: Вы знаете песнь егора Шипа", "да"),
    ("Вопрос 10: концерт кишлака тут ?", "да")
]

stroka = 0
for i, (question, pravelinei) in enumerate(questions, start=1):
    print(f"Вопрос {i}: {question}")
    user_answer = input("Ваш ответ (да/нет): ").lower()
    if user_answer == pravelinei:
        print("Правильно!")
        stroka += 1
    else:
        print("Неправильно!")

print(f"Выtest-py набрали {stroka} из {len(questions)} возможных баллов.")