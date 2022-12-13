from flask import Flask, render_template, request
import pickle
model = pickle.load(open('artifacts/model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def welcome():
    
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    BMI = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])
    
    data=[[age,sex,BMI,children,smoker,region]]
    res = model.predict(data)
    

    return render_template('index.html',result=res)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)