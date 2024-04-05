from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    check_me_out = models.BooleanField(default=False)
    feedback_text = models.TextField()

class FeedbackData(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    problem = models.CharField(max_length=255)  # Assuming you had this field before

    # New field
    problem_text = models.TextField()

    def __str__(self):
        return self.name


class QuickFormData(models.Model):
    assignee_email = models.EmailField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    password = models.CharField(max_length=255)
