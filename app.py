from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/contactos")
def contactos():
    return render_template("contactos.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

if __name__=="__main__":
    app.run(debug=True)
