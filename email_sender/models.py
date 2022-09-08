from django.db import models

# Create your models here.

class SendEmail(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email