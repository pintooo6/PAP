import requests
import json
import nltk
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

def enviar_pergunta_para_api(pergunta):
    # Endereço IP e porta do servidor DANI
    endereco_ip = "10.64.130.25"
    porta = 8000  

    # URL para ter acesso a api do dani
    url = f"http://{endereco_ip}:{porta}/api/get_answer"

    # Parâmetros da requisição pergunta
    parametros = {"question": pergunta}

    # Envia a pergunta para a API do dani
    resposta = requests.get(url, params=parametros)

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        # Retorna a resposta da API
        return resposta.json()["answer"]
    else:
        # Em caso de erro, retorna uma mensagem de erro
        return "Erro ao enviar pergunta para a API"

def chat_bot():
    # Download NLTK biblioteca
    nltk.download('punkt')

    # carregar base de conhecimento
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break

        # Tokenize a entrada do usuário
        user_tokens = nltk.word_tokenize(user_input)

        # Processamento da pergunta do utilizador a usar a api do dani
        resposta = enviar_pergunta_para_api(user_input)
        print(f"Bot (via API): {resposta}")

if __name__ == '__main__':
    chat_bot()
