from django.test import TestCase
from .models import Goal

# Create your tests here.

class GoalTTests(TestCase):

    def setUp(self):
        self.goal_model_a = Goal.objects.create(name="New Goal", slug="slug", target_hours=5, rating=5)
        self.goal_model_b = Goal.objects.create(name="New Goal1", slug="slug-two", target_hours=5, rating=5)
    
    def test_goal_creating(self):
        self.assertEqual(Goal.objects.count(), 2)



    # MAKE TEST for target hours - must be positive integers
