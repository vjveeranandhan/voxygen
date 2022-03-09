from flask import Blueprint,make_response,jsonify, request, render_template, render_template
from models.questions import Questions
from models.referenceData import ReferenceData
from models import db
from datetime import datetime

qust_set=Blueprint('qust_set',__name__)

@qust_set.route('/question_set_add', methods=['POST'])
def question_set_add():
    data=request.get_json() or {}
    print(data)
    referenceData_value=db.session.query(ReferenceData).get(data.get('questSetStatusID2RefData'))
    if referenceData_value:
        val = Questions()
        val.from_dict(data) 
        db.session.add(val)
        db.session.commit()
        return make_response(jsonify({"staus":"success","data":data}),200)
    else:
        return make_response(jsonify({"status":"erro","message":"Invalid reference date question set"}),400)

# @qust_set.route('/question_set_all', methods=['GET'])
# def fetch_all_question_set():
#     val=db.session.query(question_set).all()
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"question set is empty"}),400)
#     else:
#         data=[] 
#         for item in val:
#             data.append(item.to_dict())
#         return make_response(jsonify({"status": "success", "data": data}), 200)

# @qust_set.route('/question_set/<int:id>', methods=['PUT'])
# def question_set_edit(id):
#     data=request.get_json() or {}
#     reference_date_to_qstn_set=db.session.query(Reference_data).get(data.get('reference_date_to_qstn_set'))
#     if reference_date_to_qstn_set:
#         data=request.get_json() or {}
#         val = db.session.query(question_set).get(id)
#         val.question_set_title=data.get('question_set_title')
#         val.effective_date=data.get('effective_date')
#         val.expiry_date=data.get('expiry_date')
#         val.qstn_created_date=data.get('qstn_created_date')
#         val.reference_date_to_qstn_set=data.get('reference_date_to_qstn_set')

#         db.session.commit()     
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)
#     else:
#         return make_response(jsonify({"status":"erro","message":"Invalid reference date question set"}),400)

# @qust_set.route('/question_set/<int:id>', methods=['DELETE'])
# def question_set_delete(id):
#     val = db.session.query(question_set).get(id)
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
#     else:
#         db.session.delete(val)
#         db.session.commit()
#         return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

# # abca
        
# @qust_set.route('/qustn_set_activate_deactivate', methods=['GET'])
# def activate_deactivate():
#     return make_response(jsonify({"staus":"success","data":"sample"}),200)

# @qust_set.route('/question_set_add', methods=['GET'])
# def question_set_add():
#     val=db.session.query(Reference_data).all()
#     data=[]
#     for item in val:
#         data.append(item.to_dict())
#     return render_template('add_question_set.html', data=data)

# @qust_set.route('/submit_question_set', methods=['POST'])
# def submit_question_set():
#     print(request.form)
#     for item in request.form:
#         print(request.form[item])
#     question_set_add_obj=question_set()
#     current_date = datetime.now().date()
#     question_set_add_obj.from_dict(
#         {
#             'question_set_title': request.form['question_set'],
#             'effective_date': request.form['effective_date'],
#             'expiry_date':request.form['expiry_date'],
#             'qstn_created_date':current_date,
#             'reference_date_to_qstn_set':request.form['refence_data'],
#         }
#     )
#     db.session.add(question_set_add_obj)
#     db.session.commit()
#     return make_response(jsonify({"staus":"success","data":"sample"}),200)

# @qust_set.route('/question_set/<int:id>', methods=['GET'])
# def question_set_get_by_id(id):
#     print(id)
#     val = db.session.query(questions).filter(questions.question_set_id == id).all()
#     if not val:
#         return make_response(jsonify({"staus":"faild","message":"Invalid id"}),400)
#     else:
#         data=[]
#         for item in val:
#             data.append(item.to_dict())
#         print(data)
#         # return make_response(jsonify({"staus":"success","data":data}),200)
#         return render_template('set_questions.html', data=data)