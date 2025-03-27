from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/soma/<num1>/<num2>')
def soma(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'A soma de {num1} + {num2} =  {num1 + num2}'
    except TypeError:
        return "Digite apenas números"
    except ValueError:
        return f"Digite apenas números"

@app.route('/subtracao/<num1>/<num2>')
def subtracao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'A subtração de {num1} - {num2} =  {num1 - num2}'
    except TypeError:
        print("Digite apenas números")
    except ValueError:
        return f"Digite apenas números"

@app.route('/multiplicacao/<num1>/<num2>')
def multiplicaco(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'A multiplicação de {num1} * {num2} =  {num1 * num2}'
    except TypeError:
        print("Digite apenas números")
    except ValueError:
        return f"Digite apenas números"

@app.route('/divisao/<num1>/<num2>')
def divisao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'A divisão de {num1} / {num2} =  {num1 / num2}'
    except TypeError:
        print("Digite apenas números")
    except ValueError:
        print("Digite apenas números")
    except ZeroDivisionError:
        print("Não ha divisão por 0")

@app.route('/par-impar/<num>')
def valor(num):
    num = int(num)
    try:
        if num % 2 == 0:
            return f'O número é par'
        else:
            return f'O número é impar'
    except TypeError:
        print("Digite apenas números")
    except ValueError:
        return f"Digite apenas números"


if __name__ == '__main__':
    app.run(debug=True)