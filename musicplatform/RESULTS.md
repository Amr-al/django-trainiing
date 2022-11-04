art1 = Artist.objects.create(Stage_name = 'Amr', Social_link = 'facebook.com') 
art2 = Artist.objects.create(Stage_name = 'Ahmed', Social_link = 'facebook.com')
art3 = Artist.objects.create(Stage_name = 'CR7', Social_link = 'facebook.com')

Artist.objects.all()
<QuerySet [<Artist: Ahmed>, <Artist: Amr>, <Artist: CR7>]>

Artist.objects.all().order_by('Stage_name')
<QuerySet [<Artist: Ahmed>, <Artist: Amr>, <Artist: CR7>]>

Artist.objects.filter(Stage_name__startswith = 'A') 
<QuerySet [<Artist: Ahmed>, <Artist: Amr>]>

album = Album(name = 'album1', release_datetime = '2022-11-03 03:00:00', cost = 15.5 , artist_id = 6)
album.save() 

album2 = Album.objects.create(name = 'album2', release_datetime = '2022-11-04 16:00:00', cost = 25.5 , artist_id = 7) 

Album.objects.all().order_by('-release_datetime').first() 
<Album: Album object (2)>

Album.objects.filter(release_datetime__lt= '2022-11-03 00:00:00')
 <QuerySet []>

Album.objects.filter(release_datetime__lte= datetime.now())
<QuerySet [<Album: Album object (1)>]>

Album.objects.all().count()       
2

Album.objects.all().order_by('cost','name')
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>

for art in Album.objects.all().values_list('artist_id'):
     Album.objects.filter(artist_id = art).values('artist_id','name')
 
<QuerySet [{'artist_id': 6, 'name': 'album1'}]>
<QuerySet [{'artist_id': 7, 'name': 'album2'}]>

for art in Artist.objects.all():
     print(art.Stage_name, art.albums.all())
 
Ahmed <QuerySet [<Album: Album object (2)>]>
Amr <QuerySet [<Album: Album object (1)>]>
CR7 <QuerySet []>
