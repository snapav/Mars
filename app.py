from crypt import methods

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum'

class LoginForm(FlaskForm):
    astronaut_id = StringField('id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField('id капитана', validators=[DataRequired()])
    capitan_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    access = SubmitField('Доступ')




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


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    return render_template('astronaut_selection.html')


@app.route('/answer', methods=['POST'])
@app.route('/auto_answer', methods=['POST'])
def answer():
    context = {
        'surname': request.form['surname'],
        'name': request.form['name'],
        'education': request.form['education'],
        'profession': ', '.join(request.form.getlist('profession')),
        'gender': request.form['gender'],
        'motivation': request.form['motivation'],
        'ready': request.form.get('ready', '') == 'Готов'
    }
    return render_template('answer.html', **context)

@app.route('/training/<prof>')
def training(prof):
    context = {
        'prof': prof
    }
    return render_template('training.html', **context)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    context = {
        'profs': ['врач', 'инженер', "механик", "охранник", "строитель"],
        'list': lst,

    }
    return render_template('list_prof.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    if form.validate_on_submit():
        return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)