from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Person, Sighting


def persons_table_view(request):
    query = request.GET.get('query')
    if query:
        persons = Person.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        persons = Person.objects.all()
    return render(request, 'persons_table.html', {'persons': persons})


def sighting_list_view(request, person_id):
    sightings = Sighting.objects.filter(person_id=person_id).order_by('sighting_time')
    return render(request, 'sighting_list.html', {'sightings': sightings})


def main(request):
    return render(request, 'index.html')
