from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)
model = pickle.load(open('hlr_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=0
        else:
            Gender=1
            
        Age = int(request.form['Age'])
        Height = float(request.form['Height'])
        Weight=float(request.form['Weight'])
        BMI = Weight/(Height*Height)
        RBS = float(request.form['RBS'])
        Addiction=request.form['Addiction']
        if(Addiction=='Yes'):
            Addiction=1
        else:
            Addiction=0
           
        Sick_Leave=float(request.form['Sick Leave'])
        Creatinine = float(request.form['Creatinine'])
        SGPT = float(request.form['SGPT'])
        BP = request.form['BP']
        # Kms_Driven2=np.log(Kms_Driven)
        BP = BP.split('/')
        SBP = float(BP[0])
        DBP = float(BP[1])
        
        
        prediction=model.predict([[Gender,Age,Height,Weight,BMI,RBS,Addiction,Sick_Leave,Creatinine,SGPT,SBP,DBP]])
        output=prediction
        print(output)
        print('hello')
        if output==0:
            print('Zero')
            return render_template('index1.html',prediction_text="Best Health!! 🙂")
        elif output==1:
            print('One')
            return render_template('index1.html',prediction_text="Average Health!! 😐")
        else:
            print('Two')
            return render_template('index1.html',prediction_text="Poor Health!! ☹")
        # else:
        #     return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

