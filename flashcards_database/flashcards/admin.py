from django.contrib import admin
from .models import Flashcard
from .models import Collection


# Register your models here.
admin.site.register(Flashcard)
admin.site.register(Collection)
