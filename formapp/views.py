# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.views.generic as generic_views
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from formapp.models import forms
from django.shortcuts import redirect

# Create your views here.

@login_required
def home(request):
    return render(request, 'formapp/home.html')


@login_required
def create_form(request):
    return render(request, 'formapp/create_form.html')


@login_required
def form_edit(request):

    forms_data = forms.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        qdict = request.POST
        form_instance = forms.objects.create(
            user_id=request.user.id, data=dict(qdict.iterlists()))
    return render(request, 'formapp/form_edit.html', {'forms_list_data': forms_data})


class FormDetailView(generic_views.DetailView):
    model = forms
