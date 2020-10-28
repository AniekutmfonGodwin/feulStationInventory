from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tank.models import Tank

class TestSetup(APITestCase):
    def setUp(self):
        self.tank_list_url = reverse('tank')
        self.tank_detail_url = reverse('tank_details',args=[1])
        self.user = User.objects.create_user('test1', 'test1@thebeatles.com', 'test1234')
        self.client.force_authenticate(user=self.user)
        Tank.objects.create(**{
            "tank_name": "gg",
            "product": "maff",
            "capacity": "50000 ca",
            "owner_id": self.user
        })
        self.user_data = {
            "email":"testuser@gmail.com",
            "username":"testuser",
            "password":"12345Admin"
            
        }
        self.tank_data = {
            "tank_name": "tanking",
            "product": "maff",
            "capacity": "50000 ca"
        }
        # response = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        # self.access_token = response.data.get("access")
        # self.refresh_token = response.data.get("refresh")

        
        
        
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

