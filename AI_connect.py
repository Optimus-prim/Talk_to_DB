import os
from pymongo import MongoClient
from ollama import Client

# MongoDB setup
mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["Sample_Purchaces"]
collection = db["User_sales"]

# Ollama client (local LLM)
ollama_client = Client(host='http://localhost:11434')

# Schema context
schema_hint = """
You are working with the 'User_sales' collection which has the following structure:

- _id (string): Unique order ID 
- customer (object):
    - name (string): Customer full name
    - email (string): Customer email address
    - address (object):
        - street (string): Street address
        - city (string): City name
- order_date (string): Date of the order in ISO format
- total_price (float): Total amount of the order
- items (array of objects): List of products in the order, each with:
    - product_name (string)
    - quantity (int)
    - price (float)
"""

def generate_mongo_query(user_question):
    full_prompt = f"""{schema_hint}

Translate the following natcreate gitural language request into a valid **Python expression** using PyMongo and the variable `collection`.

Very Important:
- Only return a **single Python expression**.
- Do NOT use print(), for-loops, or list comprehensions.
- Do NOT include any explanations or markdown formatting.
- The result should be directly assignable like: results = <expression>

User input:
"{user_question}"
"""
    response = ollama_client.chat(
        model='mistral',
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response['message']['content'].strip()


def run_query(mongo_code_str):
    try:
        code = mongo_code_str.replace("```python", "").replace("```", "").strip()

        # Force fallback for distinct error pattern
        if "for" in code and "distinct" in code:
            return collection.distinct("_id")

        if code.startswith("for ") or "print(" in code:
            exec(code)
            return None
        else:
            exec(f"results = {code}", globals())
            return results
    except Exception as e:
        return f"Error executing query: {str(e)}"


if __name__ == "__main__":
    user_question = input("Ask your MongoDB question: ")
    mongo_query_code = generate_mongo_query(user_question)
    print("\n Generated MongoDB Query:\n", mongo_query_code)

    print("\n Running the query...\n")
    result = run_query(mongo_query_code)
    if isinstance(result, str):
        print(result)
    elif result:
        for doc in result:
            print(doc)
    else:
        print(" Query ran, but no results were returned.")
