import sql as Mysql
from flask import Flask, render_template, request, jsonify
from database import Database

# 创建Flask对象app并初始化
app = Flask(__name__)


@app.route("/")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("index.html")


# app的路由地址"/submit"即为ajax中定义的url地址，采用POST、GET方法均可提交
@app.route("/submit", methods=["GET", "POST"])
# 从这里定义具体的函数 返回值均为json格式
def submit():
    # 由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    if request.method == "POST":
        request.form.get("主播名字")
        request.form.get("房间号")
    if request.method == "GET":
        name = request.args.get("主播名字")
        number = request.args.get("房间号")
    # 如果获取的数据为空
        if len(name) == 0 or len(number) == 0:
            return {'message': "error!"}
        else:
            return {'message': "success!", 'name': name, 'age': number}


# 通过python装饰器的方法定义路由地址
@app.route("/data")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def data():
    return render_template("data.html")


# app的路由地址"/show"即为ajax中定义的url地址，采用POST、GET方法均可提交
@app.route("/show", methods=["GET", "POST"])
def show():
    # 首先获取前端传入的name数据
    global Mysql
    if request.method == "POST":
        name = request.form.get("主播名字")
        number = request.form.get("房间号")
    if request.method == "GET":
        name = request.args.get("主播名字")
        number = request.args.get("房间号")
# 创建Database类的对象Mysql，android为需要访问的数据库名字 具体可见Database类的构造函数
        Mysql = Database("android")
    try:
        # 执行sql语句 多说一句，f+字符串的形式，可以在字符串里面以{}的形式加入变量名 结果保存在result数组中
        result = Mysql.execute(f"SELECT type FROM type WHERE douyu='{name,number}'")

    except Exception as e:
        return {'status': "error", 'message': "code error"}
    else:
        if not len(result) == 0:
            # 这个result，我觉得也可以把它当成数据表，查询的结果至多一个，result[0][0]返回数组中的第一行第一列
            return {'status': 'success', 'message': result[0][0]}
        else:
            return "rbq"


# 定义app在8080端口运行
app.run(port=8080)
