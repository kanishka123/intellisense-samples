from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')


# @app.route('/data.json')
# def data():
#      return app.send_static_file('data.json')

if __name__ == '__main__':
  app.run()

