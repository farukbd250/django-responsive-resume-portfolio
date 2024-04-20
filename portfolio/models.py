from django.db import models
from django.utils.text import slugify


# Create your models here.
class Social(models.Model):
    name = models.CharField(max_length=20)
    icon_class = models.CharField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return f"{self.name} {self.icon_class}"
    
class Email(models.Model):
    email = models.EmailField()
    def __str__(self):
        return f"{self.email}"
class Phone(models.Model):
    phone_number = models.CharField(max_length=14)
    def __str__(self):
        return f"{self.phone_number}"
class Address(models.Model):
    address = models.CharField(max_length=140)
    def __str__(self):
        return f"{self.address}"
class Skills(models.Model):
    TYPE_CHOICES = (
    ("Technical", "Technical"),
    ("Proffesional", "Proffesional"),
)
    type = models.CharField(max_length=50,choices=TYPE_CHOICES)
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()
    def __str__(self):
        return f"{self.name}" 
class Global(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    email =  models.ManyToManyField(Email)
    phone_number =  models.ManyToManyField(Phone)
    present_address =  models.ManyToManyField(Address)
    image = models.ImageField(default=None,upload_to='profile')
    social_link = models.ManyToManyField(Social)
    def __str__(self):
        return f"{self.name}"
    
class About(models.Model):
    description = models.TextField()
    skills= models.ManyToManyField(Skills)
    file = models.FileField(upload_to="resume/")
    def __str__(self):
        return f"{self.description}" 

class Work(models.Model):
    TYPE_CHOICES = (
    ("Education", "Education"),
    ("Work", "Work"),
)
    type = models.CharField(max_length=50,choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    institute =  models.CharField(max_length=200)
    starting_date =  models.DateField()
    ending_date = models.DateField()
    description = models.TextField()
    link = models.URLField()
    def __str__(self):
        return f"{self.title} {self.institute}"     
class Service(models.Model):
    name = models.CharField( max_length=150)
    description = models.TextField()
    i_cone = models.CharField(max_length=75)
    def __str__(self):
        return f"{self.name}"
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio/")
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.ManyToManyField(Skills)
    demo_link = models.URLField()
    def __str__(self):
        return f"{self.title}"
class Review(models.Model):
    image = models.ImageField(upload_to="review_client/" )
    comment = models.TextField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=75)
    company_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.designation} {self.company_name}"



    

