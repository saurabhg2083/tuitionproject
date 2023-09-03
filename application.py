from flask import Flask,request,render_template,jsonify
import requests
import pandas as pd
import numpy as np
import json

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
        Source = request.form['passagetype']

    #data = dict(request.form.get('passagetype'))
    url = 'https://elvinatech.in/dicey/getQuestions.php?PassageName='+data+'&Source='+Source
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url,headers=headers)
    jsonData = response.json()
    return jsonify(jsonData)



@app.route('/predictpart1',methods=['GET','POST'])
def predictpart1():    
    if request.method == "POST":
        Source = request.form['passagetype']
        PassageName = request.form['passages']
        QuestionId = request.form['questions']
        StudentGrade = request.form['grade']
        ExamHour = request.form['hour']  

    if StudentGrade != '':
        if int(StudentGrade) == 3:
            StudentAge = '8'
        if int(StudentGrade) == 4:
            StudentAge = '9'
        if int(StudentGrade) == 5:
            StudentAge = '10'
        if int(StudentGrade) == 6:
            StudentAge = '11'
    else:
        StudentAge = '8'


    
    AttentionLevelName = get_attention_level(int(ExamHour))

    url = 'https://elvinatech.in/dicey/getDetails.php?Source='+Source+'&PassageName='+PassageName+'&StudentGrade='+StudentGrade+'&QuestionId='+QuestionId
    #url = 'https://elvinatech.in/dicey/getDetails.php?Source=mocktest&PassageName=notre-dame&StudentGrade=5&QuestionId=1'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url,headers=headers)
    jsonData = response.json()

    #return jsonData['Genre']
    QuestionText=jsonData[0]['QuestionText']
    Genre = jsonData[0]['Genre']
    VocabularyAndLanguageComplexity = jsonData[0]['VocabularyAndLanguageComplexity']
    SentenceStructure = jsonData[0]['SentenceStructure']
    ThemesAndContent = jsonData[0]['ThemesAndContent']
    Overall = jsonData[0]['Overall']
    QuestionDifficultyDesc = jsonData[0]['QuestionDifficulty']
    QuestionTypeMeaning = '' #jsonData[0]['QuestionTypeMeaning']
    A = jsonData[0]['A']
    B = jsonData[0]['B']
    C = jsonData[0]['C']
    D = jsonData[0]['D']
    E = jsonData[0]['E']
    CorrectAnswer = jsonData[0]['CorrectAnswer']
    AnswerByStudent = jsonData[0]['AnswerByStudent']
    #return jsonify(jsonData)
    prompt = 'Student Age: ' + str(StudentAge) + ' ' + 'Student Grade: ' + str(StudentGrade) + ' ' + 'Source: ' + str(Source) + ' ' +'Passage Name: '+ str(PassageName) + ' ' + 'Genre: '+ str(Genre) + ' ' + 'Language Complexity: '+ str(VocabularyAndLanguageComplexity) + ' ' + 'Sentence Structure: '+ str(SentenceStructure)+ ' ' + 'Themes and Content: '+ str(ThemesAndContent) + ' ' +'Overall Complexity: '+ str(Overall) + ' ' + 'Question: '+ str(QuestionText) + ' ' +'Question Difficulty: '+ str(QuestionDifficultyDesc) + ' ' + 'Question Type:'+ str(QuestionTypeMeaning) + ' ' + 'Answer Option A: '+ str(A) + ' ' + 'Answer Option B: '+ str(B) + ' ' + 'Answer Option C: '+ str(C) + ' ' + 'Answer Option D: '+ str(D) + ' ' + 'Answer Option E: '+ str(E) + ' ' + 'Correct Answer: '+ str(CorrectAnswer) + ' ' + 'Answer By Student: '+ str(AnswerByStudent) + ' ' + 'Hour of exam: '+ str(ExamHour) + ' ' + 'Attention Level: '+ str(AttentionLevelName)
    
    #prompt = 'Source: ' + passagetype + ' Passage Name: ' + passages + ' Student Grade: ' + grade + 'Question: ' + questions + 'Hour of exam: ' + hour
    url = 'http://chattinc.com/dicey/part1'

    data = {"text": f"{prompt}"}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.post(url, json=data,headers=headers)
    jsonData = response.json()  

    if jsonData['Prediction'] == "1":
        return "Will respond well" + "<br/><br/>Prompt sent to model: " + prompt +"<br/><br/> Raw Result"+ json.dumps(jsonData)
    else:
        return "Will fail" + "<br/><br/> Prompt sent to model: " + prompt +"<br/><br/> Raw Result"+ json.dumps(jsonData)
    

@app.route('/predictpart2',methods=['GET','POST'])
def predictpart2():    
    if request.method == "POST":
        Source = request.form['passagetype']
        PassageName = request.form['passages']
        QuestionId = request.form['questions']
        StudentGrade = request.form['grade']
        ExamHour = request.form['hour']  

    if StudentGrade != '':
        if int(StudentGrade) == 3:
            StudentAge = '8'
        if int(StudentGrade) == 4:
            StudentAge = '9'
        if int(StudentGrade) == 5:
            StudentAge = '10'
        if int(StudentGrade) == 6:
            StudentAge = '11'
    else:
        StudentAge = '8'


    
    AttentionLevelName = get_attention_level(int(ExamHour))

    url = 'https://elvinatech.in/dicey/getDetails.php?Source='+Source+'&PassageName='+PassageName+'&StudentGrade='+StudentGrade+'&QuestionId='+QuestionId
    #url = 'https://elvinatech.in/dicey/getDetails.php?Source=mocktest&PassageName=notre-dame&StudentGrade=5&QuestionId=1'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url,headers=headers)
    jsonData = response.json()

    #return jsonData['Genre']
    QuestionText=jsonData[0]['QuestionText']
    Genre = jsonData[0]['Genre']
    VocabularyAndLanguageComplexity = jsonData[0]['VocabularyAndLanguageComplexity']
    SentenceStructure = jsonData[0]['SentenceStructure']
    ThemesAndContent = jsonData[0]['ThemesAndContent']
    Overall = jsonData[0]['Overall']
    QuestionDifficultyDesc = jsonData[0]['QuestionDifficulty']
    QuestionTypeMeaning = '' #jsonData[0]['QuestionTypeMeaning']
    A = jsonData[0]['A']
    B = jsonData[0]['B']
    C = jsonData[0]['C']
    D = jsonData[0]['D']
    E = jsonData[0]['E']
    CorrectAnswer = jsonData[0]['CorrectAnswer']
    AnswerByStudent = jsonData[0]['AnswerByStudent']
    #return jsonify(jsonData)
    prompt = 'Student Age: ' + str(StudentAge) + ' ' + 'Student Grade: ' + str(StudentGrade) + ' ' + 'Source: ' + str(Source) + ' ' +'Passage Name: '+ str(PassageName) + ' ' + 'Genre: '+ str(Genre) + ' ' + 'Language Complexity: '+ str(VocabularyAndLanguageComplexity) + ' ' + 'Sentence Structure: '+ str(SentenceStructure)+ ' ' + 'Themes and Content: '+ str(ThemesAndContent) + ' ' +'Overall Complexity: '+ str(Overall) + ' ' + 'Question: '+ str(QuestionText) + ' ' +'Question Difficulty: '+ str(QuestionDifficultyDesc) + ' ' + 'Question Type:'+ str(QuestionTypeMeaning) + ' ' + 'Answer Option A: '+ str(A) + ' ' + 'Answer Option B: '+ str(B) + ' ' + 'Answer Option C: '+ str(C) + ' ' + 'Answer Option D: '+ str(D) + ' ' + 'Answer Option E: '+ str(E) + ' ' + 'Correct Answer: '+ str(CorrectAnswer) + ' ' + 'Answer By Student: '+ str(AnswerByStudent) + ' ' + 'Hour of exam: '+ str(ExamHour) + ' ' + 'Attention Level: '+ str(AttentionLevelName)
    #prompt = 'Source: ' + passagetype + ' Passage Name: ' + passages + ' Student Grade: ' + grade + 'Question: ' + questions + 'Hour of exam: ' + hour
    url = 'http://chattinc.com/dicey/part2'

    data = {"text": f"{prompt}"}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.post(url, json=data,headers=headers)
    jsonData = response.json()   
    return "Expected answer from student: "+jsonData['Prediction'] + "<br/><br/>Prompt sent to model: " + prompt +"<br/><br/> Raw Result"+ json.dumps(jsonData)


def get_attention_level(hour: int):
    if hour is None:
        return 'Invalid Hour'
    if 0 <= hour <= 6:
        return 'Very low'
    elif 7 <= hour <= 8:
        return 'Low'
    elif 9 <= hour <= 11:
        return 'High'
    elif 12 <= hour <= 13:
        return 'Medium'
    elif 14 <= hour <= 16:
        return 'High'
    elif 17 <= hour <= 19:
        return 'Medium'
    elif 20 <= hour <= 21:
        return 'Low'
    elif 22 <= hour <= 23:
        return 'Very low'
    else:
        return 'Invalid Hour'

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)

