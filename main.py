from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
secret_key = 'f8ab5312884947aa7b60ec9e4f0c1e5e'
app.config['SECRET_KEY'] = secret_key

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')
  
@app.route("/second_page")
def second_page():
  return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")