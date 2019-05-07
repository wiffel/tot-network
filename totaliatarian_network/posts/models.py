from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_on', )
