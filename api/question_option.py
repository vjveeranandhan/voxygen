from flask import Blueprint,make_response,jsonify, request
from models.questions import Questions
from models.questionOptions import QuestionOptions
from models import db

qust_opt=Blueprint('qust_opt',__name__)
@qust_opt.route('/update_option', methods=['POST'])
def update_option():
    keys=list(request.form.keys())
    key_values=[]
    ids=[]
    for item in keys:
        temp=item.split(',')
        if temp not in key_values:
            key_values.append(temp[1])
        ids.append(temp[0])
    print(key_values)
    print(ids)
    # val=db.session.query(question_options).filter(question_options.questions_to_question_optns==key_values[0]).all()

    for item,id in zip(request.form,ids):
        val = db.session.query(QuestionOptions).get(id)
        # print(request.form[item])
        val.question_options=request.form[item]
        db.session.commit()
    
    return make_response(jsonify({"staus":"success","message":"values"}),200)


# @qust_opt.route('/question_option_add', methods=['POST'])
# def question_add():
#     data=request.get_json() or {}
#     print(data)
#     reference_option_to_question=db.session.query(questions).get(data.get('questions_to_question_optns'))
#     if reference_option_to_question:
#         val = question_options()
#         val.from_dict(data)

#         db.session.add(val)
#         db.session.commit()
#         return make_response(jsonify({"staus":"success","data":data}),200)
#     else:
#         return make_response(jsonify({"status":"erro","message":"Invalid reference"}),400)

# @qust_opt.route('/question_options_all', methods=['GET'])
# def fetch_all_question_set():
#     val=db.session.query(question_options).all()
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
#     else:
#         data=[] 
#         for item in val:
#             data.append(item.to_dict())
#         return make_response(jsonify({"status": "success", "data": data}), 200)

# @qust_opt.route('/question_options/<int:id>', methods=['PUT'])
# def question_option_edit(id):
#     data=request.get_json() or {}
#     reference_option_to_question=db.session.query(questions).get(data.get('questions_to_question_optns'))
#     if reference_option_to_question:
#         data=request.get_json() or {}
#         val = db.session.query(question_options).get(id)
#         val.question_options=data.get('question_options')
#         val.questions_to_question_optns=data.get('questions_to_question_optns')

#         db.session.commit()     
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)
#     else:
#         return make_response(jsonify({"status":"erro","message":"Invalid reference"}),400)

# @qust_opt.route('/question_options/<int:id>', methods=['DELETE'])
# def question_option_delete(id):
#     val = db.session.query(question_options).get(id)
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
#     else:
#         db.session.delete(val)
#         db.session.commit()
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

# @qust_opt.route('/question_options/<int:id>', methods=['GET'])
# def question_options_get_by_id(id):
#     val = db.session.query(question_options).get(id)
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
#     else:
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)