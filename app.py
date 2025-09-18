from flask import Flask, redirect, url_for, request, render_template
from routes import bp
import tkinter as tk
import threading
from ACEest_Fitness import FitnessTrackerApp
app = Flask(__name__)

def run_tkinter_app():
    root = tk.Tk()
    app_instance = FitnessTrackerApp(root)
    root.mainloop()

@app.route('/')
def acestfitness():
    threading.Thread(target=run_tkinter_app).start()
    return  render_template("index.html")

@app.route('/hello')
def hello_world():
    return render_template("hello.html")
@app.route('/login')
def login_world():
    return render_template("login.html")

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))
    
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

        
""" if __name__=='__main__':
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

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__=='__main__':
    app.run(debug=True)

    