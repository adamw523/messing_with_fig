from db import db, Tick
from flask import Flask, redirect, render_template, request, url_for
import flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ticks', methods=['GET', 'POST'])
def ticks():
    if request.method == 'POST':
        t = Tick(message=request.form['message'])
        db.session.add(t)
        db.session.commit()

    return render_template('ticks.html', ticks=Tick.query.all())

@app.route('/ticks/<int:id>/delete')
def ticks_delete(id=None):
    t = Tick.query.get(id)
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for('ticks'))

@app.route('/ticks/create_all')
def ticks_create_all():
    db.create_all()
    return redirect(url_for('index'))

app.debug = True

if __name__ == '__main__':
    app.run(host='0.0.0.0')

