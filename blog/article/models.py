from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField() #大量文本时使用TextField
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True) #每次更新时自动写入时间

    class Meta:
        ordering = ('-created',)# -created 表明数据应该倒序排序
    def __str__(self):
        return self.title

# Create your models here.
