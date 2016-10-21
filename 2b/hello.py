#coding=utf-8
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
			# <> 尖括号是动态的内容，任何能匹配静态部分的 URL 都会映射到这个路由上
			# 路由中的动态部分默认使用字符串，不过也可使用类型定义。例如，路由 /user/<int:id>
			# 只会匹配动态片段 id 为整数的 URL。 Flask 支持在路由中使用 int、 float 和 path 类型。
			# path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。

def user(name):
    print type(name),'=====>',name
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
