import pytest
from users.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

@pytest.fixture
def fix():
    def _method(user):
        factory=APIClient()
        factory.post('/authentication/register/',{
            'username':user['username'],
            'email':user['email'],
            'password1':user['password'],
            'password2':user['password']
        },format='json')
        response=APIClient().post('/authentication/login/',{
            'username':user['username'],
            'password':user['password']
        },format='json')
        client=APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        return client
    return _method


@pytest.mark.django_db  
class TestViews:

    def test_user_view(self):
        # Not authenticated
        client=APIClient()
        response=client.get('/user/')
        assert response.status_code==401
    
    
    def test_user_view2(self):
        # Not authenticated
        client=APIClient()
        response=client.get('/user/1')
        assert response.status_code==401
    
    def test_user_view3(self,fix):
        # Authenticated
        user={
            'username':'mahmoud',
            'email':'m@m.com',
            'password':'mahmoud1',
        }
        client=fix(user)
        request=client.get('/user/1')
        assert request.status_code==200

    
    def test_user_view4(self,fix):
        # Not found
        user={
            'username':'mahmoud',
            'email':'m@m.com',
            'password':'mahmoud1',
        }
        client=fix(user)
        request=client.get('/user/2')
        assert request.status_code==404

    def test_user_view5(self,fix):
        # Authenticated and update himself
        user={
            'username':'mahmoud',
            'email':'m@m.com',
            'password':'mahmoud1',
        }
        client=fix(user)
        request=client.put('/user/1',{
            'username':'mahmoud',
            'email':'m@m.com',
            'bio':'this is bio'
        })
        assert request.status_code==200

    def test_user_view6(self,fix):
        # Authenticated but can not update others
        user={
            'username':'mahmoud',
            'email':'m@m.com',
            'password':'mahmoud1',
        }
        client=fix(user)
        APIClient().post('/authentication/register/',{
            'username':'mahmoud2',
            'email':'m@m2.com',
            'password1':'mahmoud2',
            'password2':'mahmoud2'
        },format='json')
        
        request=client.put('/user/2',{
            'username':'mahmoud',
            'email':'m@m.com',
            'bio':'this is bio'
        })
        assert request.status_code==403

