from django.test import TestCase
from django.contrib.auth import get_user_model
from newspaper_app.forms import (
    NewspaperForm,
    RedactorCreationForm,
    RedactorExperienceUpdateForm,
    RedactorUpdateDataForm,
    NewspaperSearchForm,
)


class RedactorCreationFormTest(TestCase):
    def test_redactor_creation_form_valid(self):
        data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "years_of_experience": 5,
            "first_name": "Test",
            "last_name": "User",
        }
        form = RedactorCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_redactor_creation_form_invalid(self):
        data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "years_of_experience": -5,
            "first_name": "Test",
            "last_name": "User",
        }
        form = RedactorCreationForm(data=data)
        self.assertFalse(form.is_valid())


class RedactorExperienceUpdateFormTest(TestCase):
    def test_redactor_experience_update_form_valid(self):
        data = {
            "years_of_experience": 5,
        }
        form = RedactorExperienceUpdateForm(data=data)
        self.assertTrue(form.is_valid())


class RedactorUpdateDataFormTest(TestCase):
    def test_redactor_update_data_form_valid(self):
        data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "years_of_experience": 5,
        }
        form = RedactorUpdateDataForm(data=data)
        self.assertTrue(form.is_valid())

    def test_redactor_update_data_form_invalid(self):
        data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "invalidemail",
            "years_of_experience": -5,
        }
        form = RedactorUpdateDataForm(data=data)
        self.assertFalse(form.is_valid())


class NewspaperSearchFormTest(TestCase):
    def test_newspaper_search_form_valid(self):
        data = {
            "title": "Test",
        }
        form = NewspaperSearchForm(data=data)
        self.assertTrue(form.is_valid())