import pytest
from albums.serializers import AlbumSerializer, NewAlbumSerializer
from albums.models import Album
from users.models import User
from artists.models import Artist
from artists.serializers import ArtistSerializer
from authentication.serializers import RegisterSerializer


@pytest.mark.django_db
class TestSerializers:
    def test_return(self):
        albumobject = {
            'name': 'NewAlbum',
            'release_datetime': '2022-10-10 10:10:10',
            'approved': False,
            'cost': 299
        }
        album = NewAlbumSerializer(data=albumobject)
        assert album.is_valid() == True and album.data['name'] == 'NewAlbum' and album.data[
            'release_datetime'] == '2022-10-10T10:10:10Z' and album.data['approved'] == False and album.data['cost'] == 299.00

    def test_create(self):
        userdata = {
            'username': 'amr',
            'email': 'AmR@AmR.com',
            'password1': 'amr1',
            'password2': 'amr1'
        }
        user = RegisterSerializer(data=userdata)
        if user.is_valid():
            user.save()
        user = User.objects.filter(username='amr').first()
        artistdata = {
            'Stage_name': 'amr',
            'Social_link': 'https://www.youtube.com/',
            'user': user
        }
        artist = ArtistSerializer(data=artistdata)
        if artist.is_valid():
            artist.save()
       # print('GGGGGGGGGGGG' , artist.is_valid())
        artist = Artist.objects.get(Stage_name='amr')
        albumdata = {
            'name': 'NewAlbum',
            'release_datetime': '2022-10-10 10:10:10',
            'approved': False,
            'cost': 299,
            'artist': 1
        }

        album = AlbumSerializer(data=albumdata)
        if album.is_valid():
            album.save()
        album = Album.objects.get(name='NewAlbum')
        assert album.name == 'NewAlbum' and str(album.release_datetime) == '2022-10-10 10:10:10+00:00' and album.approved == False and album.cost == 299.00 and album.artist.id == artist.id and album.artist.user == user


