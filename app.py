
import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('kmeanscluster.pkl','rb'))   


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
  '''
  For rendering results on HTML GUI
  '''
  income = int(request.args.get('income'))
  score = int(request.args.get('score'))
    
    
  predict = model.predict([[income,score ]])
  if predict==[0]:
    result="Customer is Careless"

  elif predict==[1]:
    result="Customer is Standard"
  elif predict==[2]:
    result="Customer is Regular"
  elif predict==[3]:
    result="Customer is Careful"

  else:
    result="Custmor is Sensible"
    
        
  return render_template('index.html', prediction_text='Model  has predicted  : {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)
