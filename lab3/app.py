from flask import Flask, render_template, request
import platform
from datetime import datetime

app = Flask(__name__)

# Список ваших навичок та умінь
my_skills = [
    "Python",
    "Flask",
    "HTML",
    "CSS",
]

# Маршрут для відображення всіх навичок
@app.route('/skills')
def display_all_skills():
    return render_template('skills.html', skills=my_skills)

# Маршрут для відображення конкретної навички за її індексом у списку
@app.route('/skills/<int:id>')
def display_skill(id):
    if 0 <= id < len(my_skills):
        skill = my_skills[id]
        return f"Skill #{id}: {skill}"
    else:
        return "Skill not found"

# Маршрут для індексної сторінки
@app.route('/')
def index():
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os_info = platform.system()  # Отримання інформації про операційну систему

    return render_template('base.html', user_agent=user_agent, current_time=current_time, os_info=os_info)

# Маршрути для сторінок page1, page2 і page3
@app.route('/page1')
def page1():
    return render_template('page1.html')

if __name__ == '__main__':
    app.run(debug=True)
