from flask import Flask, render_template, session, request
from wtforms import Form, StringField, TextAreaField, validators
import sys

from encoder import Encoder
from decoder import Decoder

class BasicForm(Form):
    text = TextAreaField('', [validators.DataRequired()])
    zero = StringField('', [validators.DataRequired()])
    one = StringField('', [validators.DataRequired()])

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    session['show_encoded'] = False
    form = BasicForm(request.form)
    if request.method == 'POST' and form.validate():
        text = form.text.data
        zero = form.zero.data
        one = form.one.data

        encoder = Encoder(zero, one)
        encoded_text = encoder.encode(text)
        
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

def syntax():
    print('flags:')
    print('  --production, -p\n    Start a production server')
    print('  --development, -d\n    Start a development server')
        
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    
    if len(sys.argv) != 2:
        syntax()
        sys.exit(-1)
    
    if sys.argv[1] == '--production' or sys.argv[1] == '-p':
        app.run(host= '0.0.0.0', debug=False, port=80)
    
    elif sys.argv[1] == '--development' or sys.argv[1] == '-d':
        app.run(host= '0.0.0.0', debug=True, port=8080)

    else:
        syntax()