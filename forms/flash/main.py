from flask import Flask,render_template,flash,session,render_template,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MYKEY'

class SimpleForm(FlaskForm):

    breed = StringField('What breed are you?')
    submit = SubmitField('Click me ')

@app.route('/',methods=['GET','POST'])
def index():

    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        return redirect(url_for("index"))

    return render_template('index.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)