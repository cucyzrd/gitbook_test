#coding=utf-8
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	# index()视图函数
    return '<h1>Hello World!</h1>'
    # 返回响应


if __name__ == '__main__':
    app.run(debug=True)
