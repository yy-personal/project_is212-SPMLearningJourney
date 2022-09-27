from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/is212_example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                        'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Skill(db.model):
    __tablename__ = 'skill'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100))
    description = db.Column(db.String(100))

class Role(db.model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100))
    description = db.Column(db.String(100))
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))


db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)