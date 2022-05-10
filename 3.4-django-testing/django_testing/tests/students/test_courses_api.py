from bdb import set_trace
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course
from django.urls import reverse


@pytest.fixture
def course_url():
    def build_url(pk=None):
        if pk:
            return reverse('courses-detail', kwargs = {'pk': pk})
        return reverse('courses-list')
         
    return build_url

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
    resp = api_client.get(course_url(course.id))

    assert resp.status_code == 200

    resp_json = resp.json()
    assert course.name == resp_json.get('name')

@pytest.mark.django_db
def test_course_list(api_client, course_url, course_factory):
    courses = course_factory(_quantity = 10)

    resp = api_client.get(course_url())

    assert resp.status_code == 200

    resp_json = resp.json()
    assert len(resp_json) == 10

    given_names = [course.name for course in courses]
    recieved_names = [course.get('name') for course in resp_json]
    assert given_names == recieved_names

@pytest.mark.django_db
def test_filter_by_id(api_client, course_url, course_factory):
    courses = course_factory(_quantity = 10)
    selected_course = courses[0]

    resp = api_client.get(course_url(), data={'id': selected_course.id})

    assert resp.status_code == 200

    resp_json = resp.json()
    assert len(resp_json) == 1

    filtered_course = resp_json[0]
    assert selected_course.id == filtered_course.get('id')

@pytest.mark.django_db
def test_filter_by_name(api_client, course_url, course_factory):
    courses = course_factory(_quantity=10)
    selected_course = courses[0]
    the_same_courses_names = [course.name for course in courses if course.name == selected_course.name]

    resp = api_client.get(course_url(), data = {'name': selected_course.name})

    assert resp.status_code == 200

    resp_json = resp.json()
    assert len(the_same_courses_names) == len(resp_json)

    recieved_course_names = [course['name'] for course in resp_json]
    assert the_same_courses_names == recieved_course_names

@pytest.mark.parametrize('course_name', ['test1', 'test2', 'test3'])
@pytest.mark.django_db
def test_course_create(api_client, course_url, course_name):
    resp = api_client.post(course_url(), data={'name': course_name})

    assert resp.status_code == 201

    resp_json = resp.json()
    created_course = Course.objects.get(id=resp_json['id'])
    assert course_name == created_course.name

@pytest.mark.parametrize('new_course_name', ['updated_name1', 'updated_name2'])
@pytest.mark.django_db
def test_course_update(api_client, course_url, course_factory, new_course_name):
    course = course_factory()

    resp = api_client.patch(course_url(course.id), data = {'name': new_course_name})

    assert resp.status_code == 200

    updated_course = Course.objects.get(id=course.id)
    assert updated_course.name == new_course_name

@pytest.mark.django_db
def test_course_delete(api_client, course_url, course_factory):
    course = course_factory()

    resp = api_client.delete(course_url(course.id))

    assert resp.status_code == 204
    