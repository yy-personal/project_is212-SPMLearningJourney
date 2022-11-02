from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                            '@localhost:3306/is212_example'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                               'pool_recycle': 280}
else:
    print("herrr")
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# # CREATE A users TABLE USING RAW SQL QUERY
# db.engine.execute(
#     '''
#     CREATE TABLE `Role` (
#     `role_id` int PRIMARY KEY AUTO_INCREMENT,
#     `role_name` varchar(20) NOT NULL);
#     '''
# )
  


# # CREATE A users TABLE USING RAW SQL QUERY
# db.engine.execute(
#     '''
#     CREATE TABLE `Staff` (
#         `staff_id` int PRIMARY KEY,
#         `staff_Fname` varchar(50) NOT NULL,
#         `staff_Lname` varchar(50) NOT NULL,
#         `department` varchar(50) NOT NULL,
#         `email` varchar(50) NOT NULL,
#         `role` int NOT NULL
#     );
#     '''
# )
  

CORS(app)



class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(20))
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
    role = db.Column(db.Integer , db.ForeignKey('role.id'))

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


class Skill(db.Model):
    __tablename__ = 'skill'

    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name  = db.Column(db.String(100))
    skill_description = db.Column(db.String(500))
    skill_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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
        return 

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
        print(result)
        return result

class SkillCourse(db.Model):
    __tablename__ = 'skillcourse'
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)

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
        return 


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


######## JOB ROLE ########
# Create A New Job Role (C)
@app.route("/jobrole", methods=['POST'])
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


class Doctor(Person):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    reg_num = db.Column(db.String(15))
    hourly_rate = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }

    def calculate_charges(self, num_mins):
        """
        Uses the doctor's hourly rate to determine how much
        a 'num_mins' length appointment should be charged.
        NB: an appointment shorter than 10 mins is charged
        as if it were 10 mins long.
        """
        if num_mins < 10:
            result = self.hourly_rate / 6
        else:
            result = self.hourly_rate * (num_mins / 60)
        return result


class Patient(Person):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    contact_num = db.Column(db.String(15))
    ewallet_balance = db.Column(db.Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }

    def ewallet_topup(self, amount):
        """
        Tops up a patient's e-wallet account.
        'amount' must be positive.
        """
        if amount >= 0:
            self.ewallet_balance += amount
        else:
            raise Exception("Negative topups not allowed.")

    def ewallet_withdraw(self, amount):
        """
        Withdraws an 'amount' from the patient's e-wallet if
        there is sufficient balance.
        """
        if self.ewallet_balance >= amount:
            self.ewallet_balance -= amount
        else:
            raise Exception("Unable to withdraw: insufficient balance.")


class Consultation(db.Model):
    __tablename__ = 'consultation'

    id = db.Column(db.Integer, primary_key=True)
    diagnosis = db.Column(db.String(100))
    prescription = db.Column(db.String(30))
    charge = db.Column(db.Integer)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

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


db.create_all()


@app.route("/persons/<int:person_id>")
def person_by_id(person_id):
    person = Person.query.filter_by(id=person_id).first()
    if person:
        return jsonify({
            "data": person.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Person not found."
        }), 404


@app.route("/doctors")
def doctors():
    search_name = request.args.get('name')
    if search_name:
        doctor_list = Doctor.query.filter(Doctor.name.contains(search_name))
    else:
        doctor_list = Doctor.query.all()
    return jsonify(
        {
            "data": [doctor.to_dict() for doctor in doctor_list]
        }
    ), 200


@app.route("/doctors", methods=['POST'])
def create_doctor():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('name', 'title',
                       'reg_num', 'hourly_rate')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    doctor = Doctor(**data)
    try:
        db.session.add(doctor)
        db.session.commit()
        return jsonify(doctor.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


@app.route("/patients")
def patients():
    search_name = request.args.get('name')
    if search_name:
        patient_list = Patient.query.filter(Patient.name.contains(search_name))
    else:
        patient_list = Patient.query.all()
    return jsonify(
        {
            "data": [patient.to_dict() for patient in patient_list]
        }
    ), 200


@app.route("/patients", methods=['POST'])
def create_patient():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('name', 'title',
                       'contact_num', 'ewallet_balance')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    patient = Patient(**data)
    try:
        db.session.add(patient)
        db.session.commit()
        return jsonify(patient.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


@app.route("/consultations")
def consultations():
    consultation_list = Consultation.query.all()
    return jsonify(
        {
            "data": [consultation.to_dict()
                     for consultation in consultation_list]
        }
    ), 200


@app.route("/consultations", methods=['POST'])
def create_consultation():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('doctor_id', 'patient_id',
                       'diagnosis', 'prescription', 'length')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate doctor
    doctor = Doctor.query.filter_by(id=data['doctor_id']).first()
    if not doctor:
        return jsonify({
            "message": "Doctor not valid."
        }), 500

    # (2): Compute charges
    charge = doctor.calculate_charges(data['length'])

    # (3): Validate patient
    patient = Patient.query.filter_by(id=data['patient_id']).first()
    if not patient:
        return jsonify({
            "message": "Patient not valid."
        }), 500

    # (4): Subtract charges from patient's e-wallet
    try:
        patient.ewallet_withdraw(charge)
    except Exception:
        return jsonify({
            "message": "Patient does not have enough e-wallet funds."
        }), 500

    # (4): Create consultation record
    consultation = Consultation(
        diagnosis=data['diagnosis'], prescription=data['prescription'],
        doctor_id=data['doctor_id'], patient_id=data['patient_id'],
        charge=charge
    )

    # (5): Commit to DB
    try:
        db.session.add(consultation)
        db.session.commit()
        return jsonify(consultation.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)