from django.test import TestCase

from event_planner.models import Event
from event_planner.tests.test_utils import EventPlannerTestCase

class EventModelTestCase(TestCase):

    def test_event_creation(self):
        # Tester la création d'un event
        event = EventPlannerTestCase.create_event()

        self.assertTrue(isinstance(event, Event))
        self.assertEqual(event.__str__(), event.name)