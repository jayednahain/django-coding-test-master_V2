from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django import views
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
   template_name = 'authentication/dashboard.html'

