from django.urls import path
from comment import views

app_name="comment"

urlpatterns = [
    path('hello1', views.hello1, name='hello1'),
    path('hello2', views.hello2, name='hello2'),
]