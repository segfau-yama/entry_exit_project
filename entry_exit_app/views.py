from django.views.generic import ListView, UpdateView, TemplateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import student_location
from django.urls import reverse_lazy


class index_views(LoginRequiredMixin, ListView):
    model = student_location
    template_name = 'index.html'
    login_url = '/accounts/login/'


class update_views(LoginRequiredMixin, UpdateView):
    model = student_location
    fields = ('student', 'location')
    template_name = 'update.html'
    login_url = '/accounts/login/'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.student != self.request.user:
            raise PermissionDenied
        return obj


class test_views(TemplateView):
    template_name = 'test.html'

