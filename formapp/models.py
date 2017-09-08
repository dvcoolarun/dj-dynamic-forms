# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_hstore import hstore
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.


class forms(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    data = hstore.SerializedDictionaryField()

    objects = hstore.HStoreManager()

    def get_absolute_url(self):
        return reverse('form_detail', kwargs={"pk": str(self.id)})
