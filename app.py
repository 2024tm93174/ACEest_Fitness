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
        
""" def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(bp)
    return app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True) """

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # in-memory DB for testing
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  
    @app.route("/ping")
    def ping():
        return {"message": "pong"}

    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(bp)
    return app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True)

    