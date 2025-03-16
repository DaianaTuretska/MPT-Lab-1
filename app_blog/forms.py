# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import ClearableFileInput

from .models import ArticleImage


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ArticleImageForm(forms.ModelForm):
    image = MultipleImageField()

    class Meta:
        model = ArticleImage
        fields = "__all__"
