import json
from difflib import get_close_matches
from google.cloud import search
from google.cloud import os
 

# Load the knowledge base file

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

    # Use Google Search API to answer coding questions
    if question.startswith('how to'):
        client = search.SearchServiceClient()

        search_params = search.SearchParams()
        search_params.query = question
        search_params.location = "US"
        search_params.language = "en"

        search_response = client.search(request=search_params)

        for result in search_response.results:
            if result.doc_id == "codingpedia/python-for-beginners/functions-in-python":
                answer_text = result.snippet
                break

        # Return the extracted answer from Google Search
        return answer_text 

    # Corrected code to break out of the loop when `quit` is entered
    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        

def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    from google.cloud import search
     
    from googlesearch import search
    search("foo") 
     # Replace with your actual API key
    os.environ["SEARCH_API_KEY"] = "AIzaSyCO-JfMMXxTdlDbzZGfGh1ynE1sjY7ApN0"
    
    # Initialize the SearchServiceClient object
    client = search.SearchServiceClient()
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
