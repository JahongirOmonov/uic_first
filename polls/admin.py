from django.contrib import admin

# from django.apps import apps

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except:
#         pass

from .models import Category, Tag, FAQ, Post,Author,ContactUs,ContactUsRequest

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(FAQ)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(ContactUs)
admin.site.register(ContactUsRequest)