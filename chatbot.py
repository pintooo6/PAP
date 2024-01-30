import requests

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    # Conecte-se à API RESTful
    response = requests.get("http://10.64.130.114:5000/api/get_answer", params={"question": question})

    # Retorne a resposta da API RESTful
    if response.status_code == 200:
        return response.text
    else:
        return None
