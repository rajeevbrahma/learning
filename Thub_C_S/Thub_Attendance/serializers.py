from rest_framework import serializers
from .models import EmployeeDailyReport

class EmployeeDailyReportSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = EmployeeDailyReport
		# fields = ('title','description')
		fields = '__all__'

		