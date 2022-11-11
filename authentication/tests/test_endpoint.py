import pytest
from rest_framework.test import APIRequestFactory,APIClient
from users.models import User
from rest_framework import status



@pytest.mark.django_db
class TestViews:
    
    def test_register1(self):
        # Good request
        factory=APIClient()
        response=factory.post('/authentication/register/',{
            'username':'amr',
            'email':'amr@amr.com',
            'password1':'amr123',
            'password2':'amr123'
        },format='json')
        assert response.status_code==200

    def test_register2(self):
        # missing fields
        factory=APIClient()
        response=factory.post('/authentication/register/',data={
            'username':'amr',
            'email':'amr@amr.com',
            'password1':'amr'
        },format='json')
        assert response.status_code==400 

    def test_register3(self):
        # password1 != password2
        factory=APIClient()
        response=factory.post('/authentication/register/',{
            'username':'amr',
            'email':'amr@amr.com',
            'password1':'ammr11',
            'password2':'amrr12'
        },format='json')
        print(response.status_code)
        assert response.status_code==400
