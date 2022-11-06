from django.db import models

# Create your models here.
class Student(models.Model):
    GENDERS = (
        ('M' , 'Male'),
        ('F' , 'Female'),
        ('U' , 'Undisclosed')
    )
    name = models.CharField(max_length = 100)
    roll = models.IntegerField(unique = True)
    email = models.EmailField(max_length = 100 , null =True , blank = True)
    gender  = models.CharField(max_length = 1, choices = GENDERS)
    percentage = models.FloatField()
    # Provide a many-to-one relation by adding a column to the local model to hold the remote value.
    institute = models.ForeignKey('Institute' , on_delete = models.CASCADE , null = True , blank = True)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name


class Institute(models.Model):
    class InstituteType(models.TextChoices):
        COLLEGE = "College"
        HIGH_SCHOOL = "High School"

    name = models.CharField(max_length = 200)
    type_of_institute = models.CharField(max_length = 20 , choices = InstituteType.choices , default = InstituteType.COLLEGE)

    class Meta:
        verbose_name_plural = "Institutes"

    def __str__(self):
        return self.name





