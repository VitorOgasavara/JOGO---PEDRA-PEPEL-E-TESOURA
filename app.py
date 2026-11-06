from flask import Flask, render_template, request
import random

app = Flask(__name__)

resultado_maquina = 0
resultado_jogador = 0


@app.route("/", methods=["GET", "POST"])
def index():
    global resultado_maquina, resultado_jogador

    mensagem = ""

    if request.method == "POST":
        jogador = request.form["jogada"]

        nomes = ["pedra", "papel", "tesoura"]
        computador = random.choice(nomes)

        if jogador == computador:
            mensagem = "Empate!"

        elif (
            (jogador == "pedra" and computador == "tesoura")
            or (jogador == "papel" and computador == "pedra")
            or (jogador == "tesoura" and computador == "papel")
        ):
            resultado_jogador += 1
            mensagem = "Você ganhou!"

        else:
            resultado_maquina += 1
            mensagem = "Computador ganhou!"

        if resultado_jogador == 5:
            mensagem = "JOGADOR CAMPEÃO!"
            resultado_jogador = 0
            resultado_maquina = 0

        elif resultado_maquina == 5:
            mensagem = "COMPUTADOR CAMPEÃO!"
            resultado_jogador = 0
            resultado_maquina = 0

        return render_template(
            "index.html",
            mensagem=mensagem,
            computador=computador,
            jogador=jogador,
            resultado_jogador=resultado_jogador,
            resultado_maquina=resultado_maquina
        )

    return render_template(
        "index.html",
        mensagem="",
        resultado_jogador=resultado_jogador,
        resultado_maquina=resultado_maquina
    )


if __name__ == "__main__":
    app.run(debug=True)