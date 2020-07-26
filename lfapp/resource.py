from import_export import resources
from .models import imdb_data

class imdb_dataResource(resources.ModelResource):
    class meta:
        model = imdb_data