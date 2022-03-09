from cgitb import html
from flask import Blueprint,make_response,jsonify, request, render_template
from models.questions import Questions
from models.questionOptions import QuestionOptions
from models import db

active_qust=Blueprint('active_qust',__name__)

@active_qust.route('/home', methods=['GET'])
def home():
    return render_template('home.html')
@active_qust.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@active_qust.route('/active_questions_for_employee', methods=['GET'])
def fetch_active_questions_for_employee():
    val=db.session.query(Questions).filter(Questions.questStatusID2RefData=='4')
    if not val:
        return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
    else:
        data=[]
        for item in val:
            options = db.session.query(QuestionOptions).filter(QuestionOptions.questionOption2Question == item.id).all()
            opt =[]
            for i in options:
                opt.append(i.to_dict())
            data.append({
                "question":item.to_dict(),
                "option": opt
            })
        print(data)
        return render_template('feedback_form.html', data=data)

@active_qust.route('/active_questions', methods=['GET'])
def fetch_active_questions():
    val=db.session.query(Questions).filter(Questions.questStatusID2RefData=='4')
    if not val:
        return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
    else:
        data=[]
        for item in val:
            data.append(item.to_dict())
        # return make_response(jsonify({"status": "success", "data": data}), 200)
        # json_data=jsonify({"data": data})
        return render_template('active_questions.html', data=data)

@active_qust.route('/inactive_questions', methods=['GET'])
def fetch_inactive_questions():
    val=db.session.query(Questions).filter(Questions.questStatusID2RefData=='2')
    if not val:
        return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
    else:
        data=[] 
        for item in val:
            data.append(item.to_dict())
        # return make_response(jsonify({"status": "success", "data": data}), 200)
        return render_template('inactive_questions.html', data=data)
        # inactive_questions.html

