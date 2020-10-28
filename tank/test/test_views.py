from .test_setup import TestSetup
from rest_framework import status
from django.contrib.auth.models import User









class TestViews(TestSetup):
    


    def test_user_create(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


    def test_users_list(self):
        # resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        # resp = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        # self.client.credentials(HTTP_AUTHORIZATION='JWT ' + resp.data.get("access"))
        response = self.client.get("/auth/users/",format='json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_user(self):
        # resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        # resp = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        # self.client.credentials(HTTP_AUTHORIZATION='JWT ' + resp.data.get("access"))
        response = self.client.get("/auth/users/me/",format='json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_username(self):
        response = self.client.post("/users/set_username/",{"new_username":"newusername","current_password":"test1234"},format='json')
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        


    def test_delete_user(self):
        response = self.client.delete("/auth/users/me/",{'current_password':"test1234"},format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            
            
            

    def test_user_login_jwt(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        response = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        self.assertTrue(response.data.get("refresh"),'refresh token generated')
        self.assertTrue(response.data.get("access"),'access token generated')
        self.assertEqual(response.status_code,status.HTTP_200_OK)




    def test_tank_list(self):
        response = self.client.get(self.tank_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    

    def test_tank_create(self):
        # unauthenticated user
        self.client.force_authenticate(user=None)
        response = self.client.post(self.tank_list_url,self.tank_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        # authenticated user
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.tank_list_url,self.tank_data,format='json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


        # invalid data
        data = {
            "bad_data": "tanking",
            "unknow": "maff",
            "capacity": "50000 ca"
        }
        
        response = self.client.post(self.tank_list_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

        



    

        

        
        





