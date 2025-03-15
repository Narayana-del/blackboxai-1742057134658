from flask import Blueprint, request, jsonify
from models import db, Farmer, Crop

api = Blueprint('api', __name__)

@api.route('/farmers', methods=['POST'])
def add_farmer():
    data = request.json
    new_farmer = Farmer(
        agreement_no=data['agreement_no'],
        name=data['name'],
        father_name=data['father_name'],
        village=data['village'],
        district=data['district'],
        taluk=data['taluk'],
        pincode=data['pincode'],
        acres=data['acres'],
        sowing_date=data['sowing_date'],
        sowing_type=data['sowing_type'],
        crop_scheme=data['crop_scheme']
    )
    db.session.add(new_farmer)
    db.session.commit()
    return jsonify({'message': 'Farmer added successfully!'}), 201

@api.route('/farmers/<agreement_no>', methods=['GET'])
def get_farmer(agreement_no):
    farmer = Farmer.query.filter_by(agreement_no=agreement_no).first()
    if farmer:
        return jsonify({
            'agreement_no': farmer.agreement_no,
            'name': farmer.name,
            'father_name': farmer.father_name,
            'village': farmer.village,
            'district': farmer.district,
            'taluk': farmer.taluk,
            'pincode': farmer.pincode,
            'acres': farmer.acres,
            'sowing_date': farmer.sowing_date,
            'sowing_type': farmer.sowing_type,
            'crop_scheme': farmer.crop_scheme
        }), 200
    return jsonify({'message': 'Farmer not found!'}), 404
