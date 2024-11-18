import datetime
from django.shortcuts import redirect, render
from django.contrib import messages

from event_planner.forms import EventForm
from event_planner.utils import add_event, list_events, find_conflicts

def list_events_view(request):
    """
    Vue pour la page d'accueil qui affiche la liste des événements.

    Si la requête est de type POST, elle tente d'ajouter un événement à la base de données si celui-ci n'est pas en conflit avec d'autres événements.
    Si la requête est de type GET, elle affiche la liste des événements.
    --------------------------------------------------------------------------------------------------------------------
    Home Page View: A page that presents a list of events.

    If the request is of type POST, it attempts to insert an event into the database, provided it does not have conflicts with other events. If the request is of type GET, it displays the list of events
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            try:
                add_event(name, start_time, end_time)
                # Redirect to the main page after adding the event // prevent form resubmission
                messages.success(request, "Evénement ajouté avec succès.")
                return redirect('list_events_view')
            except ValueError:
                messages.error(request, "L'événement que vous souhaitez ajouter est en confit avec d'autres événements.")

    else:
        form = EventForm()
        
    events = list_events()

    context = {
        'events' : events,
        'form' : form
    }

    return render(request, 'events_list.html', context)

def list_conflicts_view(request):
    """
    Vue pour la page des conflits qui affiche la liste des événements qui entrent en conflit entre eux.
    --------------------------------------------------------------------------------------------------------------------
    Conflict Resolution View: A page that presents a list of events that have scheduling conflicts with one another.
    """    
    conflicts = find_conflicts()
    
    context = {
        'conflicts' : conflicts
    }

    return render(request, 'conflicts_list.html', context)