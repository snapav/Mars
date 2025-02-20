from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Миссия Колонизация Марса </h1>'


@app.route('/index')
def about():
    return '<h1> И на Марсе будут яблони цвести! </h1>'


@app.route('/promotion')
def promotion():
    return '''<h1>Человечество вырастает из детства. <br>
Человечеству мала одна планета. <br>
Мы сделаем обитаемыми безжизненные пока планеты. <br>
И начнем с Марса! <br>
Присоединяйся!</h1>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
