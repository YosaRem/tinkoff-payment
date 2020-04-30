from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils.constants import TRANSACTION_STATUSES


class Balance(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount * transaction.direction
        return balance / 10

    def __str__(self):
        return f"{self.user.name} - {str(self.get_balance())}"


class Transaction(models.Model):
    DIRECTIONS = [
        [-1, "Withdraw"],
        [1, "Refill"]
    ]

    balance = models.ForeignKey(Balance, related_name="transactions", on_delete=models.CASCADE)
    order_id = models.IntegerField
    amount = models.IntegerField("Количество копеек, на которое изменился баланс", editable=False)
    direction = models.IntegerField("Пополнение или снятие", choices=DIRECTIONS, editable=False)
    status = models.CharField("Статус транзакции", choices=TRANSACTION_STATUSES)

    def __str__(self):
        return f"{self.balance.user.name}: {str(self.amount * self.direction)}"


@receiver(post_save, sender=get_user_model())
def crate_balance_for_new_user(sender, instance, created, **kwargs):
    if created:
        balance = Balance(instance)
        balance.save()
