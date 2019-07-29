from flask import Flask, render_template, flash, request, redirect, url_for, session, send_from_directory, logging

app = Flask(__name__, static_url_path='/static')

from wtforms import Form, StringField, TextAreaField, PasswordField, validators, FileField

from encoder import Encoder
from decoder import Decoder

class BasicForm(Form):
    text = TextAreaField('', [validators.DataRequired()])
    zero = StringField('', [validators.DataRequired()])
    one = StringField('', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/encode', methods=['GET', 'POST'])
def encrypt():
    session['show_encoded'] = False
    form = BasicForm(request.form)
    if request.method == 'POST' and form.validate():
        text = form.text.data
        zero = form.zero.data
        one = form.one.data

        encoder = Encoder(zero, one)
        encoded_text = encoder.encode(text)
        
        print(encoded_text)
        session['show_encoded'] = True
        return render_template('encode.html', encoded=encoded_text, form=form)
    
    session['show_encoded'] = False
    return render_template('encode.html', form=form)

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    session['show_decoded'] = False
    form = BasicForm(request.form)

    if request.method == 'POST' and form.validate():
        text = form.text.data
        zero = form.zero.data
        one = form.one.data

        decoder = Decoder(zero, one)
        decoded_text = decoder.decode(text)
        
        session['show_decoded'] = True
        return render_template('decode.html', decoded=decoded_text, form=form)

    session['show_decoded'] = False
    return render_template('decode.html', form=form)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host= '0.0.0.0', debug=True)
