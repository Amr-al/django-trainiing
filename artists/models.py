from django.db import models

class Artist(models.Model):
    Stage_name = models.CharField(max_length = 30, unique = True, null = False , blank = False )
    Social_link = models.URLField(max_length = 200,blank = True)
    class Meta:
        ordering = ('Stage_name',)

    def __str__(self) :
        return self.Stage_name

    def NumberOfApproved(self):
        return self.albums.all().filter(approved=True).count()

    def approved_albums(self):
        return self.albums.all().filter(approved=True).count()
