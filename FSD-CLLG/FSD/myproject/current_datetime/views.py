from django.shortcuts import render

# Create your views here.
from datetime import datetime

def get_datetime(request):
    now = datetime.now()
    print(type(now))  # Should print "<class 'datetime.datetime'>"
    return now