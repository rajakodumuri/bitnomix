from django.contrib import admin

from store.models import Categories, Authors, Books

# Register your models here.

# Categories model
admin.site.register(Categories)

# Authors model
admin.site.register(Authors)

# Books model
admin.site.register(Books)
