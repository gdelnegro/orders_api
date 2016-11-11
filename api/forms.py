# -*- coding: utf-8 -*-
# Created by Gustavo Del Negro <gustavodelnegro@gmail.com> on 11/11/16.
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from api.models import *
from django import forms


class ItemAdminForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ItemAdminForm, self).clean()
        if cleaned_data.get('catalog_price') < cleaned_data.get('retail_price'):
            raise forms.ValidationError('too large')
        return cleaned_data

    def save(self, commit=False):
        item = super(ItemAdminForm, self).save(commit=commit)
        item.save()
        item.migration_created = False
        item.save()
        return item

    class Meta:
        model = Item
        fields = "__all__"

