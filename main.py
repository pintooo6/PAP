import json
from difflib import get_close_matches

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

//adicionar logica para responder a pergunta Que curos engressar?
def answer_what_course_to_enroll(question):
  """Responde à pergunta "Em que curso devo engressar?".

  Args:
    question: A pergunta do usuário.

  Returns:
    Uma resposta à pergunta.
  """

  response = "A escolha do curso regular ou profissional de ensino secundário é uma decisão importante que deve ser tomada com cuidado. Depende muito dos seus gostos e do caminho profissional que você quer seguir."

  courses = [
      {
        "name": "Técnico de Gestão e Programação de Sistemas Informatícos",
        "description": "Este curso prepara os alunos para trabalharem com computadores e tecnologia de informação.",
      },
      {
        "name": "Técnico de Eletromecánica",
        "description": "Este curso prepara os alunos para trabalharem com sistemas eletrônicos.",
      },
      {
        "name": "Técnico de Mecatrónica",
        "description": "Este curso prepara os alunos para trabalharem com máquinas e equipamentos mecânicos.",
      },
      {
        "name": "Curso de Ciências e Tecnologias",
        "description": "Este curso prepara os alunos para seguir carreiras nas áreas de ciências, matemática e tecnologia.",
      },
      {
        "name": "Curso de Línguas e Humanidades",
        "description": "Este curso prepara os alunos para seguir carreiras nas áreas de línguas, literatura, história e filosofia.",
      },
      {
        "name": "Curso de Artes Visuais e Design",
        "description": "Este curso prepara os alunos para seguir carreiras nas áreas de artes visuais, design e comunicação.",
      },
  ]

  for course in courses:
    response += f"* **{course['name']}:** {course['description']}"

  return response

//Fim da classe


def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break

        # Check if the user's input is a coding-related question
        best_match = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']])
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
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
