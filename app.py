from lib2to3.fixes.fix_input import context
from os import lstat

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html")


@app.route('/index/<title>')
def about(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    return '''<h1>Человечество вырастает из детства. <br>
Человечеству мала одна планета. <br>
Мы сделаем обитаемыми безжизненные пока планеты. <br>
И начнем с Марса! <br>
Присоединяйся!</h1>'''

@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')

@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')

@app.route('/astronaut_selection' , methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['motivation'])
        print(request.form['gender'])
        print(request.form['ready'])
        print(request.form['email'])
        return '<h1> Анкета отправлена </h1>'

@app.route('/training/<prof>')
def training(prof):
    context ={
        'prof': prof
    }
    return  render_template('training.html', **context)

@app.route('/list_prof/<lst>')
def list_prof(lst):
    context = {
        'profs': ['врач', 'инженер', "механик", "охранник", "строитель"],
        'list': lst,

    }
    return render_template('list_prof.html', **context)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)