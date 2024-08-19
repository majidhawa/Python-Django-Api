from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    teachers_id = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    subject_specialization = models.CharField(max_length = 20)
    years_of_experience = models.IntegerField()
    office_hours = models.IntegerField()
    biography = models.TextField()
    course_taught = models.CharField(max_length = 20)
    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
