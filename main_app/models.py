from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
COMPONENTS = (
    ('C', 'Communications System'),
    ('W', 'Weapons Malfunction'),
    ('R', 'Reactor Cores')
)

# Create your models here.

class Weapon(models.Model):
  name = models.CharField(max_length=60)
  info = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('weapons_detail', kwargs={'pk': self.id})

class Gundam(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    weapons = models.ManyToManyField(Weapon)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gundam_id': self.id})

# Add new Feeding model below Gundam model
class Repairs(models.Model):
  date = models.DateField('repair Date')
  component = models.CharField(
    max_length=22,
    choices=COMPONENTS,
    default=COMPONENTS[0][0]
  )

  gundam = models.ForeignKey(Gundam, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_component_display()} on {self.date}"

  class Meta:
    ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    gundam = models.ForeignKey(Gundam, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for gundam_id: {self.gundam_id} @{self.url}"
