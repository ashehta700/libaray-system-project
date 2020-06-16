from django.db import models
from django.utils import timezone


# Create your models here.  Tablesss

class Author (models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    email = models.EmailField(blank=True,null=True)
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


    
class Books (models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE ,null=True)
    headline = models.CharField(max_length=100,null=True)
    Withdrawn = models.IntegerField()
    Draft = models.TextField()
    published_date=models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.headline 
    
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})   
  

   
     
                