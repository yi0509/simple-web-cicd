from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>CI/CD自动部署实验<br>学号：2440666121<br>姓名：古心怡<br>服务器IP：8.138.122.7</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)