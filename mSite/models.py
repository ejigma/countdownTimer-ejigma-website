from django.db import models


class FirstPage(models.Model):
    title = models.CharField(max_length=255, null=True)
    background_color = models.CharField(max_length=20, null=True)
    opening_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
