from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', status = False)

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(debug=True)