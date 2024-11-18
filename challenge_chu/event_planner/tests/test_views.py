import datetime

from django.test import TestCase
from django.urls import reverse

from event_planner.models import Event
from event_planner.tests.test_utils import EventPlannerTestCase

class EventViewsTestCase(TestCase):

    def test_list_events_view(self):
        # Tester la liste des événements
        # Test response 200 et nom de l'évent contenu dans la réponse
        event = EventPlannerTestCase.create_event()

        url = reverse('list_events_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(event.name, response.content.decode('utf-8'))


    def test_list_events_view_with_post(self):
        # Tester la création d'événements avec une requête POST et redirection vers la page list_events_view
        url = reverse('list_events_view')
        response = self.client.post(url, {'name': 'Test Event', 'start_time': '2024-11-18 10:00:00', 'end_time': '2024-11-18 12:00:00'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url)

        # Vérifier si l'évent est créé
        event = Event.objects.get(name='Test Event')
        self.assertEqual(event.start_time, datetime.datetime(2024, 11, 18, 10, 0))
        self.assertEqual(event.end_time, datetime.datetime(2024, 11, 18, 12, 0))

        # Vérifier si l'évent est ajouté dans la liste des événements
        response = self.client.get(url)
        self.assertIn(event.name, response.content.decode('utf-8'))


    def test_list_conflicts_view(self):
        # Tester la liste des événements en conflit
        event = EventPlannerTestCase.create_event()
        response = self.client.get(reverse('list_conflicts_view'))
        self.assertEqual(response.status_code, 200)
        # Le nouvel événement ne doit pas apparaitre dans la liste des événements en conflit
        self.assertNotIn(event.name, response.content.decode('utf-8'))

    
    def test_list_conflicts_view_with_conflict(self):
        # Créer deux événements en conflit
        event = Event.objects.create(name='Test Event 1', start_time='2024-11-18 10:00:00', end_time='2024-11-18 12:00:00')
        event_2 = Event.objects.create(name='Test Event 2', start_time='2024-11-18 11:00:00', end_time='2024-11-18 11:30:00')
        response = self.client.get(reverse('list_conflicts_view'))

        self.assertEqual(response.status_code, 200)
        # Les deux événements doivent apparaitre dans la liste des événements en conflit
        self.assertIn(event.name, response.content.decode('utf-8'))
        self.assertIn(event_2.name, response.content.decode('utf-8'))