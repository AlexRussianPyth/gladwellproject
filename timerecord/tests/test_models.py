from django.test import TestCase
from timerecord.models import Goal

# Create your tests here.

class GoalTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.goal_model_a = Goal.objects.create(
            name="New Goal",
            description="Totally Basic Description", 
            target_hours=5, 
            rating=5, 
            )
        cls.goal_model_b = Goal.objects.create(
            name="New Goal1", 
            description="Second Description for Goal", 
            target_hours=5, 
            rating=5)
        # TODO Unhardcode this with Faker and random mumber of models
    
    def test_goal_creating(self):
        self.assertEqual(Goal.objects.count(), 2)

    def test_goal_slug_creating(self):
        self.assertEqual(self.goal_model_a.slug, "new-goal")

    def test_goal_search(self):
        qs = Goal.objects.search("basic")
        self.assertEqual(len(qs), 1)

    # Test Querysets and Searches

    # def test_goal_positive_hours(self):
    #     test_goal = Goal.objects.create(name="Test Goal", target_hours=-12, rating=3)
    #     self. 
    # TODO TEST for target hours - must be positive integers
