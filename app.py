from flask import Flask,request,render_template

import pickle
app = Flask(__name__)
@app.route('/',methods = ['POST','GET'])
def main():
    if request.method == 'POST':
        pclass = int(request.form['pclass'])
        sex = int(request.form['sex'])
        age = float(request.form['age'])
        sibpb = int(request.form['sibpb'])
        parch = int(request.form['parch'])
        fare = float(request.form['fare'])
        data = [[pclass,sex,age,sibpb,parch,fare]]
        model=pickle.load(file=open('titanic.pickle','rb'))
        result=model.predict(data)

        return render_template('index.html',result = result[0],form = 0)
    return render_template('index.html',form = 1)
if __name__ == '__main__':
    app.run(debug = True)
