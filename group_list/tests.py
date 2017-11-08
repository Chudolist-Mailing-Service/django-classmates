from django.test import TestCase, Client

from group_list.models import Group, GroupMate

class MateTestCase(TestCase):
    def setUp(self):
        group = Group.objects.create(name='404')
        GroupMate.objects.create(
            group=group,
            name='Иван Иванов',
        )
        self.c = Client()

    def test_full_list(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_group_list(self):
        response = self.c.get('/404/')
        self.assertEqual(response.status_code, 200)

    def test_name_in_group_list(self):
        response = self.c.get('/404/')
        self.assertIn(bytes('Иван Иванов', 'utf-8'), response.content)
