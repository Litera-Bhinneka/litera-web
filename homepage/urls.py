from django.urls import path
from homepage.views import show_homepage, submit_feedback, show_json

app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('json/', show_json, name='show_json'), 
]