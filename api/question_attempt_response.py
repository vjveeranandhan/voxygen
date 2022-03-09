from datetime import date
from flask import Blueprint,make_response,jsonify, request, render_template
from models.questions import Questions
from models.questionAttemptHdr import QuestionAttemptHdr
from models.questionAttemptResponse import QuestionAttemptResponse
from models.questionOptions import QuestionOptions
from models import db
from datetime import datetime

qust_attempt=Blueprint('qust_attempt',__name__)

# @qust_attempt.route('/question_attempt_add', methods=['POST'])
# def question_attempt_add():
#     data=request.get_json() or {}
#     print(data)
#     questions_option_id_to_question_attempt=db.session.query(question_options).get(data.get('questions_id'))
#     questions_id_to_question_attempt=db.session.query(questions).get(data.get('questions_id'))
#     questions_attempt_hdr_id_to_question_attempt=db.session.query(question_attempt_hdr).get(data.get('questions_attempt_hdr_id'))
#     if questions_id_to_question_attempt and questions_attempt_hdr_id_to_question_attempt and questions_option_id_to_question_attempt:
#         val = question_attempt_response()
#         val.from_dict(data)

#         db.session.add(val)
#         db.session.commit()
#         return make_response(jsonify({"staus":"success","data":data}),200)
#     else:
#         return make_response(jsonify({"status":"erro","message":"Invalid reference"}),400)

@qust_attempt.route('/question_attempt_all', methods=['GET'])
def fetch_all_question_attempt():
    val=db.session.query(QuestionAttemptHdr).all()
    if not val:
        return make_response(jsonify({"staus":"succes","message":"response is empty"}),200)
    else:
        data=[]
        for item in val:
            if item.to_dict() not in data:
                data.append(item.to_dict())
            # print(type(item.to_dict))
        # print(data)
        # data_new=[]
        # for item in data:
        #     if str(item['data']) not in data_new:
        #         data_new.append(str(item['data']))
        # print(data_new)
        # date_li=[]
        li=[]
        for item in data:
            datetime_str=str(item['data'])
            date_li=datetime_str.split(' ')
            if date_li[0] not in li:
                li.append(date_li[0])
        return render_template('responses.html', data=li)

# @qust_attempt.route('/question_attempt/<int:id>', methods=['DELETE'])
# def question_attempt_delete(id):
#     val = db.session.query(question_attempt_response).get(id)
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
#     else:
#         db.session.delete(val)
#         db.session.commit()
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

# @qust_attempt.route('/question_attempt/<int:id>', methods=['PUT'])
# def question_attempt_edit(id):
#     data=request.get_json() or {}
#     questions_option_id_to_question_attempt=db.session.query(question_options).get(data.get('question_option_id'))
#     questions_id_to_question_attempt=db.session.query(questions).get(data.get('questions_id'))
#     questions_attempt_hdr_id_to_question_attempt=db.session.query(question_attempt_hdr).get(data.get('questions_attempt_hdr_id'))
#     if questions_id_to_question_attempt and questions_attempt_hdr_id_to_question_attempt and questions_option_id_to_question_attempt:
#         val = db.session.query(question_attempt_response).get(id)
#         val.response_text=data.get('response_text')
#         val.question_option_id=data.get('question_option_id')
#         val.questions_id=data.get('questions_id')
#         val.questions_attempt_hdr_id=data.get('questions_attempt_hdr_id')

#         db.session.commit()     
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)
#     else:
#         return make_response(jsonify({"status":"erro","message":"Invalid reference"}),400)


@qust_attempt.route('/question_attempt/<date_string>', methods=['GET'])
def question_attempt_get_by_id(date_string):
    print(date_string)
    # val = db.session.query(question_attempt_response).get(id)
    val = db.session.query(QuestionAttemptHdr).filter(QuestionAttemptHdr.date == date_string).all()
    if not val:
        return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
    else:
        data=[]
        for item in val:
            data.append(item.to_dict())
        # print(data)
        rsp_list=[]
        for item in data:
            val = db.session.query(QuestionAttemptResponse).filter(QuestionAttemptResponse.questions_attempt_hdr_id == item['id']).all()
            # if not val:
            #     return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
            if val:
                for item in val:
                    rsp_list.append(item.to_dict())
        id_li=[]
        i = 0
        for item in rsp_list:
            if item['questions_attempt_hdr_id'] not in [x.get('id') for x in id_li]:
                id_li.append({"id":item['questions_attempt_hdr_id'],"value":i+1})
                i+=1
        # print(id_li)
        # response_list=rsp_list
        # print(response_list) 
        # question_list=[]  
        # for item1 in response_list:
            
        #     questions_obj=db.session.query(questions).filter(questions.id == item1['questions_id']).all()
        #     for item2 in questions_obj:
        #         question_list.append(item2.to_dict())
        #         item1['question']=item2.to_dict()
        # print(response_list)

        return render_template('responses_list.html', data=id_li)
        # return make_response(jsonify({"staus":"success","data":rsp_list}),200)
        # return render_template('set_question_response.html', data=data)

@qust_attempt.route('/response/<int:id>', methods=['GET'])
def response_view(id):
    val = db.session.query(QuestionAttemptResponse).filter(QuestionAttemptResponse.questions_attempt_hdr_id == id).all()
    response_li=[]
    for item in val:
        response_li.append(item.to_dict())
    for item in response_li:
        val = db.session.query(Questions).get(item['questions_id'])
        item['question']=val.question_text
    # return make_response(jsonify({"staus":"success","data":response_li}),200)
    return render_template('response_view.html', data=response_li)