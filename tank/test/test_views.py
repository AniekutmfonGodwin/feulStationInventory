from .test_setup import TestSetup
from rest_framework import status
from django.contrib.auth.models import User









class TestViews(TestSetup):
    


    def test_user_create(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


    def test_users_list(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        resp = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + resp.data.get("access"))
        response = self.client.get("/auth/users/",format='json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_user(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        resp = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + resp.data.get("access"))
        response = self.client.get("/auth/users/me/",format='json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_username(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        resp = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + resp.data.get("access"))
        response = self.client.post("/users/set_username/",{"new_username":"newusername","current_password":self.user_data.get("password")},format='json')
        print(response.data)
        # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        return True


    def test_delete_user(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        resp = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + resp.data.get("access"))
        response = self.client.delete("/auth/users/me/",{'current_password':self.user_data.get('password')},format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            
            
            

    def test_user_login_jwt(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        response = self.client.post('/auth/jwt/create/',{'username':self.user_data["username"],'password':self.user_data["password"]}, format='json')
        self.assertTrue(response.data.get("refresh"),'refresh token generated')
        self.assertTrue(response.data.get("access"),'access token generated')
        self.assertEqual(response.status_code,status.HTTP_200_OK)




    def test_tank_list(self):
        response = self.client.get(self.tank_list_url)
        self.assertEqual(response.status_code,200)

    def test_tank_create(self):
        # unauthenticated user
        response = self.client.post(self.tank_list_url,self.tank_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

        # authenticated user
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        user = User.objects.get(username = self.user_data.get("username"))
        self.client.force_authenticate(user=user)
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

        



    def test_tank_update(self):
        resp = self.client.post("/auth/users/", {'username':self.user_data["username"],"email":self.user_data["email"],'password':self.user_data["password"],'re_password':self.user_data["password"]}, format='json')
        self.tank_data["tank_name"] = "new tank name"
        user = User.objects.get(username = self.user_data.get("username"))
        self.client.force_authenticate(user=user)
        response = self.client.put(self.tank_detail_url,self.tank_data,format='json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        

        
        





# def test_api_jwt(self):

#     url = reverse('api-jwt-auth')
#     u = user_model.objects.create_user(username='user', email='user@foo.com', password='pass')
#     u.is_active = False
#     u.save()

#     resp = self.client.post(url, {'email':'user@foo.com', 'password':'pass'}, format='json')
#     self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

#     u.is_active = True
#     u.save()

#     resp = self.client.post(url, {'username':'user@foo.com', 'password':'pass'}, format='json')
#     self.assertEqual(resp.status_code, status.HTTP_200_OK)
#     self.assertTrue('token' in resp.data)
#     token = resp.data['token']
#     #print(token)

#     verification_url = reverse('api-jwt-verify')
#     resp = self.client.post(verification_url, {'token': token}, format='json')
#     self.assertEqual(resp.status_code, status.HTTP_200_OK)

#     resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
#     self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
#     resp = client.get('/api/v1/account/', data={'format': 'json'})
#     self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
#     client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
#     resp = client.get('/api/v1/account/', data={'format': 'json'})
#     self.assertEqual(resp.status_code, status.HTTP_200_OK)




