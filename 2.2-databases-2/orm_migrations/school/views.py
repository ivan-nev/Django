from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    students = Student.objects.prefetch_related("teachers").all()
    students1 = Student.objects.all().order_by(ordering)
    # for student in students:
    #     for techer in student.teachers.all():
    #         print(f'stud: {student}, ucit{techer}')
    context = {'object_list':students}
    print(context)
        # filter(positions__product__price__lte=600)

    return render(request, template, context)
