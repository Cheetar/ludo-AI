from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    """docstring for User."""

    #def __init__(self, arg):
    #    superUser, self).__init__()
    #    self.arg = arg
    title = models.CharField(max_length=128)
    source = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date added')
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=20000)

    def __str__(self):
        return self.title
