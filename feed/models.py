from django.db import models

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    view_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField('data published')

    #choices https://docs.djangoproject.com/en/1.10/ref/models/fields/#choices
    DEVELOPMENT = 'DV'
    PERSONAL = 'PN'
    TRAVEL = 'TV'
    CATEGORY_CHOICES = (
        (DEVELOPMENT, 'development'),
        (PERSONAL, 'pensonal'),
        (TRAVEL, 'travel'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=150)
    cmt_date = models.DateTimeField('data published')

    def __str__(self):
        return self.comment


