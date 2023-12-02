from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    comment = models.CharField(max_length=200,null=False,blank=False)
    imageURL = models.CharField(max_length=200,null=False,blank=False)
    yumFactor = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])
    date_created =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return self.name