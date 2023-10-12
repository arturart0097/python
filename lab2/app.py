from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')

        if num1 and num2 and operation:
            try:
                num1 = float(num1)
                num2 = float(num2)

                if operation == 'add':
                    result = num1 + num2
                elif operation == 'subtract':
                    result = num1 - num2
                elif operation == 'multiply':
                    result = num1 * num2
                elif operation == 'divide':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Помилка: ділення на нуль"
                else:
                    result = "Невідома операція"
            except ValueError:
                result = "Помилка: некоректні дані"

    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
