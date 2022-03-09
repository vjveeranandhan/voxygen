from cgitb import html
from flask import Blueprint,make_response,jsonify, request, render_template, session
from models.questions import Questions
from models.questionSet import QuestionSet
from models import db

active_qust_set=Blueprint('active_qust_set',__name__)

@active_qust_set.route('/active_question_set', methods=['GET'])
def fetch_active_questions():
    val=db.session.query(QuestionSet).filter(QuestionSet.questSetStatusID2RefData=='4')
    if not val:
        return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
    else:
        data=[]
        for item in val:
            data.append(item.to_dict())
        # return make_response(jsonify({"status": "success", "data": data}), 200)
        return render_template('active_question_set.html', data=data)

@active_qust_set.route('/inactive_question_set', methods=['GET'])
def fetch_inactive_question_set():
    val=db.session.query(QuestionSet).filter(QuestionSet.questSetStatusID2RefData=='2')
    if not val:
        return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
    else:
        data=[] 
        for item in val:
            data.append(item.to_dict())
        return render_template('inactive_question_set.html', data=data)

@active_qust_set.route('/active_question', methods=['POST'])
def active_question():  
    key=list(request.form.keys())
    # print(request.form[key[0]])
    # for item in request.form:
    #     print(request.form[item])
    val=db.session.query(Questions).filter(Questions.question2QuestionSet==key[0], Questions.questStatusID2RefData=="4")
    val2=db.session.query(QuestionSet).filter(QuestionSet.id==key[0])
    for item in val:
        item.reference_date_id="2"
        db.session.commit()
    for item in val2:
        item.reference_date_to_qstn_set="2"
        db.session.commit()
    return make_response(jsonify({"staus":"success","data":"sucess"}),200)

@active_qust_set.route('/inactive_question', methods=['POST'])
def inactive_question():  
    key=list(request.form.keys())
    # print(key)
    # for item in request.form:
    #     print(request.form[item])
    val=db.session.query(Questions).filter(Questions.question2QuestionSet==key[0], Questions.questStatusID2RefData=="2")
    val2=db.session.query(QuestionSet).filter(QuestionSet.id==key[0])
    for item in val:
        item.reference_date_id="4"
        db.session.commit()
    for item in val2:
        item.reference_date_to_qstn_set="4"
        db.session.commit()
    return make_response(jsonify({"staus":"success","data":"success"}),200)