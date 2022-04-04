from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testuser@super.com', 'boris39', 'Boris', 'password')

        self.assertEqual(super_user.email, "testuser@super.com")
        self.assertEqual(super_user.user_name, "boris39")
        self.assertEqual(super_user.first_name, "Boris")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'boris39')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',
                user_name='boris39',
                first_name='Boris',
                password='password',
                is_superuser=False
                )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',
                user_name='boris39',
                first_name='Boris',
                password='password',
                is_staff=False
                )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='',
                user_name='boris39',
                first_name='Boris',
                password='password',
                )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('testuser@user.com', 'boris39', 'Boris', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.user_name, 'boris39')
        self.assertEqual(user.first_name, 'Boris')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='',
                user_name='boris39',
                first_name='Boris',
                password='password',
                )