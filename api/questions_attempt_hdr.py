from crypt import methods
from sre_constants import SUCCESS
from flask import Blueprint,make_response,jsonify, request
from models.questionAttemptHdr import QuestionAttemptHdr
from models import db

auth=Blueprint('question123',__name__)

@auth.route('/qstn_attempt_hdr_add', methods=['POST'])
def qstn_attempt_add():
    data=request.get_json() or {}
    val = QuestionAttemptHdr()
    val.from_dict(data)
    
    db.session.add(val)
    db.session.commit()
    return make_response(jsonify({"staus":"success","data":data}),200)

@auth.route('qst_attempt_all', methods=['GET'])
def qstn_attempt_fetch_all():
    val=db.session.query(QuestionAttemptHdr).all()
    data=[] 
    for item in val:
        data.append(item.to_dict())
    return make_response(jsonify({"status": "success", "data": data}), 200)

@auth.route('/qstn_attempt_hdr/<int:id>', methods=['PUT'])
def qstn_attempt_hdr_edit(id):
    data=request.get_json() or {}
    val = db.session.query(QuestionAttemptHdr).get(id)
    val.date=data.get('date')

    db.session.commit()     
    return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

@auth.route('/qstn_attempt_hdr/<int:id>', methods=['DELETE'])
def qstn_attempt_hdr_delete(id):
    val = db.session.query(QuestionAttemptHdr).get(id)
    db.session.delete(val)
    db.session.commit()
    return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)

@auth.route('/qstn_attempt_hdr/<int:id>', methods=['GET'])
def qstn_attempt_hdr_get(id):
    val = db.session.query(QuestionAttemptHdr).get(id)

    return make_response(jsonify({"staus":"success","data":val.to_dict()}),200)