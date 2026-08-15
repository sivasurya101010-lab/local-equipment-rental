from django.db import models

from users.models import TimeStampedModel


class Equipment(TimeStampedModel):
    name = models.CharField(
        max_length=150,
        verbose_name="equipment name",
    )

    category = models.CharField(
        max_length=100,
        verbose_name="equipment category",
    )

    description = models.TextField(
        blank=True,
        verbose_name="equipment description",
    )

    rental_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="daily rental price",
    )

    deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="refundable deposit",
    )

    business = models.ForeignKey(
        "businesses.RentalBusiness",
        on_delete=models.CASCADE,
        related_name="equipment",
        verbose_name="rental business",
    )

    def __str__(self):
        return self.name