from flask import Flask, render_template
from scrape import get_data

app = Flask(__name__)

@app.route('/')
def home():
    df = get_data()
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
