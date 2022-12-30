from django.db import models

# Create your models here.
class Posts(models.Model):
    tittle = models.TextField(blank=False)
    text = models.TextField(default="New Post")
    
    def __str__(self):
        return self.tittle[0:20]

class User(models.Model):
    email = models.EmailField(null=False,blank=False,db_index=True)
    password = models.CharField(max_length=128)

class Sense(models.Model):
    activity = models.CharField(max_length=6)
    userID = models.IntegerField()
    timestamp = models.DateTimeField(blank= True, auto_now_add=True,primary_key=True)

    def __str__(self):
        active = False
        for char in self.activity:
            if char =='1':
                active = True
                break
        return str(active)+" "+str(self.timestamp.time())