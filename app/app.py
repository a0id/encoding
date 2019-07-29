from flask import Flask, render_template, flash, request, redirect, url_for, session, send_from_directory, logging

app = Flask(__name__, static_url_path='/static')

from wtforms import Form, StringField, TextAreaField, PasswordField, validators, FileField

from encoder import Encoder
from decoder import Decoder

class EncryptForm(Form):
    text = TextAreaField('', [validators.DataRequired()])
    zero = StringField('', [validators.DataRequired()])
    one = StringField('', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/encode', methods=['GET', 'POST'])
def encrypt():
    form = EncryptForm(request.form)
    if request.method == 'POST' and form.validate():
        text = form.text.data
        zero = form.zero.data
        one = form.one.data

        encoder = Encoder(zero, one)
        encoded_text = encoder.encode(text)
        
        print(encoded_text)
        session['show_encoded'] = True
        return render_template('encode.html', encoded=encoded_text, form=form)
    
    session['show_encoded'] = None
    return render_template('encode.html', form=form)

@app.route('/decode', methods=['GET', 'POST'])
def upload_file():
    session['filename'] = ''
    if request.method == 'POST':
        # check if the post `request has the file part
        if 'file' not in request.files :
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            PATH = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(PATH)
            session['filename'] = filename
            text = ''
            with open(Decrypt(PATH).NAME, 'r') as f:
                text = f.read()
            print(text)
            return render_template('decode.html', text=text)
    else:
        session['filename'] = ''
    return render_template('decode.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host= '0.0.0.0', debug=True)
