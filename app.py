import datetime
import csv
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/hi')
def hi():
    return '안녕, 지원'
    
# 5월 20일부터 d-day를 출력하는 것을 만들어주세요.
@app.route('/dday')
def dday():
    now = datetime.datetime.now()
    vacation = datetime.datetime(2019, 5, 20)
    result = vacation - now
    # return은 반드시 string으로 되어야 한다
    return f'{result.days}일 남았다'

@app.route('/hi/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)

# 세제곱의 결과를 출력해볼게요!
@app.route('/cube/<int:num>')
def cube(num):
    return f'{num}^3 = {num**3}'
    
@app.route('/movie')
def movie():
    movies = ['극한직업', '신비한 동물 사전', '그린북', '그린랜턴']
    return render_template('movie.html', movies=movies)
    
@app.route('/google')
def google():
    return render_template('google.html')
    
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
    # request.args = {'name':'뿡', 'msg':'안녕'}
    name = request.args.get('name')
    msg = request.args.get('msg')
    return render_template('pong.html', name=name, msg=msg)

@app.route('/op.gg')
def opgg():
    playerName = request.args.get('playerName')
    return render_template('opgg.html', playerName=playerName)

@app.route('/op.ggg')
def opggg():
    playerName = request.args.get('playerName')
    return render_template('opgg.html', playerName=playerName)
    
@app.route('/timeline')
def timeline():
    # 지금까지 기록되어있는 방명록들을 ('timeline.csv')를 읽어서 보여주기
    timelines = []
    with open('timeline.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            timelines.append(row)
    return render_template('timeline.html', timelines=timelines)
    
@app.route('/timeline/create')
def timeine_create():
    username = request.args.get('username')
    message = request.args.get('message')
    # a : append, w : write
    with open('timeline.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['username', 'message'])
        writer.writerow({
            'username': username,
            'message': message
        })
    # return render_template('timeline_create.html', username=username, message=message)
    return redirect('/timeline')

@app.route('/dictionary/<string:word>')
def greeting2(word):
    return render_template('190128workshop.html', html_name=word)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)