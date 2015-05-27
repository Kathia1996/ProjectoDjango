from django.shortcuts import render, render_to_response
from datetime import datetime
import datetime

# Create your views here.

def hora_actual(request):
    ahora = datetime.now()
    return render_to_response('app/hora.html', {'hora': ahora}) 

def horas_adelantada(request, hora):
    try:
        horas = int(hora)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = horas)
    return render(request, "app/horas_adelante.html", {'hora_siguiente': dt, 'horas': horas})