from django.db import models


# makemigramtions meaning create changes and store in a file
# migrate meaning apply the pending changes create by makemigrations
# create your models here

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name