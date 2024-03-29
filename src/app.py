from flask import Flask, render_template
from routes import InsightFlow

app = Flask(__name__)
app.register_blueprint(InsightFlow, url_prefix='')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
