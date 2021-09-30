from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/name', methods=['GET'])
def ejemplo(name):
    return f"Hola, {name}"

@app.route('/palindromo/<palabra>', methods=['GET'])
def ejercicio1(palabra):
    # Su código va aquí

    n = len(palabra)
    i = 0
    es_palindromo = False

    while i < n :
        if palabra[i] == palabra[-i-1]:
            es_palindromo = True
            break
        i += 1

    if es_palindromo:
        return "Es palindromo"
    else:
        return "No es palindromo"

@app.route('/operaciones/<num1>/<num2>', methods=['GET'])
def ejercicio2(num1, num2):
    # Su código va aquí
    n1 = int(num1)
    n2 = int(num2)
    suma = n1 + n2
    if n1 > n2 :
        resta = n1 - n2
    else:
        resta = n2 - n1
    product = n1 * n2
    division = n1 // n2
    return str(suma) + str(resta) + str(product) + str(division)

@app.route('/ordenar/<a>/<b>/<c>', methods=['GET'])
def ejercicio3(a, b, c):
    # Su código va aquí
    
    num = [a, b, c]
    z = num.sort()
    return z[1:-1]


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
