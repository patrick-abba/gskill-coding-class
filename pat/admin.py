from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Product
from .models import Customer


admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Customer)

