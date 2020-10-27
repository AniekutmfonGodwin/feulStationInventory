from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestSetup(APITestCase):
    def setUp(self):
        self.tank_list_url = reverse('tank')
        self.tank_detail_url = reverse('Tank_details',kwargs={"id":1})
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

