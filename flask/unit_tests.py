import unittest

from app2 import Skill, JobRole, LearningJourney, LearningJourneySkill, LearningJourneyCourse

class TestJobRole(unittest.TestCase):
    def test_to_dict(self):
        jr1 = JobRole(job_role_name="Analyst", job_role_description="Analyse work", job_role_deleted= False)
        self.assertEqual(jr1.to_dict(), {
            'job_role_id': None, 
            'job_role_name': "Analyst",
            'job_role_description': 'Analyse work',
            'job_role_deleted': False
            }
        )

class TestSkill(unittest.TestCase):
    def test_to_dict(self):
        s1 = Skill(skill_name="JavaScript", skill_description="JavaScript is a lightweight interpreted programming language.", skill_deleted= False)
        self.assertEqual(s1.to_dict(), {
            'skill_id': None, 
            'skill_name': "JavaScript",
            'skill_description': 'JavaScript is a lightweight interpreted programming language.',
            'skill_deleted': False
            }
        )

    def test_update_skill(self):
        s1 = Skill(skill_name="JavaScript", skill_description="JavaScript is a lightweight interpreted programming language.", skill_deleted= False)
        self.assertEqual(s1.skill_name, "JavaScript")
        self.assertEqual(s1.skill_description, "JavaScript is a lightweight interpreted programming language.")
        s1.update_skill("UpdatedSkill", "UpdatedSkillDescription")
        self.assertEqual(s1.skill_name, "UpdatedSkill")
        self.assertEqual(s1.skill_description, "UpdatedSkillDescription")

        

class TestLearningJourneySkill(unittest.TestCase):
    def test_to_dict(self):
        ljs1 = LearningJourneySkill(learning_journey_id=1, skill_id=3)
        self.assertEqual(ljs1.to_dict(), {
            'learning_journey_id': 1,
            'skill_id': 3,
            }
        )

class TestLearningJourneyCourse(unittest.TestCase):
    def test_to_dict(self):
        ljc1 = LearningJourneyCourse(learning_journey_id=1, course_id="COR002")
        self.assertEqual(ljc1.to_dict(), {
            'learning_journey_id': 1, 
            'course_id': "COR002",
            }
        )

if __name__ == "__main__":
    unittest.main()