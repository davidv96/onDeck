from django.db import models

from account.models import Profile


# https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
# useful to learning related fields and how to get the many to many search/set of orgs user belonged to
class Organization(models.Model):
    members = models.ManyToManyField(Profile, related_name="organizations")
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):

    assigned_to = models.ForeignKey(
        Profile, on_delete=models.DO_NOTHING, related_name="tasks")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
