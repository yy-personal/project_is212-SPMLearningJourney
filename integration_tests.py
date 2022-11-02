import unittest
import flask_testing
import json
from app import app, db, Doctor, Patient


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


class TestCreateConsultation(TestApp):
    def test_create_consultation(self):
        d1 = Doctor(name='Imran', title='Dr',
                    reg_num='UKM123', hourly_rate=30)
        p1 = Patient(name='Phris Coskitt', title='HRH',
                     contact_num='+65 8888 8888', ewallet_balance=15)
        db.session.add(d1)
        db.session.add(p1)
        db.session.commit()

        request_body = {
            'doctor_id': d1.id,
            'patient_id': p1.id,
            'diagnosis': 'Itchy armpits',
            'prescription': 'Better deodrant',
            'length': 15
        }

        response = self.client.post("/consultations",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'id': 1,
            'doctor_id': 1,
            'patient_id': 2,
            'diagnosis': 'Itchy armpits',
            'prescription': 'Better deodrant',
            'charge': 7.5
        })

    def test_create_consultation_invalid_doctor(self):
        p1 = Patient(name='Hyacinth Bucket', title='Mrs',
                     contact_num='+65 8888 8888', ewallet_balance=15)
        db.session.add(p1)
        db.session.commit()

        request_body = {
            'doctor_id': p1.id,
            'patient_id': p1.id,
            'diagnosis': 'Itchy armpits',
            'prescription': 'Better deodrant',
            'length': 15
        }

        response = self.client.post("/consultations",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Doctor not valid.'
        })

    def test_create_consultation_invalid_patient(self):
        d1 = Doctor(name='Imran', title='Dr',
                    reg_num='UKM123', hourly_rate=30)
        db.session.add(d1)
        db.session.commit()

        request_body = {
            'doctor_id': d1.id,
            'patient_id': d1.id,
            'diagnosis': 'Itchy armpits',
            'prescription': 'Better deodrant',
            'length': 15
        }

        response = self.client.post("/consultations",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Patient not valid.'
        })

    def test_create_consultation_insufficient_balance(self):
        d1 = Doctor(name='Imran', title='Dr',
                    reg_num='UKM123', hourly_rate=30)
        p1 = Patient(name='Hyacinth Bucket', title='Mrs',
                     contact_num='+65 8888 8888', ewallet_balance=15)
        db.session.add(d1)
        db.session.add(p1)
        db.session.commit()

        request_body = {
            'doctor_id': d1.id,
            'patient_id': p1.id,
            'diagnosis': 'Itchy armpits',
            'prescription': 'Better deodrant',
            'length': 60
        }

        response = self.client.post("/consultations",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Patient does not have enough e-wallet funds.'
        })





if __name__ == '__main__':
    unittest.main()