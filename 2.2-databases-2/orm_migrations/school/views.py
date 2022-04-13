from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    context = {'object_list': Student.objects.prefetch_related('teachers').order_by(ordering) }

    return render(request, template, context)
