from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User

from groups.models import Group 
from people.models import Student

from django.core.urlresolvers import reverse, reverse_lazy

class LoginCreateAddTest(unittest.TestCase):
    username = 'test_user'
    email = 'test@test.ua'
    password = 'test_test'
    
    def setUp(self):
        self.user = User.objects.create_user(self.username, self.email, self.password)
        
    def tearDown(self):
        self.user.delete()
    
    def test_main(self):
        client = Client()        
        
        # login by usrnm
        status = client.login(username=self.username, password=self.password)
        self.assertEqual(status, True)
        
        # login by eml
        status = client.login(username=self.email, password=self.password)
        self.assertEqual(status, True)
        
        # create Group
        group_name = 'Test_Group'
        
        response = client.post(reverse('group:add'), {'name': group_name})
        self.assertEqual(response.status_code, 302)
        
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            group = None
        
        self.assertNotEqual(group, None)

        response = client.post(reverse_lazy('student:add'),
                                   {'name': 'TempStudent',
                                    'last_name': 'SomeName',
                                    'birthday_date': '1990-10-10',
                                    'student_id_card': '98765',
                                    'group': group.id })

        self.assertEqual(response.status_code, 302)
        
        try:
            student = group.groups.get(name='TempStudent')
        except Student.DoesNotExist:
            student = None
        
        self.assertNotEqual(student, None)
        
        self.assertEqual(student.birthday_date.__str__(), '1990-10-10')
        
        self.assertEqual(student.student_id_card.__str__(), '98765')
        