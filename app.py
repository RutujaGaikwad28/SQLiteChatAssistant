from flask import Flask, request, render_template
from chat_logic import process_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_query = request.form["query"]
        response = process_query(user_query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production