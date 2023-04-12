from django.db import models

class Account(models.Model):
    username = models.CharField(max_length = 30, default = 'Daniel')
    email = models.EmailField(blank=True)
    password = models.CharField(max_length = 50)
    password2 = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.email