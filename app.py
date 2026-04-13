from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    tarefa = request.form["tarefa"]
    tarefas.append(tarefa)
    return redirect("/")

@app.route("/remover/<int:numero>")
def remover(numero):
    tarefas.pop(numero)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)