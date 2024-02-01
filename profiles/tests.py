from django.test import TestCase
from .models import Profile


# Create your tests here.
class ProfileModelTest(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            name="First Name",
            phone_number="+1234567890",
            sex="M",
            birth_date="1990-01-01",
            image="path/to/image.jpg",
        )

    def test_name_content(self):
        self.assertEqual(self.profile.name, "First Name")

    def test_phone_number_content(self):
        self.assertEqual(self.profile.phone_number, "+1234567890")

    def test_image_content(self):
        self.assertEqual(self.profile.image, "path/to/image.jpg")

    def test_sex_content(self):
        self.assertEqual(self.profile.sex, "M")

    def test_birth_date_content(self):
        expected_birth_date = "1990-01-01"
        self.assertEqual(str(self.profile.birth_date), expected_birth_date)
