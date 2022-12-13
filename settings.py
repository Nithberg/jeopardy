import json


def get_questions_from_json():
    with open("questions.json", "r") as file:
        get_data_questions = json.load(file)
    return get_data_questions


def show_game_menu(use_data_questions):
    for category_question, category_price in use_data_questions.items():
        print(category_question.ljust(12), end=" ")
        for price, asked in category_price.items():
            if not asked["asked"]:
                print(price.ljust(5), end=" ")
            else:
                print("   ".ljust(5), end=" ")
        print()
        print()


def parse_input(user_answer):
    user_answer = user_answer.split(" ")
    return {"category": user_answer[0], "price": user_answer[1]}


def get_question(question):
    print(f'Слово {question} в переводе означает ...')



