from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage

# Register your models here.
for x in [AccessRecord, Topic, Webpage]:
    admin.site.register(x)

# admin.site.register(AccessRecord)
# admin.site.register(Topic)
# admin.site.register(Webpage)
