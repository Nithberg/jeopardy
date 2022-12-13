from settings import get_questions_from_json, show_game_menu, parse_input, get_question


def main():
    data_questions = get_questions_from_json()
    while True:

        show_game_menu(data_questions)
        user_input = parse_input(input('Введите категорию и цену через пробел: '))
        category, price = user_input["category"], user_input["price"]
        question = data_questions[category][price]
        get_question(question["question"])
        answer_to_question = input("Введите ответ на вопрос: ").lower()
        if answer_to_question == question["answer"]:
            print(f"Верно! Слово {question['question']} переводится  - {question['answer']}")
        else:
            print(f"Не верно! Слово {question['question']} переводится  - {question['answer']}")

        question["asked"] = True


main()
