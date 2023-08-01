from django.urls import path
from .views import *

app_name = 'generator'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('project/', Project.as_view(), name='project')
]
