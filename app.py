from flask import Flask,render_template,request,jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict',methods=['POST'])
def predict():
  if request.method == "POST" :

     FS = int(request.form["FS"])
     FU = int(request.form["FU"])  
     with open('my_model','rb') as f:
         model = pickle.load(f)    
     result = model.predict([[FS,FU]])
     if result[0] == "NO":
       return render_template('index.html',data=["Congratulations You dont have diabetes","green"])  
     else:
        return render_template('index.html',data=["Sorry you might have diabeties","red"])    


if __name__ == "__main__":
    app.run(debug=True)