import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from model_bakery import baker

from students.models import Course, Student

def test_example():
    assert True, "Just test example"


@pytest.fixture
def client():
    return APIClient()


# @pytest.fixture
# def user():
#     return User.objects.create_user('admin')


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory



@pytest.mark.django_db
def test_course(client, student_factory, course_factory):

    student_factory(_quantity=1)
    course_factory(_quantity=1)
    cor = Course.objects.first()
    url = reverse('courses-detail', args=(cor.id,))
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == cor.id

@pytest.mark.django_db
def test_courses_list(client, student_factory, course_factory):
    student_factory(_quantity=30)
    courses = course_factory(_quantity=30)
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 30
    for i, m in enumerate(courses):
        assert m.name == response.data[i].get('name')

@pytest.mark.django_db
def test_course_id(client, course_factory):
    course_factory(_quantity=4)
    url = reverse('courses-list')
    x = Course.objects.all()
    response = client.get(url, data={'id': x[0].id})
    assert response.data[0].get('id') == x[0].id

@pytest.mark.django_db
def test_course_delete(client, course_factory):
    course_factory(_quantity=1)
    cor = Course.objects.first()
    url = reverse('courses-detail', args=(cor.id,))
    response = client.delete(url, data={'id': f'{cor.id}'})
    assert response.status_code == 204

@pytest.mark.django_db
def test_course_patch(client, course_factory):
    course_factory(_quantity=1)
    cor = Course.objects.first()
    url = reverse('courses-detail', args=(cor.id,))
    data_patch = {'name': 'XXX'}
    response = client.patch(url, data=data_patch)
    assert response.status_code == 200
    assert response.data.get('name') == data_patch.get('name')

@pytest.mark.django_db
def test_courses_name(client, course_factory):
    course_factory(_quantity=4)
    x = Course.objects.all()
    url = reverse('courses-list')
    response = client.get(url, data={'name': x[0].name})
    assert response.data[0].get('name') == x[0].name

@pytest.mark.django_db
def test_courses_post(client):
    cor = {'name': 'Course'}
    url = reverse('courses-list')
    response = client.post(url, data=cor)
    assert response.status_code == 201
    assert response.data.get('name') == cor.get('name')

