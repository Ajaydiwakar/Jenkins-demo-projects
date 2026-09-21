from django.test import TestCase
from django.urls import reverse

class TaskViewTest(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Setup Jenkins", response.content)
