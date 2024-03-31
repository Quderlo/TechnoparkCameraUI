from django.shortcuts import render, get_object_or_404
from .models import Person, Sighting


def persons_table_view(request):
    persons = Person.objects.all()
    return render(request, 'persons_table.html', {'persons': persons})


def sighting_list_view(request, person_id):
    sightings = Sighting.objects.filter(person_id=person_id).order_by('sighting_time')
    return render(request, 'sighting_list.html', {'sightings': sightings})
