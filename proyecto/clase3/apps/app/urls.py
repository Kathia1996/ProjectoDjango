from django .conf.urls import patterns, url, include 

urlpatterns = patterns('apps.app.views',

    #nuestras urls de la aplicacion app
    url(r'^hora/$', 'hora_actual'),
    url(r'^horaAdelantada/(\d{1,2})/$', 'horas_adelantada'),

    )