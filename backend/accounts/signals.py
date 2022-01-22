from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save

from .models import Account, Income, Expense, Transfer

# ToDo(lgruelas) handle change on is_payed


def is_update(instance, **kwargs):
    return not instance._state.adding


def update_old_account_balance_from_income(instance, old_account_balance, old_account_id):
    if instance.old_amount:
        fixed_balance = old_account_balance - instance.old_amount
    else:
        fixed_balance = instance.old_account_balance - instance.amount
    Account.objects.filter(id=old_account_id).update(balance=fixed_balance)


def update_new_account_balance_from_income(instance, instance_amount, account_name="account"):
    getattr(instance, account_name).balance += instance_amount
    getattr(instance, account_name).save()


def update_old_account_balance_from_expense(instance, old_account_balance, old_account_id):
    if instance.old_amount:
        fixed_balance = old_account_balance + instance.old_amount
    else:
        fixed_balance = instance.old_account_balance + instance.amount
    Account.objects.filter(id=old_account_id).update(balance=fixed_balance)


def update_new_account_balance_from_expense(instance, instance_amount, account_name="account"):
    getattr(instance, account_name).balance -= instance_amount
    getattr(instance, account_name).save()


@receiver(pre_save, sender=Income)
def saves_old_income_if_update(sender, instance, **kwargs):
    if is_update(instance, **kwargs):
        old_income = Income.objects.select_related("account").get(id=instance.id)
        instance.old_amount = old_income.amount
        if instance.account.id != old_income.account.id:
            instance.old_account_id = old_income.account.id
            instance.old_account_balance = old_income.account.balance


@receiver(pre_save, sender=Expense)
def saves_old_expense_if_update(sender, instance, **kwargs):
    if is_update(instance, **kwargs):
        old_expense = Expense.objects.select_related("account").get(id=instance.id)
        instance.old_amount = old_expense.amount
        if instance.account.id != old_expense.account.id:
            instance.old_account_id = old_expense.account.id


@receiver(pre_save, sender=Transfer)
def saves_old_transfer_if_update(sender, instance, **kwargs):
    if is_update(instance, **kwargs):
        old_transfer = Transfer.objects.select_related("account_to", "account_from").get(id=instance.id)
        instance.old_amount = old_transfer.amount
        if instance.account_to.id != old_transfer.account_to.id:
            instance.old_account_to_id = old_transfer.account_to.id
        if instance.account_from.id != old_transfer.account_from.id:
            instance.old_account_from_id = old_transfer.account_from.id


@receiver(post_save, sender=Income)
def increase_balance_on_income(sender, instance, created, **kwargs):
    if created:
        update_new_account_balance_from_income(instance, instance.amount)
    elif is_update(instance, **kwargs):
        if instance.old_account_id:
            update_old_account_balance_from_income(instance, instance.old_account_balance, instance.old_account_id)
            update_new_account_balance_from_income(instance, instance.amount)
        elif instance.old_amount:
            update_new_account_balance_from_income(instance, instance.old_amount - instance.amount)


@receiver(post_save, sender=Expense)
def decrease_balance_on_expense(sender, instance, created, **kwargs):
    if created and instance.is_payed:
        update_new_account_balance_from_expense(instance, instance.amount)
    elif is_update(instance, **kwargs):
        if instance.old_account_id:
            update_old_account_balance_from_expense(instance, instance.old_account_balance, instance.old_account_id)
            update_new_account_balance_from_expense(instance, instance.amount)
        elif instance.old_amount:
            update_new_account_balance_from_expense(instance, instance.old_amount - instance.amount)


@receiver(post_save, sender=Transfer)
def update_balance_on_transfer(sender, instance, created, **kwargs):
    if created and instance.is_payed:
        update_new_account_balance_from_income(instance, instance.amount, "account_to")
        update_new_account_balance_from_expense(instance, instance.amount, "account_from")
    elif is_update(instance, **kwargs):
        if instance.old_account_id:
            update_old_account_balance_from_income(instance,
                                                   instance.old_account_to_balance,
                                                   instance.old_account_to_id)
            update_old_account_balance_from_expense(instance,
                                                    instance.old_account_from_balance,
                                                    instance.old_account_from_id)
            update_new_account_balance_from_income(instance, instance.amount, "account_to")
            update_new_account_balance_from_expense(instance, instance.amount, "account_from")
        elif instance.old_amount:
            update_new_account_balance_from_income(instance, instance.old_amount - instance.amount, "account_to")
            update_new_account_balance_from_expense(instance, instance.old_amount - instance.amount, "account_from")


@receiver(post_delete, sender=Income)
def decrease_balance_on_income_delete(sender, instance, **kwargs):
    instance.account.balance -= instance.amount
    instance.account.save()


@receiver(post_delete, sender=Expense)
def increase_balance_on_expense_delete(sender, instance, **kwargs):
    if instance.is_payed:
        instance.account.balance += instance.amount
        instance.account.save()


@receiver(post_delete, sender=Transfer)
def update_balance_on_transfer_delete(sender, instance, **kwargs):
    if instance.is_payed:
        instance.account_from.balance += instance.amount
        instance.account_to.balance -= instance.amount
        instance.account_from.save()
        instance.account_to.save()
