from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    suggestion = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
