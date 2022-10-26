from django.shortcuts import render
from django.views.generic import TemplateView

from testapp.models import Rubric


class Test(TemplateView):
    template_name = 'testapp/test.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'testapp/test.html')
    def get(self, request, *args, **kwargs):
        return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})


class GetRubric(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})
