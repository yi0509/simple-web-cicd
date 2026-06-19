from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>CI/CD 自动部署实验成功！服务器IP：8.138.122.7</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
