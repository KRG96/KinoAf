from django.urls import path

from . import views

app_name = 'film'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('kino/<int:film_id>/', views.vision, name='vision'),
]
