from flask import Flask
app = Flask(__name__) 

@app.route("/")
def decorator():
    return"Qualquer coisa"

@app.route("/ok")
def decorator1():
    return"Outra coisa"

if __name__ == "__main__" :
    app.run(debug=True)