# -*- coding: utf-8 -*
from django import forms
from django.forms import ModelForm
from feedbacks.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


