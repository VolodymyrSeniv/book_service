from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    email = models.EmailField(unique=True)
