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

class Sensor(models.Model):
    activity1 = models.CharField(max_length=6,default = "")
    activity2 = models.CharField(max_length=6,default = "")
    activity3 = models.CharField(max_length=6,default = "")
    activity4 = models.CharField(max_length=6,default = "")
    activity5 = models.CharField(max_length=6,default = "")
    activity6 = models.CharField(max_length=6,default = "")
    activity7 = models.CharField(max_length=6,default = "")
    activity8 = models.CharField(max_length=6,default = "")
    activity9 = models.CharField(max_length=6,default = "")
    activity10 = models.CharField(max_length=6,default = "")
    activity11 = models.CharField(max_length=6,default = "")
    activity12 = models.CharField(max_length=6,default = "")
    activity13 = models.CharField(max_length=6,default = "")
    activity14 = models.CharField(max_length=6,default = "")
    activity15 = models.CharField(max_length=6,default = "")
    activity16 = models.CharField(max_length=6,default = "")
    activity17 = models.CharField(max_length=6,default = "")
    activity18 = models.CharField(max_length=6,default = "")
    activity19 = models.CharField(max_length=6,default = "")
    activity20 = models.CharField(max_length=6,default = "")
    activity21 = models.CharField(max_length=6,default = "")
    activity22 = models.CharField(max_length=6,default = "")
    activity23 = models.CharField(max_length=6,default = "")
    activity24 = models.CharField(max_length=6,default = "")
    activity25 = models.CharField(max_length=6,default = "")
    activity26 = models.CharField(max_length=6,default = "")
    activity27 = models.CharField(max_length=6,default = "")
    activity28 = models.CharField(max_length=6,default = "")
    activity29 = models.CharField(max_length=6,default = "")
    activity30 = models.CharField(max_length=6,default = "")
    activity31 = models.CharField(max_length=6,default = "")
    activity32 = models.CharField(max_length=6,default = "")
    activity33 = models.CharField(max_length=6,default = "")
    activity34 = models.CharField(max_length=6,default = "")
    activity35 = models.CharField(max_length=6,default = "")
    activity36 = models.CharField(max_length=6,default = "")
    activity37 = models.CharField(max_length=6,default = "")
    activity38 = models.CharField(max_length=6,default = "")
    activity39 = models.CharField(max_length=6,default = "")
    activity40 = models.CharField(max_length=6,default = "")
    activity41 = models.CharField(max_length=6,default = "")
    activity42 = models.CharField(max_length=6,default = "")
    activity43 = models.CharField(max_length=6,default = "")
    activity44 = models.CharField(max_length=6,default = "")
    activity45 = models.CharField(max_length=6,default = "")
    activity46 = models.CharField(max_length=6,default = "")
    activity47 = models.CharField(max_length=6,default = "")
    activity48 = models.CharField(max_length=6,default = "")
    activity49 = models.CharField(max_length=6,default = "")
    activity50 = models.CharField(max_length=6,default = "")
    activity51 = models.CharField(max_length=6,default = "")
    activity52 = models.CharField(max_length=6,default = "")
    activity53 = models.CharField(max_length=6,default = "")
    activity54 = models.CharField(max_length=6,default = "")
    activity55 = models.CharField(max_length=6,default = "")
    activity56 = models.CharField(max_length=6,default = "")
    activity57 = models.CharField(max_length=6,default = "")
    activity58 = models.CharField(max_length=6,default = "")
    activity59 = models.CharField(max_length=6,default = "")
    activity0 = models.CharField(max_length=6,default = "")
    
    userID = models.IntegerField(db_index=True)
    time = models.CharField(max_length=13,db_index=True)

    class Meta:
        index_together = [['userID', 'time']]
