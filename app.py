from flask import Flask, render_template, request, jsonify
from flipkart.retrieval_generation import generation
from flipkart.data_ingestion import data_ingestion
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY not found in .env file. Please set it.")
os.environ["GROQ_API_KEY"] = api_key

# Initialize vector store and conversational chain
vstore = data_ingestion("done")
chain = generation(vstore)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    try:
        # Expect JSON data from AJAX
        data = request.get_json()
        if not data or "msg" not in data:
            return jsonify({"error": "No message provided"}), 400
        
        msg = data["msg"]
        input_data = {"input": msg}
        result = chain.invoke(
            input_data,
            config={"configurable": {"session_id": "dhruv"}}
        )["answer"]

        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)