from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask('MyApp')


@app.route('/index')
def func1():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/')
def func2():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/promotion')
def func3():
    text = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(text)


@app.route('/image_mars')
def func4():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    </br>Вот она какая, красная планета.
                  </body>
                </html>"""


@app.route('/promotion_image')
def func5():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-secondary" role="alert">
                    Человечество вырастает из детства.</div>
                    <div class="alert alert-success" role="alert">
                    Человечеству мала одна планета.</div>
                    <div class="alert alert-secondary" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning" role="alert">
                    И начнем с Марса!</div>
                    <div class="alert alert-danger" role="alert">
                    Присоединяйся!</div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def func6():
    if request.method == 'GET':
        return f'''<!doctype html>
                           <html lang="en">
                             <head>
                               <meta charset="utf-8">
                               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                               <link rel="stylesheet" type="text/css" href="/static/css/style1.css">
                               <title>Отбор астронавтов</title>
                             </head>
                            <h1 align="center">Анкета претендента</h1>
                            <h2 align="center">на участие в миссии</h2>
                             <div>
                                   <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    </br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </br>
                                    <div class="form-group">
                                           <label for="classSelect">Какое у Вас образование?</label>
                                           <select class="form-control" id="classSelect" name="class">
                                             <option>Начальное</option>
                                             <option>Среднее</option>
                                             <option>Среднее профессиональное</option>
                                             <option>Высшее</option>
                                           </select>
                                        </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="form-check">Какая у Вас основная профессия?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="researchengineer" value="researchengineer" checked>
                                          <label class="form-check-label" for="researchengineer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="civilengineer" value="civilengineer">
                                          <label class="form-check-label" for="civilengineer">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="meteorologist" value="meteorologist">
                                          <label class="form-check-label" for="meteorologist">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="lifesupportengineer" value="lifesupportengineer">
                                          <label class="form-check-label" for="lifesupportengineer">
                                            Инженер по жизнеобеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="radiationprotectionengineer" value="radiationprotectionengineer">
                                          <label class="form-check-label" for="radiationprotectionengineer">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="professions" id="exobiologist" value="exobiologist">
                                          <label class="form-check-label" for="exobiologist">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    </br>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                   </form>
                               </div>
                             </body>
                           </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def func7(planet_name):
    planet_name = planet_name.capitalize()
    planets = {
        'Меркурий': ['Есть вода и атмосфера;',
                     'Огромные запасы солнечной энергии;', 'Полное отсутствие атмосферы.'],
        'Венера': ['Вода практически полностью отсутствует;', 'Большие температуры;', 'Много углекислого газа.'],
        'Земля': ['Наш дом', 'Не требует колонизации', '(=^･ｪ･^=)'],
        'Марс': ['Эта планета близка к Земле;', 'На ней есть вода и атмосфера;',
                 'На ней есть небольшое магнитное поле.'],
        'Юпитер': ['Можно организовывать поселения в облачной атмосфере;', 'Присутствует радиация;',
                   'Имеет сильную гравитацию;'],
        'Сатурн': ['Его спутники очень перспективны, например:', 'Титан,', 'Энцелад.'],
        'Уран': ['Хороший кандидат для добычи гелия-3;', 'Можно разместить базу на одном из его спутников;',
                 'Является газовым гигантом.'],
        'Нептун': ['Находится далеко от Земли;', 'Спутники плохо изучены;',
                   'Очень слабая гравитация.'],
        'Плутон': ['...', 'Это...', 'Это не планета...']
    }
    if planet_name in planets.keys():
        planet = planets[planet_name]
    else:
        planet = ['Планета не найдена.', 'Такой планеты нет в Солнечной системе', 'или это не планета.']
    return f'''<!doctype html>
                    <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <meta charset="utf-8">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-success" role="alert">
                          {planet[0]}
                        </div>
                        <div class="alert alert-warning" role="alert">
                          {planet[1]}
                        </div>
                        <div class="alert alert-danger" role="alert">
                          {planet[2]}
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def func8(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                   <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <meta charset="utf-8">
                        <title>Результаты</title>
                   </head>
                   <body>
                    <h1>Результат отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                    Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    составляет {rating}!
                    <div class="alert alert-warning" role="alert">
                    Желаем удачи!
                    </div>
                   </body>
                </html>'''


@app.route('/carousel')
def func9():
    return f'''<!doctype html>
                <html lang="en">
                   <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
                        <title>Пейзажи Марса</title>
                   </head>
                   <body>
                    <h1 align="center">Пейзажи Марса</h1>
                    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                      <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                      </div>
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="/static/img/f.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                          <img src="/static/img/s.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                          <img src="/static/img/t.jpg" class="d-block w-100" alt="...">
                        </div>
                      </div>
                      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                      </button>
                      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                      </button>
                    </div>
                   </body>
                </html>'''


@app.route('/load_foto', methods=['POST', 'GET'])
def func10():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="/static/css/style1.css">
                               <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 align="center">Загрузка фотографии</h1>
                                <h2 align="center">для участия в миссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <img src="/static/img/file.jpg" alt="">
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.filename = 'file.jpg'
        file.save('static/img/file.jpg')
        result = os.stat('static/img/file.jpg')
        if result.st_size:
            img = Image.open('static/img/file.jpg')
            width, height = img.size
            new_image = img.resize((425, int(height // (width / 425))))
            new_image.save('static/img/file.jpg')
        return redirect('/load_foto')

# app.route('/<title>')
# app.route('/index/<title>')
# def func220(title):
#    return render_template('index.html', title=title)


app.run(port=8080, host='127.0.0.1', debug=True)
