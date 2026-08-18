from django.db import models

from users.models import TimestampedModel


class Equipment(TimestampedModel):
    name=models.CharField(max_length=150,verbose_name="equipment name")

    description=models.CharField(max_length=500,verbose_name="equipment description")

    category=models.CharField(max_length=100,verbose_name="equipment category")

    rental_price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="equipment price")

    deposit=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="equipment deposit")

    business=models.ForeignKey("businesses.RentalBusiness",on_delete=models.CASCADE,related_name="equipment",verbose_name="rental business")

    def __str__(self):
        return self.name

class EquipmentUnit(TimestampedModel):

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        RESERVED = "RESERVED", "Reserved"
        RENTED = "RENTED", "Rented"
        INSPECTION = "INSPECTION", "Inspection"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        RETIRED = "RETIRED", "Retired"

    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,related_name="units",verbose_name="equipment")

    serial_number = models.CharField(max_length=100,unique=True,verbose_name="serial number",)

    status = models.CharField(max_length=20,choices=Status.choices,default=Status.AVAILABLE,verbose_name="unit status",db_index=True)

    condition = models.CharField(max_length=100,default="GOOD",verbose_name="current condition")

    purchase_date = models.DateField(null=True,blank=True,verbose_name="purchase date")

    notes = models.TextField(blank=True,verbose_name="unit notes")

    def __str__(self):
        return f"{self.equipment.name} - {self.serial_number}"