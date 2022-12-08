from process import preparation, generate_response
from flask import Flask, render_template, request
from model import load, prediksi

#Start Chatbot
app = Flask(__name__)

# download nltk
preparation()

# load model ds
load()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predik")
def predik():
    return render_template("predik.html")

@app.route("/predict", methods=["GET","POST"])
def predict():
    harga_open = int(request.form['harga_open'])
    harga_close = int(request.form['harga_close'])
    
    # data = [[harga_open, harga_close]]
    hasil = prediksi(harga_open, harga_close)
    return render_template("predik.html", hasil_prediksi = hasil )

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)