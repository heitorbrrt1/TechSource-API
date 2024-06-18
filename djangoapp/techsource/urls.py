from django.urls import path
from techsource.views import index

app_name='techsource'

urlpatterns = [
    path('', index, name='index'),
]

