from django.contrib import admin

# Register your models here.
from kinderapp.models import CustomUser,Postupload,values,Rating,saw

admin.site.register(CustomUser)
admin.site.register(Postupload)
admin.site.register(values)
admin.site.register(Rating)
admin.site.register(saw)