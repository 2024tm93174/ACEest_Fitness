from flask import Flask, redirect, url_for, request
from routes import bp

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask World!'
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/templates/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


def create_app(test_config=None):
    app.config.update(
        TESTING=False,
        SECRET_KEY="supersecret",
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
    )

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(bp)


if __name__=='__main__':
    app.run(debug=True)