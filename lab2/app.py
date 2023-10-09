#!/usr/bin/python3

import cgi
import cgitb

# Увімкнути вивід веб-звітів про помилки для відладки
cgitb.enable()

# Отримання даних з форми
form = cgi.FieldStorage()

# Виведення заголовку HTML з правильним кодуванням
print("Content-Type: text/html; charset=utf-8\n")


# Виведення результатів з форми
print("<html>")
print("<head><title>Результати форми</title></head>")
print("<body>")
print("<h1>Результати відправки форми:</h1>")

# Отримання обраних значень з форми
name = form.getvalue("name")
age = form.getvalue("age")
gender = form.getvalue("gender")
hobbies = form.getlist("hobbies")
country = form.getvalue("country")

print("<p>Ім'я: {0}</p>".format(name))
print("<p>Вік: {0}</p>".format(age))
print("<p>Стать: {0}</p>".format(gender))
print("<p>Ваші хобі: {0}</p>".format(", ".join(hobbies)))
print("<p>Країна: {0}</p>".format(country))

print("</body>")
print("</html>")
