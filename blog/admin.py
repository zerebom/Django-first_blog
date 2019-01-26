from django.contrib import admin
from .models import Post
# Register your models here.

#モデルをAdmin画面上で見えるようにするために登録している
admin.site.register(Post)