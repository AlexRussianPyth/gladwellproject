from django.test import TestCase
from timerecord.models import Goal

# Create your tests here.

class GoalTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.goal_model_a = Goal.objects.create(name="New Goal", target_hours=5, rating=5)
        cls.goal_model_b = Goal.objects.create(name="New Goal1", target_hours=5, rating=5)
        # TODO Unhardcode this with Faker and random mumber of models
    
    def test_goal_creating(self):
        self.assertEqual(Goal.objects.count(), 2)

    def test_goal_slug_creating(self):
        self.assertEqual(self.goal_model_a.slug, "new-goal")

    # def test_goal_positive_hours(self):
    #     test_goal = Goal.objects.create(name="Test Goal", target_hours=-12, rating=3)
    #     self. 
    # MAKE TEST for target hours - must be positive integers
