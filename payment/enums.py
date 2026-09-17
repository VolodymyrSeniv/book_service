from enum import Enum


class Status(Enum):
    PENDING = "PENDING"
    PAID = "PAID"


class Type(Enum):
    PAYMENT = "PAYMENT"
    FINE = "FINE"
