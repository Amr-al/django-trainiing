from django.db import models
from artists.models import *
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator

    
class Album(models.Model):
    name              = models.CharField(max_length = 50,default = 'NewAlbum')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime  = models.DateTimeField(blank = False)
    artist            = models.ForeignKey(Artist,related_name = 'albums',on_delete = models.CASCADE)
    cost              = models.FloatField()
    approved          = models.BooleanField(default = False)

    class Meta:
        db_table = 'Albums'
        constraints = [
           models.CheckConstraint( name='name must not contain any special characters or numbers',check = ~models.Q(name__regex = '[1-9]') or ~models.Q(name__regex = '[., +, *, ?, ^, $, (, ), [, ], {, }, |, \]'))
        ]
    def __str__(self):
        return self.name

  #  def save(self):
   #     data = Songs.objects.filter(song_album_id = self.id)
        #if  not data:
        #    raise Exception('Album must have at least one song')
  #      return super().save()


class Songs(models.Model):

    song_album = models.ForeignKey(Album, related_name = 'songs', on_delete = models.CASCADE )
    name = models.CharField(max_length = 50, blank = True )
    image = models.ImageField(upload_to="", height_field=None, width_field=None, blank = False , null = False)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    audio = models.FileField(upload_to ="", validators=[FileExtensionValidator(allowed_extensions=["mp3","wav"])])

    def __str__(self):
        return self.name

    def save(self):
        if self.name == '':
            self.name = self.song_album.name
        return super().save()
  
    def delete(self):
        if Songs.objects.filter(song_album_id = self.song_album_id).count() == 1:
            raise Exception("can't delete all songs of an album")
        return super().delete()

