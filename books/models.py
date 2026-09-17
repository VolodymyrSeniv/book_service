from django.db import models
from django_enum import EnumField

from books.enums import CoverEnum


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=True, blank=True)
    cover = EnumField(CoverEnum, null=False, blank=False, default=CoverEnum.HARD)
    inventory = models.PositiveIntegerField(default=0, null=False, blank=False)
    daily_fee = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=False, blank=False
    )

    class Meta:
        verbose_name_plural = "Books"
        ordering = "title"
        unique_together = (("title", "author"),)

    def __str__(self):
        return f"{self.title} - {self.author}: Daily fee: {self.daily_fee}, Inventory: {self.inventory}, Cover: {self.cover}"  # ty: ignore
