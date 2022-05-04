from bdb import set_trace
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course
from django.urls import reverse


@pytest.fixture
def course_url():
    return '/api/v1/courses/'

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make('Student', **kwargs)
    return factory


@pytest.mark.django_db
def test_course_retrieve(api_client, course_url, course_factory):
    course = course_factory()

    resp = api_client.get(course_url)
    resp_json = resp.json()

    assert len(resp_json) == 1
    recieved_course = resp_json[0]
    assert course.name == recieved_course.get('name')

@pytest.mark.django_db
def test_course_list(api_client, course_url, course_factory):
    courses = course_factory(_quantity = 10)

    resp = api_client.get(course_url)
    resp_json = resp.json()

    assert len(resp_json) == 10

    given_names = [course.name for course in courses]
    recieved_names = [course.get('name') for course in resp_json]

    assert given_names == recieved_names

@pytest.mark.django_db
def test_filter_by_id(api_client, course_url, course_factory):
    courses = course_factory(_quantity = 10)
    selected_course = courses[0]

    resp = api_client.get(course_url, data={'id': selected_course.id})
    resp_json = resp.json()

    assert len(resp_json) == 1
    filtered_course = resp_json[0]
    assert selected_course.id == filtered_course.get('id')
