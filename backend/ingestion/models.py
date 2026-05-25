from django.db import models

class Company(models.Model):

    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ActivityRecord(models.Model):

    company=models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source=models.CharField(max_length=50)

    category=models.CharField(max_length=100)

    quantity=models.FloatField()

    unit=models.CharField(max_length=20)

    scope=models.CharField(max_length=20)

    suspicious=models.BooleanField(
        default=False
    )

    status=models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return self.category