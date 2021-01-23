from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', time = time, status = False)

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(debug=True)