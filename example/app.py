from flask import Flask, render_template, request
from models import Artist, Album, Song, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return "Вы вошли в систему"
    else:
        return render_template('login.html')


@app.route('/user/<username>')
def user_profile(username):
    return f"Это профиль пользователя: {username}"


# @app.route('/user/<int:user_id>')
# def user_profile_id(user_id):
#     return f"Это профиль пользователя с ID {user_id}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return "Блог с заметками"


@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)


if __name__ == '__main__':
    app.run(debug=True)