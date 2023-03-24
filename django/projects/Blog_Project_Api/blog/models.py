from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    options = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.URLField(max_length=5000, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=options, default='draft')
    slug = models.SlugField(blank=True, unique=True)


    def __str__(self):
        return self.title


    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.count()

    @property
    def get_view_count(self):
        return self.postview_set.count()

    @property
    def get_like_count(self):
        return self.like.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="like")

    def __str__(self):
        return self.user.username




