from crypt import methods
from sqlalchemy import desc, null
from datetime import datetime
from flask import Blueprint,make_response,jsonify, request, render_template, flash
from models import questionOptions
from models.questions import Questions
from models.questionSet import QuestionSet
from models.referenceData import ReferenceData
from models.questionAttemptResponse import QuestionAttemptResponse
from models import db
from models.questionOptions import QuestionOptions
from models.questionAttemptHdr import QuestionAttemptHdr
qust=Blueprint('qust',__name__)

# @qust.route('/question_add', methods=['POST'])
# def question_add():
#     data=request.get_json() or {}
#     print(request.form.ge)e
#     reference_date_to_question=db.session.query(reference_date).get(data.get('reference_date_id'))
#     question_set_to_question=db.session.query(question_set).get(data.get('question_set_id'))
#     if reference_date_to_question and question_set_to_question:
#         val = questions()
#         val.from_dict(data)

#         db.session.add(val)
#         db.session.commit()
#         return make_response(jsonify({"staus":"success","data":data}),200)
#         # return render_template('add_question.html', data=data)
#     else:
#         return make_response(jsonify({"status":"erro","message":"Invalid reference date questions or question set question"}),400)

@qust.route('/question_all', methods=['GET'])
def fetch_all_question_set():
    val=db.session.query(Questions).all()
    if not val:
        return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
    else:
        data=[] 
        for item in val:
            data.append(item.to_dict())
        # return make_response(jsonify({"status": "success", "data": data}), 200)
        return render_template('all_questions.html', data=data)

@qust.route('/question/<int:id>', methods=['PUT'])
def question_set_edit(id):
    data=request.get_json() or {}
    reference_date_to_question=db.session.query(ReferenceData).get(data.get('reference_date_id'))
    question_set_to_question=db.session.query(QuestionSet).get(data.get('question_set_id'))
    if reference_date_to_question and question_set_to_question:
        data=request.get_json() or {}
        val = db.session.query(Questions).get(id)
        val.question_text=data.get('question_text')
        val.question_type=data.get('question_type')
        val.question_set_id=data.get('question_set_id')
        val.reference_date_id=data.get('reference_date_id')

        db.session.commit()     
        return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)
    else:
        return make_response(jsonify({"status":"erro","message":"Invalid reference date question set"}),400)

@qust.route('/question/<int:id>', methods=['DELETE'])
def question_delete(id):
    val = db.session.query(Questions).get(id)
    if not val:
        return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
    else:
        db.session.delete(val)
        db.session.commit()
        return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

@qust.route('/question/<int:id>', methods=['GET'])
def question_get_by_id(id):
    val = db.session.query(Questions).get(id)
    if not val:
        return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
    else:
        return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

@qust.route('/submit_feedback', methods=['POST'])
def submit():
    current_date = datetime.now().date()
    qustn_attempt = QuestionAttemptHdr()
    qustn_attempt.from_dict({
            "date":current_date
        })
    db.session.add(qustn_attempt)
    db.session.commit()
    print(current_date)
    values = db.session.query(QuestionAttemptHdr).all()

    values.sort(key=lambda x:x.id)
    val = values[-1]
    print(val.id)
    # val=db.session.query(question_attempt_hdr).filter(question_attempt_hdr.date==str(current_date)).first()
    # print(val.id)
    # print(val.date)
    # print(request.form)
    # for item in request.form:
    #     print(request.form[item])
    keys=list(request.form.keys())
    # print(keys)
    for item in request.form:
        # print(current_date)
        # print(request.form[item])
        k=item.split(',')
        print(k)
        if(len(k)>2):
            if k[2]=='MCQ':
            # print(request.form[item].keys())
                question_attempt = QuestionAttemptResponse()
                question_attempt.from_dict({
                    "response_text":request.form[item],
                    "question_option_id":k[1],
                    "questions_id": k[0],
                    "questions_attempt_hdr_id":val.id,
                })
                db.session.add(question_attempt)
                db.session.commit()
                # print("commited if")
        else:
            question_attempt = QuestionAttemptResponse()
            question_attempt.from_dict({
                "response_text":request.form[item],
                # "question_option_id":null,
                "questions_id": k[0],
                "questions_attempt_hdr_id":val.id,
            })
            db.session.add(question_attempt)
            db.session.commit()
            # print("commited else")
    return make_response(jsonify({"status":"success"}))

@qust.route('/add_question')
def add_questions():
    val=db.session.query(ReferenceData).all()
    data1=[]
    data2=[]
    data=[]
    for item in val:
        data1.append(item.to_dict())
    val2=db.session.query(QuestionSet).all()
    for item in val2:
        data2.append(item.to_dict())
    data.append(data1)
    data.append(data2)
    # return make_response(jsonify({"status":"success", "data":data}),200)
    return render_template('add_question.html', data=data)

@qust.route('/submit_question', methods=['POST'])
def submit_question():
    # print(request.form)
    if not request.form:
        return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
    for item in request.form:
        print(request.form[item])
    question_add_obj=Questions()
    question_add_obj.from_dict(
        {
            'question_text': request.form['question'],
            'question_type': request.form['question_type'],
            'question_set_id':request.form['question_set'],
            'reference_date_id':request.form['status'],
        }
    )
    db.session.add(question_add_obj)
    db.session.commit()
    val=db.session.query(Questions).filter(Questions.question_text==request.form['question'])
    print(val)
    data=[] 
    for item in val:    
        data.append(item.to_dict())
    print(data)
    if request.form['question_type']=='MCQ':
        return render_template('add_options.html', data=data)
    else:
        return make_response(jsonify({"status":"success"}))

@qust.route('/submit_option', methods=['POST'])
def submit_option():
    # print(request.form)
    # for item in request.form:
    #     print(request.form[item])
    
    key = list(request.form.keys())
    # print(dict.values())
    # print(key[0])
    for item in request.form:
        print(request.form[item])
        question_opt_obj=questionOptions()
        question_opt_obj.from_dict(
                {
                    'question_options' : request.form[item],
                    'questions_to_question_optns' : key[0], 
                })
        db.session.add(question_opt_obj)
    db.session.commit()
    return make_response(jsonify({"status":"success"}))

    

@qust.route('/activate_deactivate_delete', methods=['POST'])
def activate_deactivate_delete():
    # print(request.form)
    for item in request.form:
        # print(request.form)
        key = list(request.form.keys())
        # print(key)
        val = db.session.query(Questions).get(key)
        if request.form[item]=="Delete":
            if not val:
                return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
            else:
                db.session.delete(val)
                db.session.commit()
            
            # if
            # val = db.session.query(question_options).filter(question_options.questions_to_question_optns==key)

            return make_response(jsonify({"staus":"successfully deleted","data":val.to_dict()}),200)
        elif request.form[item]=="Edit":
            if not val:
                return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
            else:
                data=[]
                data.append(val.to_dict())
                # print(data)
                return render_template('update_question.html', data=data)
        elif request.form[item]=="Activate":
            val.reference_date_id="4"
            db.session.commit()
        elif request.form[item]=="Deactivate":
            val.reference_date_id="2"
            db.session.commit()
    return make_response(jsonify({"status":"success"}))

@qust.route('/update_question', methods=['POST'])
def update_quest_option():
    keys = list(request.form.keys())
    val=db.session.query(Questions).filter(Questions.id==keys[0])
    data=[]
    for item in val:    
        item.question_type=request.form[keys[1]]
        db.session.commit()

    if request.form[keys[1]]=='Objective':
        val=db.session.query(questionOptions).filter(questionOptions.questions_to_question_optns==keys[0]).all()
        if not val:
            return make_response(jsonify({"status":"success"}))
        else:
            for item in val:
                db.session.delete(item)
                db.session.commit()
            return make_response(jsonify({"staus":"successfully deleted options qstn updated"}),200)
            
    elif request.form[keys[1]]=='MCQ':
        val=db.session.query(questionOptions).filter(questionOptions.questions_to_question_optns==keys[0]).all()
        data=[]
        if not val:
            # print("if")
            val=db.session.query(Questions).filter(Questions.id==keys[0])
            for item in val:    
                data.append(item.to_dict())
            # print(data)
            # return make_response(jsonify({"status":"success"}))
            return render_template('add_options.html', data=data)   
        else:
            for item in val:    
                data.append(item.to_dict())
            # print(data)
            return render_template('edit_options.html', data=data)

    # print(request.form[key[1]])
    # val = db.session.query(questions).get(keys[0])
    # # # print(type(val))
    # val.question_text=request.form[keys[0]]
    # val.question_type=request.form[keys[1]]
    # val.reference_date_id=request.form[key[2]]

    # db.session.commit()

    # if request.form[key[1]]=="Objective":
    #     val = db.session.query(question_options).get(question_options.questions_to_question_optns==key[0])
    #     print(val)
    #     if(val):
    #         db.session.delete(val)
    #         db.session.commit()
    #     else:
    #         return make_response(jsonify({"staus":"success","message":"No options"}),200)
    #     # return render_template('update_question.html', data=data)
    return make_response(jsonify({"status":"success"}))
