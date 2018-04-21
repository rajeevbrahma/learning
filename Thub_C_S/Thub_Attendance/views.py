# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmployeeDailyReport
from .serializers import EmployeeDailyReportSerializer
# Create your views here.


class EmployeeDailyReportRestCalls(APIView):
	

	def post(self,request,format=None):

		serializer = EmployeeDailyReportSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


