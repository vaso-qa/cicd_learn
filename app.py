from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'секретный_ключ'  # Необходимо для работы flash-сообщений

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:  # Проверяем, что поля заполнены
            flash('Регистрация прошла успешно!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Пожалуйста, заполните все поля.', 'error')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Слушаем на всех интерфейсах
