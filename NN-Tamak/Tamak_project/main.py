from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
import pymysql
import uvicorn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import subprocess
import os
from PIL import Image, ImageDraw
import shutil

def nn():
    print('запуск нейросети')
    # Путь к исходному файлу
    source = 'C:/Users/Admin/PycharmProjects/NN-Tamak/Tamak_project/templates/input.jpg'
    print('запуск нейросети')
    # Путь к целевой директории
    destination = 'C:/Users/Admin/PycharmProjects/TC/TFODCourse/Tensorflow/workspace/images/input/input.jpg'
    print('запуск нейросети')
    # Перемещение файла
    shutil.move(source, destination)
    print('запуск нейросети')
    # Переход в другую директорию
    new_directory = 'C:/Users/Admin/PycharmProjects/TC/TFODCourse'
    os.chdir(new_directory)
    print('запуск нейросети')
    # Выполнение команды Jupyter Notebook
    command = ['jupyter', 'nbconvert', '--execute', 'Detect.ipynb', '--to', 'html']
    result = subprocess.run(command, capture_output=True, text=True, cwd=new_directory)
    print('запуск нейросети')
    # Проверка статуса выполнения команды
    if result.returncode == 0:
        print("Команда успешно выполнена")
    else:
        print("Команда вернула ошибку")

    # Вывод результата работы команды
    print(result.stdout)

    new_directory = 'C:/Users/Admin/PycharmProjects/NN-Tamak/Tamak_project'
    os.chdir(new_directory)

    def wall(_ymin, _xmin, _ymax, _xmax):
        _wall = (_xmin, _ymin, _xmax, _ymax)
        draw.rectangle(_wall, outline='black', width=2, fill='black')

    def window(_ymin, _xmin, _ymax, _xmax):
        _wall = (_xmin, _ymin, _xmax, _ymax)
        draw.rectangle(_wall, outline='black', width=2, fill='black')
        if _xmax - _xmin > _ymax - _ymin:
            delta = (_xmax - _xmin) / 4
            _xmax = _xmax - delta
            _xmin = _xmin + delta
            _window = (_xmin, _ymin, _xmax, _ymax)
            draw.rectangle(_window, outline='black', width=2, fill='white')
        else:
            delta = (_ymax - _ymin) / 4
            _ymax = _ymax - delta
            _ymin = _ymin + delta
            _window = (_xmin, _ymin, _xmax, _ymax)
            draw.rectangle(_window, outline='black', width=2, fill='white')

    def door(_ymin, _xmin, _ymax, _xmax):
        if _xmax - _xmin > _ymax - _ymin:
            delta = (_xmax - _xmin)
            xmin_ = _xmin
            ymin_ = _ymin - (_ymax - _ymin)
            xmax_ = _xmax + delta
            ymax_ = _ymax
            start_angle = 90  # начальный угол дуги в градусах (вверх)
            end_angle = 180  # конечный угол дуги в градусах (вниз)
            _rectangle = (
            _xmin, _ymin, _xmax, _ymax)  # координаты верхнего левого и нижнего правого углов прямоугольника
            rectangle_ = (xmin_, ymin_, xmax_, ymax_)
            draw.arc(rectangle_, start_angle, end_angle, fill='black', width=2)

            start_point = (_xmin, _ymin)
            end_point = (_xmax, _ymin)
            draw.line([start_point, end_point], fill='black', width=2)
            delta_x = _xmax - _xmin
            xmin = _xmax - delta_x / 5
            ymin = _ymin
            xmax = _xmax
            ymax = _ymax
            draw.rectangle((xmin, ymin, xmax, ymax), outline='black', width=2, fill='white')

        else:
            xmin_ = _xmin
            ymin_ = _ymin - (_ymax - _ymin)
            xmax_ = _xmax + (_xmax - _xmin)
            ymax_ = _ymax

            start_angle = 90  # начальный угол дуги в градусах (вверх)
            end_angle = 180  # конечный угол дуги в градусах (вниз)
            _rectangle = (
            _xmin, _ymin, _xmax, _ymax)  # координаты верхнего левого и нижнего правого углов прямоугольника
            rectangle_ = (xmin_, ymin_, xmax_, ymax_)
            draw.arc(rectangle_, start_angle, end_angle, fill='black', width=2)
            # draw.rectangle(_rectangle, outline='blue', width=2)
            # draw.rectangle(rectangle_, outline='orange', width=2)

            delta_y = _ymax - _ymin
            ymin = _ymin
            xmax = _xmax
            ymax = _ymax
            _ymax = _ymin + delta_y / 5
            start_point = (xmax, ymin)
            end_point = (xmax, ymax)
            draw.rectangle((_xmin, _ymin, _xmax, _ymax), outline='black', width=2, fill='white')
            draw.line([start_point, end_point], fill='black', width=2)

    def confert():
        results = []
        with open('results.txt', 'r') as file:
            for line in file:
                elements = line.split()
                _class = elements[1]
                _ymin = elements[5]
                _ymax = elements[6]
                _xmin = elements[7]
                _xmax = elements[8]
                _width = elements[10]
                _height = elements[12]
                _r = elements[17]

                _class = _class[:-1]

                _ymin = _ymin[5:]
                _ymin = _ymin[:-1]
                _ymin = float(_ymin)

                _ymax = _ymax[5:]
                _ymax = _ymax[:-1]
                _ymax = float(_ymax)

                _xmin = _xmin[5:]
                _xmin = _xmin[:-1]
                _xmin = float(_xmin)

                _xmax = _xmax[5:]
                _xmax = _xmax[:-1]
                _xmax = float(_xmax)

                _height = _height[7:]
                _height = _height[:-1]
                _height = int(_height)

                _width = _width[6:]
                _width = _width[:-1]
                _width = int(_width)

                _r = _r[2:]
                _r = _r[:1]
                _r = int(_r)

                result = [_class, _ymin, _ymax, _xmin, _xmax, _width, _height, _r]
                results.append(result)
        file.close()
        return results

    _list = confert()

    width = _list[0][5]
    height = _list[0][6]
    _w = 16

    elem_horizont = []
    elem_vertical = []

    for l in _list:
        if l[7] == 1:
            elem_horizont.append(l)
        else:
            elem_vertical.append(l)

    # Создание изображения
    image = Image.new('RGB', (width, height), 'white')

    # Создание объекта рисования
    draw = ImageDraw.Draw(image)

    delta_0 = 20
    delta_1 = 20

    for l in _list:
        if l[7] == 1:
            if l[4] - l[2] <= 35:
                _list.remove(l)
        else:
            if l[3] - l[1] <= 35:
                _list.remove(l)

    # выравнивание по горизонту
    for i in elem_horizont:
        for j in elem_horizont:
            if abs(i[1] - j[1]) <= delta_0:
                i[1] = j[1]
                i[3] = j[1]

    # выравнивание по вертикали
    for i in elem_vertical:
        for j in elem_vertical:
            if abs(i[2] - j[2]) <= delta_0:
                i[2] = j[2]
                i[4] = j[2]

    # для изменени горизонтальх объектов
    for i in elem_horizont:
        for j in elem_vertical:
            if abs(i[2] - j[2]) <= delta_1:
                i[2] = j[2]
            else:
                if abs(i[4] - j[4]) <= delta_1:
                    i[4] = j[4]

    # для изменения вертикальных объектов
    for i in elem_vertical:
        for j in elem_horizont:
            if abs(i[1] - j[1]) <= delta_1:
                i[1] = j[1]

            if abs(i[3] - j[3]) <= delta_1:
                i[3] = j[3]

    for i in elem_horizont:
        i[1] = i[1] - _w / 2
        i[2] = i[2] - _w / 2
        i[3] = i[3] + _w / 2
        i[4] = i[4] + _w / 2

    for i in elem_vertical:
        i[1] = i[1] - _w / 2
        i[2] = i[2] - _w / 2
        i[3] = i[3] + _w / 2
        i[4] = i[4] + _w / 2

    for l in _list:
        if l[0] == 'wall':
            wall(l[1], l[2], l[3], l[4])
            # print('wall')
        else:
            if l[0] == 'window':
                window(l[1], l[2], l[3], l[4])
            else:
                door(l[1], l[2], l[3], l[4])

    image.save('templates/image.jpg')
    img_path = "templates/image.jpg"
    return img_path


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

# Подключение к базе данных PyMySQL
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db_nn',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM parser"
        cursor.execute(sql)
        data = cursor.fetchall()
finally:
    connection.close()

@app.get("/home")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/nn")
def NN(request: Request):
    return templates.TemplateResponse("nn.html", {"request": request})

@app.get("/support")
def support(request: Request):
    return templates.TemplateResponse("support.html", {"request": request})

@app.get("/team")
def support(request: Request):
    return templates.TemplateResponse("team.html", {"request": request})

@app.get("/user")
def support(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})

@app.get("/project")
def support(request: Request):
    return templates.TemplateResponse("project.html", {"request": request})

@app.get("/login")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
def home(request: Request):
    return templates.TemplateResponse("registr.html", {"request": request})

@app.get("/catalog")
def home(request: Request):
    return templates.TemplateResponse("catalog.html", {"request": request,  "data": data})

@app.post("/reg")
def register(request: Request, email: str = Form(...), username: str = Form(...), password: str = Form(...), password_confirm: str = Form(...)):
    # Проверка наличия пользователя в базе данных
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users WHERE email=%s"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
        if result:
            return {"message": "Email already exists"}

    # Проверка соответствия паролей
    if password != password_confirm:
        return {"message": "Passwords don't match"}

    # Вставка нового пользователя в базу данных
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (email, username, password))
    connection.commit()

    return {"message": "Registration successful"}

@app.post("/log")
def login(request: Request, email: str = Form(...), password: str = Form(...)):
    # Проверка правильности логина и пароля
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))
        result = cursor.fetchone()
        if not result:
            return {"message": "Invalid email or password"}

    return {"message": "Login successful"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Путь к папке, в которую нужно сохранить файл
    folder_path = 'C:/Users/Admin/PycharmProjects/NN-Tamak/Tamak_project/templates'

    # Имя файла
    file_name = 'input.jpg'

    # Полный путь до файла
    file_path = os.path.join(folder_path, file_name)

    contents = await file.read()

    # Сохранение загруженного файла
    with open(file_path, "wb") as f:
        f.write(contents)

    # return {"filename": file.filename}
    return {"img_url": f"templates/{file_name}"}

@app.get("/get_image/{image_name}")
async def get_image(image_name: str):
    image_path = nn()  # путь к изображению в директории
    return FileResponse(image_path)

if __name__ == "__main__":
    # uvicorn.run(app, host="192.168.0.105", port=8000)
    uvicorn.run(app, host="127.0.0.1", port=8000)