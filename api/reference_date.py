from crypt import methods
from flask import Blueprint,make_response,jsonify, request, render_template
from models.referenceData import ReferenceData
from models import db

ref= Blueprint('ref', __name__)

@ref.route('/add_reference_data', methods=['POST'])
def add_reference_date():
    data=request.get_json() or {}
    val = ReferenceData()
    val.from_dict(data)

    db.session.add(val)
    db.session.commit()
    return make_response(jsonify({"status":"success", "data":val.to_dict()}),200)

@ref.route('/reference_data_all', methods=['GET'])
def reference_date_fetch_all():
    val=db.session.query(ReferenceData).all()
    data=[]
    for item in val:
        data.append(item.to_dict())
    # return make_response(jsonify({"status":"success", "data":data}),200)
    return render_template('reference_data.html', data=data)

@ref.route('/reference_data/<int:id>', methods=['PUT'])
def reference_date_edit(id):
    data=request.get_json() or {}
    val=db.session.query(ReferenceData).get(id)
    val.code=data.get('code')
    val.value=data.get('value')

    db.session.commit()
    return make_response(jsonify({"status":"success","data":val.to_dict()}), 200)

@ref.route('/reference_data/<int:id>', methods=['DELETE'])
def reference_date_delete(id):
    val=db.session.query(ReferenceData).get(id)
    db.session.delete(val)
    db.session.commit()

    return make_response(jsonify({"status":"success","data":val.to_dict()}), 200)

@ref.route('/reference_data/<int:id>', methods=['GET'])
def reference_date_get(id):
    val=db.session.query(ReferenceData).get(id)

    return make_response(jsonify({"status":"success","data":val.to_dict()}), 200)
