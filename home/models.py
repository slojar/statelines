from django.db import models


GENDER_CHOICES = (
    ("male", "Male"), ("female", "Female")
)

AGE_RANGE_CHOICES = (
    ("19 - 24", "19 - 24"), ("25 - 34", "25 - 34"), ("35 - 44", "35 - 44"), ("45 & Above", "45 & Above")
)

ANNUAL_INCOME_CHOICES = (
    ("Below 1.5 Million", "Below 1.5 Million"), ("Above 1.5 Million", "Above 1.5 Million"),
    ("Above 2.5 Million", "Above 2.5 Million")
)

SURVEY_TYPE_CHOICES = (
    ("sender", "Sender"), ("courier", "Courier")
)


class Questionnaire(models.Model):
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default="male")
    age_range = models.CharField(max_length=100, choices=AGE_RANGE_CHOICES, default="19_to_24")
    annual_income = models.CharField(max_length=100, choices=ANNUAL_INCOME_CHOICES, default="below_1.5")
    survey_type = models.CharField(max_length=100, choices=SURVEY_TYPE_CHOICES, default="sender")
    intervals = models.IntegerField(default=1)
    survey = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_on}: {self.gender} - {self.age_range}"





