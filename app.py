from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return render_template('index.html')

@app.route("/base", methods=["GET"])
def base():
    return render_template('base.html')

@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
