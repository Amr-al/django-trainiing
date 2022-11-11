import pytest
from albums.serializers import AlbumSerializer, NewAlbumSerializer
from albums.models import Album
from users.models import User
from artists.models import Artist
from artists.serializers import ArtistSerializer
from authentication.serializers import RegisterSerializer
from rest_framework.test import APIClient
from users.tests.test_endpoints import fix


@pytest.mark.django_db
class TestViews:
    def test_albums1(self):
        # get albums
        factory=APIClient()
        response=factory.get('/Albums/')
        assert response.status_code == 200

    def test_album2(self):
        # post album without authentication
        client=APIClient()
        response=client.post('/Albums/',{
            'name': 'NewAlbum',
            'release_datetime': '2022-10-10 10:10:10',
            'approved': False,
            'cost': 299,
            'artist': 1
        })
        assert response.status_code==401

    def test_album3(self,fix):
        # post album with user authentication
        user={
            'username':'mahmoud',
            'email':'m@m.com',
            'password':'mahmoud1',
        }
        client=fix(user)
        response=client.post('/Albums/',{
            'name': 'NewAlbum',
            'release_datetime': '2022-10-10 10:10:10',
            'approved': False,
            'cost': 299,
            'artist': 1
        })
        assert response.status_code==403

    def test_album4(self,fix):
        # post album with artist authentication
        user={
            'username':'mahmoud',
            'email':'m@m.com',
            'password':'mahmoud1',
        }
        client=fix(user)
      #  print(client.data)
        artist={
            'Stage_name':'mahmoud',
            'Social_link':'https://www.youtube.com/',
            'user':1
        }
        artist=ArtistSerializer(data=artist)
        if artist.is_valid():
            artist.save()
        #print(artist.data)
        response=client.post('/Albums/',{
            'name': 'NewAlbum',
            'release_datetime': '2022-10-10 10:10:10',
            'approved': False,
            'cost': 299,
            'artist': 1
        })
        assert response.status_code==200