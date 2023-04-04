
from send_mail import yag_mail
from flask import Flask, render_template, request
from chatgpt import Chatbot

app = Flask(__name__)
chat = ""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        result = {}

        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['message'] = request.form['message']

        yag_mail(result)

        return render_template('thank-you.html', **locals())

    return render_template("index.html")


@app.route("/chatGPT", methods=('GET', 'POST'))
def chatGPT():
    global chat
    if request.method == 'POST':
        q = request.form['question']
        chatbot = Chatbot()
        response = chatbot.get_response(q)
        chat = f"{chat}\nYou: {q}  \nChatbot: {response}\n"
    return render_template("chatGPT.html", chat=chat)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

