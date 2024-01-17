from flask import Flask, request
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/api/get_answer", methods=["GET"])
def get_answer():
    question = request.args.get("question")

    # Conecte-se à base de dados
    engine = create_engine("mysql://root:pap@10.64.130.114/pap")
    connection = engine.connect()

    # Retorne a resposta da base de dados
    query = """
        SELECT answer
        FROM questions
        WHERE question = :question
    """
    answer = connection.execute(query, question=question).fetchone()[0]
    connection.close()

    return answer

if __name__ == "__main__":
    app.run()
