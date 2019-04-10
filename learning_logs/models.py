from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Learning topic by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        """Returns model as string"""
        return self.text


class Entry(models.Model):
    """Details about a progress in learning"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns model as string"""
        return self.text[:50] + "..." if len(self.text) >= 50 else self.text
