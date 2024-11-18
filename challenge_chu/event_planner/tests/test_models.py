from django.test import TestCase

from event_planner.forms import EventForm

class EventFormTestCase(TestCase):

    def test_event_end_time_gt_start_time(self):
        # Tester le message d'erreur si l'heure de fin est avant l'heure de début

        name = 'Test Event'
        start_time = '2024-11-18 12:00:00'
        end_time = '2024-11-18 10:00:00'

        form = EventForm(data={'name': name, 'start_time': start_time, 'end_time': end_time})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.non_field_errors(), ['L\'heure de fin doit être ultérieure à l\'heure de début.'])