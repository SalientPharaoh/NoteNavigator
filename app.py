from flask import Flask, make_response,render_template, request
from script import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        string = request.form['Notes']
        try: sign = request.form['sign']
        except: sign = "+"
        try:
            if sign=="-" : value =12 - int(request.form['value'])
            else : value=int(request.form['value'])
            tpose_string = start(value, string.upper())
            return render_template('index.html', string=tpose_string)
        except:
            return render_template('index.html', string="Invalid Input")

    return render_template('index.html') 

@app.route('/chord-progression', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        string = request.form['Song Key']
        try: sign = request.form['sign']
        except: sign = "M"
        try:
            if sign=="M" : chords = major_chord(string)
            else : chords = minor_chord(string)
            return render_template('chord_gen.html', string=chords)
        except:
            return render_template('chord_gen.html', string="Invalid Input")
        
    return render_template('chord_gen.html') 

@app.route('/chord-transpose', methods=['GET', 'POST'])
def chord():
    if request.method == 'POST':
        string = request.form['Notes']
        try: sign = request.form['sign']
        except: sign = "+"
        try:
            if sign=="-" : value =12 - int(request.form['value'])
            else : value=int(request.form['value'])
            tpose_string = chord_start(value, string)
            return render_template('chord_tpose.html', string=tpose_string)
        except:
            return render_template('chord_tpose.html', string="Invalid Input")
        
    return render_template('chord_tpose.html') 


if __name__ == '__main__':
    app.run(debug=True)