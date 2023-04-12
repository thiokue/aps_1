from flask import Flask, render_template, redirect, url_for
from scrape import get_data
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('tripAdvisor_Atividades_ao_ar_livre.csv')
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/update')
def update():
    get_data()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
