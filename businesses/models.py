from django.db import models
from django.conf import settings

from users.models import TimestampedModel


class RentalBusiness(TimestampedModel):

    owner=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="rental_business",verbose_name="business owner")

    name=models.CharField(max_length=20,verbose_name="business name",db_index=True,)

    description=models.CharField(max_length=500,blank=True,verbose_name="business description")

    location=models.CharField(max_length=300,verbose_name="business location")

    phone=models.CharField(max_length=10,verbose_name="business number")

    