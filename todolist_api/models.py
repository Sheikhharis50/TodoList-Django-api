from django.db import models


class todo(models.Model):

    title = models.CharField(null=True, max_length=220)
    completed = models.BooleanField(default=False, blank=True)
    created = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
