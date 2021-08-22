import datetime

from flask import Flask, render_template

app = Flask(__name__)


# 路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():  # put application's code here
#
#     return '你好!欢迎，请进！'


# Debug模式开启

@app.route('/index')
def index():  # put application's code here
    return '你好!欢迎，请进！'


# 通过访问路径获取用户的字符串参数
@app.route('/user/<name>')
def welcome(name):  # put application's code here
    return '你好!%s！' % name


# 通过访问路径获取用户的整形参数  此外还有float类型
@app.route('/user/<int:id>')
def welcome2(id):  # put application's code here
    return '你好!%d号会员！' % id


# 路由路径不能重复，用户只能通过唯一路径来访问特定的函数

# 返回给用户渲染后的网页文件
# @app.route("/")
# def index2():
#     return render_template("index.html")

# 向页面传递一些变量
@app.route("/")
def index2():
    time = datetime.date.today()  # 普通变量
    name = ["小张", "小王", "小赵"]  # 列表类型
    task = {"任务": "打扫卫生", "时间": "3小时"}  # 字典类型
    return render_template("index.html", var=time, list=name, task=task)


if __name__ == '__main__':
    app.run()
