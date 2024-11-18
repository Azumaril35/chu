from django.test import TestCase

from event_planner.utils import add_event, find_conflicts, list_events
from event_planner.models import Event

class EventPlannerTestCase(TestCase):

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def create_event():
        # Permet la création d'un évent sans passer par la fonction add_event qui contrôle les conflits
        event = Event.objects.create(name='Test Event', start_time='2024-11-18 10:00:00', end_time='2024-11-18 12:00:00')
        return event
    
    def test_add_event(self):
        # Test de l'ajout d'un événement sans conflit
        add_event(name='Test Event', start_time='2024-11-18 10:00:00', end_time='2024-11-18 12:00:00')
        self.assertEqual(Event.objects.count(), 1)
                
        event = Event.objects.get(name='Test Event')
        self.assertTrue(isinstance(event, Event))
        self.assertEqual(event.__str__(), event.name)


    def test_add_event_conflict(self):
        # Ajouter un évent et vérifier s'il est bien ajouté
        event = add_event(name='Test Event 1', start_time='2024-11-18 10:00:00', end_time='2024-11-18 12:00:00')
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(event.__str__(), event.name)

        # Test de l'ajout d'un événement en conflit
        with self.assertRaises(ValueError):
            add_event(name='Test Event 2', start_time='2024-11-18 11:00:00', end_time='2024-11-18 11:30:00')
        
        self.assertEqual(Event.objects.count(), 1)


    def test_list_events(self):
        # Tester la fonction list_events
        events = list_events()
        self.assertEqual(len(events), 0)

        # Créer deux événements
        event = Event.objects.create(name='Test Event 1', start_time='2024-11-18 10:00:00', end_time='2024-11-18 12:00:00')

        # Pour vérifier que la liste est triée par ordre croissant "start_time", l'event_2 doit avoir un start_time plus petit que l'event et doit apparaitre en premier dans la liste "list_events"
        event_2 = Event.objects.create(name='Test Event 2', start_time='2024-11-18 05:00:00', end_time='2024-11-18 05:30:00')

        events = list_events()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].name, event_2.name)
        self.assertEqual(events[1].name, event.name)


    def test_find_conflicts_no_conflict(self):
        # Tester la fonction find_conflicts sans conflit
        conflicts = find_conflicts()
        self.assertEqual(len(conflicts), 0)


    def test_find_conflicts_with_conflict(self):
        # Tester la fonction find_conflicts sans conflit
        conflicts = find_conflicts()
        self.assertEqual(len(conflicts), 0)

        # Créer deux événements en conflit
        event = Event.objects.create(name='Test Event 1', start_time='2024-11-18 10:00:00', end_time='2024-11-18 12:00:00')
        event_2 = Event.objects.create(name='Test Event 2', start_time='2024-11-18 11:00:00', end_time='2024-11-18 11:30:00')
        conflicts = find_conflicts()
        self.assertEqual(len(conflicts), 2)
        self.assertEqual(conflicts[0][0].name, 'Test Event 1')
        self.assertEqual(conflicts[0][1].name, 'Test Event 2')