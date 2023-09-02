from flask import Flask,request,render_template,jsonify
import requests
import pandas as pd
import numpy as np

application=Flask(__name__)
app=application


@app.route('/')
def index():
    if request.method=='GET':  
        return render_template('index.html')

@app.route('/part1',methods=['GET','POST'])
def part1():
    if request.method=='GET':  
        return render_template('form1.html')

@app.route('/part2',methods=['GET','POST'])
def part2():
    if request.method=='GET':  
        return render_template('form2.html')

@app.route('/getpassages',methods=['GET','POST'])
def getpassages():
    if request.method == "POST":
        data = request.form['passagetype']

    #data = dict(request.form.get('passagetype'))
    url = 'https://elvinatech.in/dicey/getPassages.php?passagetype='+data
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url,headers=headers)
    jsonData = response.json()
    return jsonify(jsonData)
    #return render_template('index.html', jsonData=jsonify(jsonData))

@app.route('/getquestions',methods=['GET','POST'])
def getquestions():
    if request.method == "POST":
        data = request.form['passages']

    #data = dict(request.form.get('passagetype'))
    url = 'https://elvinatech.in/dicey/getQuestions.php?PassageName='+data
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url,headers=headers)
    jsonData = response.json()
    return jsonify(jsonData)



@app.route('/predictpart1',methods=['GET','POST'])
def predictpart1():    
    if request.method == "POST":
        passagetype = request.form['passagetype']
        passages = request.form['passages']
        questions = request.form['questions']
        grade = request.form['grade']
        hour = request.form['hour']  
    prompt = 'Source:' + passagetype + ' Passage Name: ' + passages + ' Student Grade: ' + grade + 'Question: ' + questions + 'Hour of exam: ' + hour
    url = 'http://chattinc.com/dicey/part1'

    data = {"text": f"{prompt}"}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.post(url, json=data,headers=headers)
    jsonData = response.json()   
    if jsonData['Prediction'] == 1:
        return "Will respond well"
    else:
        return "Will fail"   
    

@app.route('/predictpart2',methods=['GET','POST'])
def predictpart2():    
    if request.method == "POST":
        passagetype = request.form['passagetype']
        passages = request.form['passages']
        questions = request.form['questions']
        grade = request.form['grade']
        hour = request.form['hour']  
    prompt = 'Source:' + passagetype + ' Passage Name: ' + passages + ' Student Grade: ' + grade + 'Question: ' + questions + 'Hour of exam: ' + hour
    url = 'http://chattinc.com/dicey/part2'

    data = {"text": f"{prompt}"}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.post(url, json=data,headers=headers)
    jsonData = response.json()   
    return "Expected answer from student: "+jsonData['Prediction']

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=False)

