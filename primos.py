import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')
def nao_entre_em_panico():


    limite = 100
    qtdPrimos = 2
    numero = 3

    primos = "1,2,"

    while qtdPrimos < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            qtdPrimos += 1
            if (qtdPrimos % 10 == 0):
                primos = primos + " -> " + str(qtdPrimos) + "<br>"
        numero += 1


    return primos

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
