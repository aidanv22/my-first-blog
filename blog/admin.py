from django.contrib import admin
from .models import Post

admin.site.register(Post)

# Register your models here.

# above we registered our model to be visible on the admin page