from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from Thub_Attendance import views



urlpatterns = [
    url(r'^EmployeeDailyReport/',views.EmployeeDailyReportRestCalls.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)