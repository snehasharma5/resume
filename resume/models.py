from django.db import models


class PeopleMessages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="no_id@xyz")
    message = models.TextField()

    def __str__(self):
        return self.name + " | " + self.email
