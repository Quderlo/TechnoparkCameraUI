from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    face_descriptor = models.BinaryField()
    photo = models.BinaryField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Sighting(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    sighting_time = models.DateTimeField(auto_now_add=True)
    camera_photo = models.BinaryField()

    def __str__(self):
        return f"Sighting of {self.person} at {self.sighting_time}"
