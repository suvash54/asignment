from django.contrib import admin
from .models import user_data,question,imdb_data
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(imdb_data)

admin.site.register(user_data)
admin.site.register(question)

class imdb_dataAdmin(ImportExportModelAdmin):
    list_display = ['movieTitle','movieDate','movieRunTime','movieGenre','moviecerti','moviemetascore','movieDirector']
    pass

