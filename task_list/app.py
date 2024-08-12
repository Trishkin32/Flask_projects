from flask import  Flask, render_template

app = Flask(__name__)


@app.route('/')
def task_list():
    tasks = ["Проснуться в 6:00" , "Позавтракать", "Выйти на пробежку",
             "Почитать книгу", "Пообедать", "Купить продукты", "Посотреть фильм"]
    return render_template("task_list.html", tasks=tasks)


if __name__ == "__main__":
    app.run()
