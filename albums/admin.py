from django.contrib import admin
from albums.models import *
from artists.models import *
from django.contrib.admin.options import TabularInline

# Register your models here.

# admin.site.register(Album)

#class AlbumAdminInline(TabularInline):
#        extra = 0
#        model = Album

class SongTabular(admin.TabularInline):
    extra = 0
    model = Songs

admin.site.register(Songs)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
  # inlines = (AlbumAdminInline,)
   readonly_fields = ('NumberOfApproved',)

   def NumberOfApproved(self, obj):
        return obj.NumberOfApproved()

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
     inlines = [SongTabular] 
     readonly_fields = ['creation_datetime']
     list_display = ['name', 'creation_datetime' ]
     def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["approved"].help_text = "Some help text..."
        return form


