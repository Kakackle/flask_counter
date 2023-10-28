# Words Counter and Paragraphs Counter Flask App using Python

from flask import Flask,request,render_template
from datetime import date

#### Defining Flask App
app = Flask(__name__)


#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

def replace_multiple_newlines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

################## ROUTING FUNCTIONS #########################

#### Our main page
@app.route('/')
def home():
    return render_template('index.html',datetoday2=datetoday2) 

#### This function will run when we add a new user
@app.route('/count',methods=['GET','POST'])
def count():
    text = request.form['text']
    word = request.form['word']
    print(request.form)
    word_count = 0
    
    words = len(text.split())
    
    if word != '':
        for w in text.split():
            if w.lower() == word.lower():
                word_count+=1

    paras = replace_multiple_newlines(text)

    text = text.replace('\r','')
    text = text.replace('\n','')

    chars = len(text)
    return render_template('index.html',text=text, words=words,paras=paras,chars=chars,datetoday2=datetoday2, word_count=word_count, word=word) 


#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)