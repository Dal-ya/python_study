from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    view_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    cmt_date = models.DateTimeField('data published')

    def __str__(self):
        return self.comment
    