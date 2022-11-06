import unittest
import flask_testing
import pytest
import json
from app import app, db, Doctor, Patient, LearningJourney, LearningJourneyCourse,\
Role, Staff, JobRole, Skill, JobRoleSkill, Course, SkillCourse, Registration, LearningJourneySkill



class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        # with app.app_context():
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# SAMPLE TEST CASE DONT TOUCH FOR NOW:
# @pytest.mark.skip(reason="no way of currently testing this")
# class TestCreateConsultation(TestApp):
#     def test_create_consultation(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         p1 = Patient(name='Phris Coskitt', title='HRH',
#                      contact_num='+65 8888 8888', ewallet_balance=15)
#         db.session.add(d1)
#         db.session.add(p1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': d1.id,
#             'patient_id': p1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 15
#         }

    #     response = self.client.post("/consultations",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     print(f"response.json: {response.json}")                           
    #     self.assertEqual(response.json, {
    #         'id': 2,
    #         'doctor_id': 1,
    #         'patient_id': 2,
    #         'diagnosis': 'Itchy armpits',
    #         'prescription': 'Better deodrant',
    #         'charge': 7.5
    #     })


    # def test_create_doctor(self):
    #     print("testing create doctor")

    #     request_body = {
    #         'name': "imran",
    #         'title': "dr",
    #         'reg_num': 1,
    #         'hourly_rate': 15
    #     }

    #     response = self.client.post("/doctors",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     print(f"response.json: {response.json}")                           
    #     self.assertEqual(response.json, {
    #         'hourly_rate': 15, 
    #         'id': 1, 'name': 'imran', 
    #         'reg_num': '1', 
    #         'title': 'dr'})


    # def test_create_consultation_invalid_doctor(self):
    #     p1 = Patient(name='Hyacinth Bucket', title='Mrs',
    #                  contact_num='+65 8888 8888', ewallet_balance=15)
    #     db.session.add(p1)
    #     db.session.commit()

    #     request_body = {
    #         'doctor_id': p1.id,
    #         'patient_id': p1.id,
    #         'diagnosis': 'Itchy armpits',
    #         'prescription': 'Better deodrant',
    #         'length': 15
    #     }

    #     response = self.client.post("/consultations",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 500)
    #     self.assertEqual(response.json, {
    #         'message': 'Doctor not valid.'
    #     })

#     def test_create_consultation_invalid_patient(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         db.session.add(d1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': d1.id,
#             'patient_id': d1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 15
#         }

#         response = self.client.post("/consultations",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 500)
#         self.assertEqual(response.json, {
#             'message': 'Patient not valid.'
#         })

#     def test_create_consultation_insufficient_balance(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         p1 = Patient(name='Hyacinth Bucket', title='Mrs',
#                      contact_num='+65 8888 8888', ewallet_balance=15)
#         db.session.add(d1)
#         db.session.add(p1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': d1.id,
#             'patient_id': p1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 60
#         }

#         response = self.client.post("/consultations",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 500)
#         self.assertEqual(response.json, {
#             'message': 'Patient does not have enough e-wallet funds.'
#         })




# STARTING HERE ALL OUR TEST CASES:

# CREATE SKILL:
class TestCreateSkill(TestApp):
    def test_read_skill(self):
        data = {'skill_name': 'JavaScript', 'skill_description': 'JavaScript is a lightweight interpreted programming language.'}
        skill = Skill(**data)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get("/skills")
        # print("response.json['data']:", response.json["data"])
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,{
                'data': [{
                    'skill_deleted': False,
                    'skill_description': 'JavaScript is a lightweight interpreted programming language.',
                    'skill_id': 1,
                    'skill_name': 'JavaScript'
                }]
            })
         

    def test_create_skill(self):
        request_body = {
            "skill_name": "JavaScript",
            "skill_description": "JavaScript is a lightweight interpreted programming language."
        }


        response = self.client.post("/skill",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        response = self.client.get("/skills")
        print("response is: ", response.json["data"])

        self.assertEqual(response.status_code, 200)

    def test_delete_skill(self):

        request_body = {
            "skill_name": "JavaScript",
            "skill_description": "JavaScript is a lightweight interpreted programming language."
        }


        response = self.client.post("/skill",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        # search_name = request.args.get('name')
        response = self.client.delete("/skill/1",
                                    # data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        print(f"expected response: {response.json}")
        # print("response is: ", response.json["data"])
        self.assertEqual(response.status_code, 204)

        response = self.client.get("/skills")
        self.assertEqual(response.json,  {
            'data': [{
                'skill_deleted': True,
                'skill_description': 'JavaScript is a lightweight interpreted programming language.',
                'skill_id': 1,
                'skill_name': 'JavaScript'
            }]
        })

    def test_update_skill(self):

        request_body = {
            "skill_name": "JavaScript",
            "skill_description": "JavaScript is a lightweight interpreted programming language."
        }


        response = self.client.post("/skill",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        request_body = {
            "skill_name": "JavaScript222",
            "skill_description": "JavaScript is a lightweight interpreted programming language."
        }

        # search_name = request.args.get('name')
        response = self.client.put("/skill/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        # print(f"expected response: {response.status_code}")
        # print("response is: ", response.json["data"])
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/skills")
        print(f"expected response: {response.json}")
        self.assertEqual(response.json,  {
            'data': [{
                'skill_deleted': False,
                'skill_description': 'JavaScript is a lightweight interpreted programming language.',
                'skill_id': 1,
                'skill_name': 'JavaScript'
            }]
        })

        

# CREATE SKILL:
class TestCreateJobRole(TestApp):
    def test_read_jobrole(self):
        data = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }
       
        skill = JobRole(**data)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get("/jobroles")
        # print("response.json['data']:", response.json["data"])
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,{
            'data': [{
                'job_role_deleted': False,
                'job_role_description': 'job description 1',
                'job_role_id': 1,
                'job_role_name': 'job1'
            }]
        })
                

    def test_create_jobrole(self):

        request_body = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }


        response = self.client.post("/jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'job_role_id': 1,
            'job_role_name': 'job1',
            'job_role_description': 'job description 1',
            'job_role_deleted': False
        })

    def test_delete_jobrole(self):
        
        request_body = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }

        response = self.client.post("/jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        # search_name = request.args.get('name')
        response = self.client.delete("/jobrole/1",
                                    # data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        # print(f"expected response: {response.json}")
        # print("response is: ", response.json["data"])
        self.assertEqual(response.status_code, 204)

        response = self.client.get("/skills")
        # print(f"expected response: {response.json}")
        self.assertEqual(response.json,  {'data': []})

    def test_update_jobrole(self):


        pass
        request_body = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }


        response = self.client.post("/jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )
        
        new_request_body = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }

        # search_name = request.args.get('name')
        response = self.client.put("/jobrole/1",
                                    data=json.dumps(new_request_body),
                                    content_type='application/json'
                                    )

        # print(f"expected response: {response.status_code}")
        # print("response is: ", response.json["data"])
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/jobroles")
        print(f"expected response: {response.json}")
        self.assertEqual(response.json,  {
                'data': [{
                    'job_role_deleted': False,
                    'job_role_description': 'job description 1',
                    'job_role_id': 1,
                    'job_role_name': 'job1'
                }]
            })

        
# CREATE SKILL:
class TestCreateLearningJourney(TestApp):
    def test_selects_interested_role(self):
        data = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }
       
        skill = JobRole(**data)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get("/jobroles")
        # print("response.json['data']:", response.json["data"])
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,{
            'data': [{
                'job_role_deleted': False,
                'job_role_description': 'job description 1',
                'job_role_id': 1,
                'job_role_name': 'job1'
            }]
        })


if __name__ == '__main__':
    unittest.main()