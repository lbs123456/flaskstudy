# 姓名；李伯术
# 目标；三个月学会Python，找到工作

from flask import Flask,render_template,redirect,request
ap = Flask(__name__)
STUDENT = {'name': 'Old', 'age': 38, 'gender': '中'},

STUDENT_LIST = [
    {'name': 'Old', 'age': 38, 'gender': '中'},
    {'name': 'Boy', 'age': 73, 'gender': '男'},
    {'name': 'EDU', 'age': 84, 'gender': '男'}
]

STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}
@ap.route("/")
def index():
    return "Hello World"

@ap.route("/login",methods=("POST","GET","PUT"))
def login():
    met = request.method
    if met == "GET":
        return render_template("login.html")
    if met == "POST":

        username = request.form.get("username")
        pwd = request.form.get("password")
        if username == "baby" and pwd == "want":
            return render_template("anglababy.html")
        return render_template("login.html",msg="你错了")

@ap.route("/detail")
def detail():
    return render_template("detail.html",stu=STUDENT)
ap.run(host= "0.0.0.0",port = 9527, debug = True)
