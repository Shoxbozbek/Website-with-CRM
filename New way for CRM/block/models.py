from django.db import models

class Navbar(models.Model):
    
    link1 = models.CharField(max_length=50)
    link2 = models.CharField(max_length=100)
    link3 = models.CharField(max_length=100)
    link4 = models.CharField(max_length=100)
    h1 = models.CharField(max_length=200)
    h2 = models.CharField(max_length=200)
    btn1 = models.CharField(max_length=100)
    btn2 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.link1
    
    
class Slayd(models.Model):
    
    image = models.ImageField()
    

class Body(models.Model):
    
    img = models.ImageField()
    title = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    text1 = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.title
    
    
class Body1(models.Model):
    
    facilis = models.CharField(max_length=200)
    
    def __str__(self):
        return self.facilis
    
class End(models.Model):
    
    picture = models.ImageField()
    card = models.CharField(max_length=100)
    card2 = models.TextField(max_length=1000)
    btn = models.CharField(max_length=80)
    
    def __str__(self):
        return self.card