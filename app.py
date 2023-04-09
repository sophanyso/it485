from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from fileinput import filename
import pandas 
import pickle

#User-login page
# User name is testuser
# Password is 123

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'testuser':'123','tester':'500','it485':'234'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    elif database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
    else:
        return render_template('base.html',name=name1)



#Read excel file

@app.route('/upload')
def upload():
    return render_template('upload.html')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r>' % self.id
    

 
@app.post('/view')
def view():
    file = request.files['file']
    file.save(file.filename)
    data = pandas.read_excel(file)
    return data.to_html()        
        

if __name__ == '__main__':
    app.run(debug=True)
