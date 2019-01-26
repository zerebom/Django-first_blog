from django.db import models
from django.utils import timezone

# Create your models here.
#DBに格納する物は↓のようにmodels.Modelを継承する
class Post(models.Model):
    #先ずプロパティを宣言する
    #他のモデルへのリンク↓
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    #字数制限付きのテキストフィールド↓
    title=models.CharField(max_length=200)
    
    #字数制限なしのテキストフィールド
    text=models.TextField()
    
    
    #日付と時間のフィールド↓
    created_date=models.DateTimeField(
        default=timezone.now
    )
    published_date=models.DateTimeField(
        blank=True,null=True
    )
    #ブログを公開するメソッド↓
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title