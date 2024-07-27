from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  passport = models.ImageField(upload_to='passports/', blank=True, verbose_name="Passport (Photo)")
  type = models.TextField(choices=(("student", "Student"), ("lecturer", "Lecturer")), default="student")
  hall = models.TextField(blank=True, null=True)
  faculty = models.TextField(blank=True, null=True) 
  
  def __str__(self):
      return self.username
    
  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"
    
class Porter(models.Model): 
  name = models.TextField()
  image = models.ImageField(upload_to='porter/')
  hall = models.TextField()
  is_admin = models.BooleanField()

class Evaluation(models.Model): 
  timeliness = models.TextField()
  classroom_management = models.TextField()
  ethical_values = models.TextField()
  teaching_style = models.TextField()
  effective_assessments = models.TextField()
  student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='evaluations')
  porter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)