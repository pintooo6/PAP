import json
from difflib import get_close_matches

#Carregar o ficheiro de conhecimento base 

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=2)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    # Corrected code to break out of the loop when `quit` is entered
    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        


def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')
    
    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break

        best_match = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']])  # Change to use multiple matches

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)  # Added this line
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base['questions'].append({'question': user_input, 'answer': new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you man!')


if __name__ == '__main__':
    chat_bot()

