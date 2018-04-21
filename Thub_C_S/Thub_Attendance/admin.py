# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EmployeeDetails,EmployeeDailyReport

# Register your models here.
admin.site.register(EmployeeDetails)
admin.site.register(EmployeeDailyReport)

