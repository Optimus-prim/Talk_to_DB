import os
from pymongo import MongoClient
from ollama import Client

# MongoDB setup
mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["your_db_name"]  # Replace with your DB
collection = db["transactions"]

# Ollama client (local LLM)
ollama_client = Client(host='http://localhost:11434')  # default Ollama port

# Example schema context
schema_hint = """
You are working with the 'transactions' collection which has fields:
- user_id (string)
- transaction_date (ISODate)
- amount (float)
"""

# Function to generate MongoDB query from NL
def generate_mongo_query(user_question):
    full_prompt = f"""{schema_hint}
Translate the following natural language request into a Python MongoDB query using the `collection` variable:
The collection is already defined as: collection = db["transactions"]
Only return the Python code using that variable.
"{user_question}"
Only output the Python MongoDB query, no explanation.
"""
    response = ollama_client.chat(model='mistral', messages=[{"role": "user", "content": full_prompt}])
    return response['message']['content'].strip()

# Run the generated MongoDB query
def run_query(mongo_code_str):
    try:
        # Clean up markdown artifacts like ```python and ```
        clean_code = (
            mongo_code_str.replace("```python", "")
                          .replace("```", "")
                          .strip()
        )
        exec(f"results = {clean_code}", globals())
        return results
    except Exception as e:
        return f"Error executing query: {str(e)}"


# Main loop
if __name__ == "__main__":
    user_question = input("Ask your MongoDB question: ")
    mongo_query_code = generate_mongo_query(user_question)
    print("\n🔎 Generated MongoDB Query:\n", mongo_query_code)

    print("\n📊 Running the query...\n")
    result = run_query(mongo_query_code)
    if isinstance(result, str):
        print(result)
    else:
        for doc in result:
            print(doc)
