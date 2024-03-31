from django.contrib import admin
from django.urls import path
from CameraUI.views import persons_table_view, sighting_list_view

urlpatterns = [
    path('persons/', persons_table_view, name='persons_table'),
    path('sightings/<int:person_id>/', sighting_list_view, name='sighting_list'),
    # Другие URL-адреса вашего приложения
]
