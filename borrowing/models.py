from django.db import models

from books.models import Book
from customer.models import Customer


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowing")
    user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="borrowing"
    )

    class Meta:
        verbose_name_plural = "Borrowings"
        ordering = "borrow_date"

    def __str__(self):
        return str(
            f"{self.user.first_name} {self.user.last_name}. {self.borrow_date} - {self.expected_return_date}. {self.book.title}"  # ty: ignore
        )
