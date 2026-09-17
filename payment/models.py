from django.db import models
from django_enum import EnumField

from borrowing.models import Borrowing
from payment.enums import Status, Type


class Payment(models.Model):
    status = EnumField(Status, default=Status.PENDING)
    type = EnumField(Type)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField()
    session_id = models.CharField(max_length=255)
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Payments"
        ordering = "payment_date"

    def __str__(self):
        return f"{self.id}. {self.status}. {self.money_to_pay}"  # ty: ignore
