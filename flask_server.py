from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import requests 

app = Flask(__name__)

# Configuração da string de conexão com a base de dados do dani
DB_USER = "root"
DB_PASSWORD = "pap"
DB_HOST = "10.64.130.25"
DB_NAME = "pap"

# String de conexão completa
DB_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# Cria  a engine de conexão com a base de dados
engine = create_engine(DB_URI)

@app.route("/api/get_answer", methods=["GET"])
def get_answer():
    question = request.args.get("question")

    # Conectando-se a base de dados
    connection = engine.connect()

    # Consulta SQL para buscar a resposta com base na pergunta
    query = """
        SELECT c.text AS answer
        FROM chats c
        JOIN conversas cv ON c.conver_id = cv.id
        WHERE cv.title = :question
        ORDER BY c.data DESC
        LIMIT 1
    """
    
    # Executando a consulta SQL
    result = connection.execute(query, question=question)
    
    # Obtendo a resposta da consulta
    answer = result.fetchone()

    # Fechando a conexão com o banco de dados
    connection.close()

    # Verificando se a resposta existe
    if answer:
        return jsonify({'answer': answer[0]})
    else:
        return jsonify({'answer': 'Não foi encontrada uma resposta para esta pergunta.'})

def enviar_pergunta(pergunta):
    url = "http://10.64.130.25:8000/api/get_answer"  # Substitua localhost:5000 p   ela URL do seu servidor Flask
    parametros = {"question": pergunta}
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        return resposta.json()['answer']
    else:
        return "Erro ao obter resposta da API"

if __name__ == "__main__":
    app.run(debug=True)
