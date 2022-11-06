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


    def test_selects_interested_role(self):
        pass
        data = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }
       
        role = JobRole(**data)
        db.session.add(role)
        db.session.commit()

        skill1_data = {
            'skill_name': "skill_name1", 
            'skill_description': "skill_description 1",
        }
       
        skill1 = Skill(**skill1_data)
        db.session.add(skill1)
        db.session.commit()

        request_body = {
                'job_role_id': 1,
                'skill_id': 1
            }
        response = self.client.post("/skills_to_jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )
            
        response = self.client.get("/skillbyrole/1")
        
        # print(f"response.json: {response.json}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,{
                'data': [{
                    'skill_deleted': False,
                    'skill_description': 'skill_description 1',
                    'skill_id': 1,
                    'skill_name': 'skill_name1'
                }]
            })


    def test_selects_interested_skill(self):

        skill1_data = {
            'skill_name': "skill_name1", 
            'skill_description': "skill_description 1",
        }
       
        skill1 = Skill(**skill1_data)
        db.session.add(skill1)
        db.session.commit()

        course1_data = {
            'course_name': "course_name1", 
            'course_description': "course_description 1",
            'course_status': "course_status 1",
            'course_type': "course_type 1",
            'course_category': "course_category 1"
        }
       
        course1 = Course(**course1_data)
        db.session.add(course1)
        db.session.commit()


        request_body = {
               'course_id': 1, 
               'skill_id': 1
            }
        response = self.client.post("/skills_to_course",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )
            
        response = self.client.get("/coursebyskill/1")
        
        print(f"response.json: {response.json}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,{
                'data': [{
                    'course_category': 'course_category 1',
                    'course_description': 'course_description 1',
                    'course_id': 1,
                    'course_name': 'course_name1',
                    'course_status': 'course_status 1',
                    'course_type': 'course_type 1'
                }]
            })



    def test_create_learning_journey(self):
        # to create role skill course that are all connected before:
        self.test_selects_interested_skill()
        request_body = {
            "staff_id": 1,
            "job_role_id": 1
        }

        response = self.client.post("/learning_journey",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        # response = self.client.get("/learning_journeys")
        print("response is: ", response.json)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'job_role_id': 1,
            'learning_journey_id': 1,
            'staff_id': 1
        })

    def test_view_learning_journey(self):
        # to create role skill course that are all connected before:
        self.test_create_learning_journey()

        response = self.client.get("/learning_journeys")

        # response = self.client.get("/learning_journeys")
        print("cccresponse is: ", response.json)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,{
                'data': [{
                    'job_role_id': 1,
                    'learning_journey_id': 1,
                    'staff_id': 1
                }]
            })

    def test_add_skills_to_learning_journey(self):
        # to create role skill course, learning journey that are all connected before:
        self.test_create_learning_journey()
        # 'learning_journey_id', 'skill_id',
        request_body = {
            "learning_journey_id": 1,
            "skill_id": 1
        }

        response = self.client.post("/learning_journey_addskill",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        response = self.client.get("/learning_journey_skills")
        print("response is: ", response.json)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
                'data': [{
                    'learning_journey_id': 1,
                    'skill_id': 1
                }]
            })

    def test_add_courses_to_learning_journey(self):
        # to create role skill course, learning journey that are all connected before:
        self.test_add_skills_to_learning_journey()
        request_body = {
            "learning_journey_id": 1,
            "course_id": 1
        }
        response = self.client.post("/learning_journey_addcourse",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        print("response is: ", response.json)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
                'course_id': '1',
                'learning_journey_id': 1
            })

# CREATE SKILL:
class TestDeleteLearningJourney(TestApp):

    def test_delete_learning_journey(self):
        data = {
            "staff_id": 1,
            "job_role_id": 1
        }

        learningjourney = LearningJourney(**data)
        db.session.add(learningjourney)
        db.session.commit()

        response = self.client.get("/learning_journeys")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,{
                'data': [{
                    'job_role_id': 1,
                    'learning_journey_id': 1,
                    'staff_id': 1
                }]
            })

        delete_request_body = {
            "learning_journey_id": 1,
        }

        response = self.client.delete("/learning_journey",
                                    data=json.dumps(delete_request_body),
                                    content_type='application/json'
                                    )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
                'learning_journey_id': 1
            })

    def test_delete_learning_journey_invalid_id(self):

        delete_request_body = {
            "learning_journey_id": 2,
        }

        response = self.client.delete("/learning_journey",
                                    data=json.dumps(delete_request_body),
                                    content_type='application/json'
                                    )

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
                'message': 'Unable to find role with id: 2.'
            })

    def test_delete_learning_journey_invalid_json(self):

        delete_request_body = {
            "learning_journey": 2,
        }

        response = self.client.delete("/learning_journey",
                                    data=json.dumps(delete_request_body),
                                    content_type='application/json'
                                    )

        self.assertEqual(response.status_code, 500)
        print(response.json)
        self.assertEqual(response.json, {
            'message': 'Incorrect JSON object provided.'
        })
                            
# CREATE SKILL:
class TestSkillsToRole(TestApp):

    # similar to above one: test_selects_interested_role
    def test_assign_skills_to_role(self):
        data = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }
       
        role = JobRole(**data)
        db.session.add(role)
        db.session.commit()

        skill1_data = {
            'skill_name': "skill_name1", 
            'skill_description': "skill_description 1",
        }
       
        skill1 = Skill(**skill1_data)
        db.session.add(skill1)
        db.session.commit()

        skill2_data = {
            'skill_name': "skill_name2", 
            'skill_description': "skill_description 2",
        }
       
        skill1 = Skill(**skill1_data)
        db.session.add(skill1)
        db.session.commit()

        request_body = {
                'job_role_id': 1,
                'skill_id': 1
            }
        response = self.client.post("/skills_to_jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )

        request_body = {
                'job_role_id': 1,
                'skill_id': 2
            }
        response = self.client.post("/skills_to_jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )
            
        response = self.client.get("/skillbyrole/1")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'data': [{
                'skill_deleted': False,
                'skill_description': 'skill_description 1',
                'skill_id': 1,
                'skill_name': 'skill_name1'
            }, {
                'skill_deleted': False,
                'skill_description': 'skill_description 1',
                'skill_id': 2,
                'skill_name': 'skill_name1'
            }]
        })

    # cannot test this?
    def test_assign_invalid_skills_to_role(self):
        data = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }
       
        role = JobRole(**data)
        db.session.add(role)
        db.session.commit()

        request_body = {
                'job_role_id': 1,
                'skill_id': None
            }
        response = self.client.post("/skills_to_jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )
        print("jons", response.json)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
                'message': 'Unable to commit to database.'
            })

    # cannot test this?
    def test_assign_invalid_0_skills_to_role(self):
        data = {
            'job_role_name': "job1", 
            'job_role_description': "job description 1",
        }
       
        role = JobRole(**data)
        db.session.add(role)
        db.session.commit()
        # shdnt be added:
        request_body = {
                'job_role_id': 1,
                'skill_id': 9
            }
        response = self.client.post("/skills_to_jobrole",
                                    data=json.dumps(request_body),
                                    content_type='application/json'
                                    )
        # print("jons", response.json)
        self.assertEqual(response.status_code, 201)
        # self.assertEqual(response.json, {
        #         'message': 'Unable to commit to database.'
        #     })

        self.assertEqual(response.json, {
            'job_role_id': 1,
            'skill_id': 9
        })



if __name__ == '__main__':
    unittest.main()