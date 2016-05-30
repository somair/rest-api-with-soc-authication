from django.db import models

class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='notes')
    
    class Meta:
        ordering = ('created',)