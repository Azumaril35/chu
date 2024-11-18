import datetime
from event_planner.models import Event

def add_event(name: str, start_time: datetime.datetime, end_time: datetime.datetime) -> Event:
    """
    Ajoute un évènement ou signale un conflit si nécessaire

    :param str name: nom de l'évènement
    :param datetime start_time: heure de début de l'évènement
    :param datetime end_time: heure de fin de l'évènement
    :raises ValueError: si un conflit est détecté
    :return: instance de l'évènement créé

    --------------------------------------------------------------------------------------------------------------------
    Adds an event or raises a conflict if necessary

    :param str name: name of the event
    :param datetime start_time: start time of the event
    :param datetime end_time: end time of the event
    :raises ValueError: if a conflict is detected
    :return: instance of the event created
    """
    conflicts = check_conflicts(start_time, end_time)
    
    if conflicts:
        raise ValueError("Conflicts")
    
    else:
        event = Event(name=name, start_time=start_time, end_time=end_time)
        event.save()
        return event

def list_events():
    """
    Retourne tous les événements triés par heure de début.

    :return: QuerySet des événements triés par start_time

    --------------------------------------------------------------------------------------------------------------------
    Returns all events sorted by start time.

    :return: QuerySet of events sorted by start time
    """
    return Event.objects.all().order_by('start_time')


def find_conflicts():
    """
    Cherche les événements qui entrent en conflit entre eux.

    :return: une liste de couples d'événements en conflit

    --------------------------------------------------------------------------------------------------------------------
    Finds events that have scheduling conflicts with one another.

    :return: a list of tuples of events that have scheduling conflicts
    """
    conflicts = []
    for event in Event.objects.all():
        for conflict in check_conflicts(event.start_time, event.end_time, event.id):
            conflicts.append((event, conflict))
    
    return conflicts


def check_conflicts(start_time: datetime.datetime, end_time: datetime.datetime, id: int = None) -> list:
    """
    Cherche les événements qui entrent en conflit avec un événement donné.

    :param start_time: heure de début de l'événement à tester
    :param end_time: heure de fin de l'événement à tester
    :param id: id de l'événement à exclure pour éviter une comparaison avec lui-meme

    :return: une liste des événements en conflit

    --------------------------------------------------------------------------------------------------------------------
    Retrieves a list of events that have scheduling conflicts with a specified event.

    :param start_time: start time of the event to test
    :param end_time: end time of the event to test
    :param id: id of the event to exclude to avoid comparing with itself

    :return: a list of events that have scheduling conflicts
    """

    if start_time and end_time:
        return list(Event.objects.filter(start_time__lt=end_time, end_time__gt=start_time).exclude(id=id))
    
    else:
        return None