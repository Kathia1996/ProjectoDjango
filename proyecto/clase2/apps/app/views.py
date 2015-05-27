from django.shortcuts import render, render_to_response
from datetime import datetime

# Create your views here.

def hora_actual(request):
    ahora = datetime.now()
    return render_to_response('app/hora.html', {'hora': ahora}) 