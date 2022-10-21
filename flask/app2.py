from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# Mac user ====================================================================
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/ljms'
# =============================================================================


# Windows user -------------------------------------------------------------------
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:' + \
#                                         '@localhost:3306/ljms'
# --------------------------------------------------------------------------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    title = db.Column(db.String(10))

    __mapper_args__ = {
        'polymorphic_identity': 'person'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100))
    #description = db.Column(db.String(500))

    __mapper_args__ = {
        'polymorphic_identity': 'role'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        print(result)
        return result

class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, primary_key=True)
    staff_Fname  = db.Column(db.String(50))
    staff_Lname  = db.Column(db.String(50))
    department  = db.Column(db.String(50))
    email  = db.Column(db.String(50))
    role = db.Column(db.Integer , db.ForeignKey('role.role_id'))

    __mapper_args__ = {
        'polymorphic_identity': 'staff'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        print(result)
        return result


class JobRole(db.Model):
    __tablename__ = 'jobrole'

    job_role_id = db.Column(db.Integer, primary_key=True)
    job_role_name = db.Column(db.String(100))
    job_role_description = db.Column(db.String(500))
    job_role_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'jobrole'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class JobRoleSkill(db.Model):
    __tablename__ = 'jobroleskill'
    job_role_id = db.Column(db.Integer, db.ForeignKey('jobrole.job_role_id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'), primary_key=True)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Skill(db.Model):
    __tablename__ = 'skill'

    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name  = db.Column(db.String(100))
    skill_description = db.Column(db.String(500))
    skill_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'skill',
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    course_description = db.Column(db.String(100))
    course_status = db.Column(db.String(15))
    course_type = db.Column(db.String(10))
    course_category = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'course',
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Registration(db.Model):
    __tablename__ = 'registration'

    reg_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(20), db.ForeignKey('course.course_id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))
    reg_status = db.Column(db.String(20))
    completion_status = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_identity': 'registration',
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class LearningJourney(db.Model):
    __tablename__ = 'learningjourney'

    learning_journey_id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))
    job_role_id = db.Column(db.Integer , db.ForeignKey('jobrole.job_role_id'))

    __mapper_args__ = {
        'polymorphic_identity': 'learningjourney',
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class LearningJourneySkill(db.Model):
    __tablename__ = 'learningjourneyskill'
    learning_journey_id = db.Column(db.Integer, db.ForeignKey('learningjourney.learning_journey_id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'), primary_key=True)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class LearningJourneyCourse(db.Model):
    __tablename__ = 'learningjourneycourse'
    learning_journey_id = db.Column(db.Integer, db.ForeignKey('learningjourney.learning_journey_id'), primary_key=True)
    course_id = db.Column(db.String(20), db.ForeignKey('course.course_id'), primary_key=True)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result



######## SKILLS ########
#create skills (C)
@app.route('/skill' , methods=['POST'])
def create_skill():
    data = request.get_json()
    # print(data)
    if not all(key in data.keys() for
            key in ('skill_name', 'skill_description',
                    )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    skill = Skill(**data)
    try:
        db.session.add(skill)
        db.session.commit()
        return jsonify(skill.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# Read Existing Skills (R)
@app.route("/skills")
def read_skill():
    skillList = Skill.query.all()
    return jsonify(
        {
            "data": [skill.to_dict()
                    for skill in skillList]
        }
    ), 200

# Update Existing Skills (U)
@app.route("/skill/<int:id>", methods=['PUT'])
def update_skill(id):
    chosenSkill = Skill.query.filter_by(skill_id=id).first()
    if chosenSkill:
        data = request.get_json() 
        if data['skill_name']:
            chosenSkill.name = data['skill_name']
        if data['skill_description']:
            chosenSkill.description = data['skill_description']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                # "data": chosenSkill.json()
            }
        )

#delete skills (D)
#SOFT DELETE
@app.route("/skill/<int:id>", methods=['DELETE'])
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    skill.skill_deleted = True
    db.session.commit()
    return '', 204

#HARD DELETE
# @app.route("/skill", methods=['DELETE'])
# def delete_skill():
#     data = request.get_json()
#     if not all(key in data.keys() for
#                 # only allows two or more inputs in tuple during checking
#             key in ("skill_id", "skill_id")):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500

#     try:
#         try:
#             skill = Skill.query.filter_by(skill_id=data["skill_id"]).one()
#         except Exception:
#             return jsonify({
#             "message": f"Unable to find skill with id: {data['skill_id']}"
#             }), 500
#         db.session.delete(skill)
#         db.session.commit()
#         return jsonify(data), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500

######## ROLES ########
# Create A New Job Role (C)
@app.route('/jobrole' , methods=['POST'])
def create_role():
    data = request.get_json()
    print(data)
    if not all(key in data.keys() for
            key in ('job_role_name', 'job_role_description',
                    )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    jobrole = JobRole(**data)
    try:
        db.session.add(jobrole)
        db.session.commit()
        return jsonify(jobrole.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# Read Existing Roles (R)
@app.route("/jobroles")
def read_role():
    roleList = JobRole.query.all()
    return jsonify(
        {
            "data": [role.to_dict()
                    for role in roleList]
        }
    ), 200

# Update Existing Roles (U)
@app.route("/jobrole/<int:id>", methods=['PUT'])
def update_role(id):
    chosenRole = JobRole.query.filter_by(job_role_id=id).first()
    if chosenRole:
        data = request.get_json() 
        if data['job_role_name']:
            chosenRole.job_role_name = data['job_role_name']
        if data['job_role_description']:
            chosenRole.job_role_description = data['job_role_description']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                # "data": chosenRole.json()
            }
        )

# Delete An Existing Job Role (D)
#SOFT DELETE
@app.route("/jobrole/<int:id>", methods=['DELETE'])
def delete_role(id):
    jobrole = JobRole.query.get_or_404(id)
    jobrole.job_role_deleted = True
    db.session.commit()
    return '', 204

#HARD DELETE
# @app.route('/jobrole', methods=['DELETE'])
# def delete_role():
#     data = request.get_json()
#     print(data)
#     if not all(key in data.keys() for
#             key in ('job_role_id', 'job_role_id')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500
#     try:
#         try:
#             role = JobRole.query.filter_by(job_role_id=data["job_role_id"]).one()
#         except Exception:
#             return jsonify({
#                 "message": f"Unable to find role with id: {data['job_role_id']}."
#             }), 500
#         db.session.delete(role)
#         db.session.commit()

#         return jsonify(data), 201
#     except Exception:
#             return jsonify({
#                 "message": "Unable to commit to database."
#             }), 500



######## COURSES ########
# Read Courses (R)
@app.route("/courses")
def read_course():
    courseList = Course.query.all()
    return jsonify(
        {
            "data": [course.to_dict()
                    for course in courseList]
        }
    ), 200

######## Learning Journey ########
# Get all Learning Journey 
@app.route("/learning_journies")
def get_learning_journey():
    learning_journey_List = LearningJourney.query.all()
    return jsonify(
        {
            "data": [learning_journey.to_dict()
                    for learning_journey in learning_journey_List]
        }
    ), 200

# Get all Learning Journey Skill R/S
@app.route("/learning_journey_skills")
def get_learning_journey_skill():
    learning_journey_skill_List = LearningJourneySkill.query.all()
    return jsonify(
        {
            "data": [learning_journey_skill.to_dict()
                    for learning_journey_skill in learning_journey_skill_List]
        }
    ), 200

######## JOBROLESKILL ########
# add skils to jobrole 
@app.route("/skills_to_jobrole", methods=['POST'])
def add_skill_to_jobrole():
    data = request.get_json()
    print(data)
    if not all(key in data.keys() for
            key in ('job_role_id', 'skill_id',
                    )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    jobrole_skill = JobRoleSkill(**data)
    try:
        db.session.add(jobrole_skill)
        db.session.commit()
        return jsonify(jobrole_skill.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

#get all the skills from that role
@app.route("/skills_to_jobrole")
def get_skills_from_jobrole():
    jobrole_skills_List = JobRoleSkill.query.all()
    return jsonify(
        {
            "data": [jobrole_skills.to_dict()
                    for jobrole_skills in jobrole_skills_List]
        }
    ), 200


db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)