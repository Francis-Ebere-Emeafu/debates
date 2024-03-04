from django.test import TestCase
from .models import Profile, Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Junior Category")

    def test_name_content(self):
        self.assertEqual(self.category.name, "Junior Category")

    def test_str_method(self):
        self.assertEqual(
            str(self.category), "Junior Category"
        )  # Corrected typo in expected output


class ProfileModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Junior Category")
        self.profile = Profile.objects.create(
            name="John Doe",  # Corrected name for clarity
            phone_number="+1234567890",
            sex="M",
            birth_date="1990-01-01",
            image="path/to/image.jpg",
            category=self.category,
        )

    def test_name_content(self):
        self.assertEqual(self.profile.name, "John Doe")

    def test_phone_number_content(self):
        self.assertEqual(self.profile.phone_number, "+1234567890")

    def test_image_content(self):
        self.assertEqual(self.profile.image, "path/to/image.jpg")

    def test_sex_content(self):
        self.assertEqual(self.profile.sex, "M")

    def test_birth_date_content(self):
        expected_birth_date = "1990-01-01"
        self.assertEqual(str(self.profile.birth_date), expected_birth_date)

    def test_category_content(self):
        self.assertEqual(self.profile.category, self.category)

    def test_str_method(self):
        self.assertEqual(
            str(self.profile), "John Doe"
        )
