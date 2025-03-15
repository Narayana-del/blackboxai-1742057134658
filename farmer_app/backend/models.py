from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agreement_no = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    village = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    taluk = db.Column(db.String(100), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    acres = db.Column(db.Float, nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    sowing_type = db.Column(db.String(50), nullable=False)
    crop_scheme = db.Column(db.String(100), nullable=False)

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    yield_qty = db.Column(db.Float, nullable=False)
    crop_amt = db.Column(db.Float, nullable=False)
