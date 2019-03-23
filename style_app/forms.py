# -*- coding: utf-8 -*-

from django.forms import ModelForm
from style_app.models import Client

class ClientForm(ModelForm):
#fields
    class Meta:
        model = Client
        fields = '__all__'