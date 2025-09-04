from flask import Flask, redirect, url_for, request, render_template
from routes import bp
import tkinter as tk
import threading
from ACEest_Fitness import FitnessTrackerApp
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("hello.html")

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

def run_tkinter_app():
    root = tk.Tk()
    app_instance = FitnessTrackerApp(root)
    root.mainloop()

@app.route('/acestfitness')
def acestfitness():
    threading.Thread(target=run_tkinter_app).start()
    return  "Fitness Tracker app launched!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

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
    app.run(debug=True)

    