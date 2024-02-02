from answer import answer_question, df
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user_question = request.form["question"]
        response = answer_question(df, question=user_question, debug=False)
        return redirect(url_for("index", result=response))  

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
