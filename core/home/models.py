from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True, blank=True)


class Car(models.Model):
    car_name = models.CharField(max_length=300)
    speed = models.IntegerField(max_length=50)

    def __str__(self) -> str:
        return self.car_name