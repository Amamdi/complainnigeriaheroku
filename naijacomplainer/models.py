from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Complainer(models.Model): 
    STATES = (
        ('Abia', 'Abia'),
        ('Abuja', 'Abuja'),
        ('Adamawa', 'Adamawa'),
        ('Akwa-Ibom', 'Akwa-Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross-River', 'Cross-River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara')
  )
    SECTOR = (
       ('Federal Government', 'Federal Government'),
       ('State Government', 'State Government'),
       ('Local Government', 'Local Government'),
       ('Private Company', 'Private Company'),
       ('Public Company', 'Public Company'),
       ('Other', 'Other'),
   )

    NATURE = (
        ('Delay of Service', 'Delay of Service'),
        ('Non compliance with Regulation', 'Non compliance with Regulation'),
        ('Demand for Bribery', 'Demand for Bribery'),
        ('Vandalism', 'Vandalism'),
        ('Unrepaired or damaged infrastructure', 'Unrepaired or damaged infrastructure '),
        ('Insecurity', 'Insecurity'),
        ('Non Payment of Salary', 'Non Payment of Salary'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(null=True)
    anonymous = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    state = models.CharField(
        max_length=20, choices=STATES,
        blank=False, null=False)
    complaintIsAgainst = models.CharField(
        max_length=100, choices=SECTOR,
        blank=False, null=True)
    natureOfComplaint = models.CharField(
        max_length=100, choices=NATURE,
        blank=False, null=True)
    complaint = models.TextField(max_length=10000, null=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    videos = models.FileField(upload_to='videos/',blank=True, null=True)

    def __str__(self):
        return self.firstname

    class Meta:  
        db_table = "complainers"
        ordering = ["-id", "-time"]


