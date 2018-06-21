# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DateChecker(models.Model):
date1 = models.DateTimefield(black=true, null=true)
date2 = models.DateTimefield(black=true, null=true)
date3 = models.DateTimefield(black=true, null=true)
result = models.CharField(max_length=2)
