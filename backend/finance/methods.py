from .models import Wallet, CreditCard, BankAccount


def get_account_instance(id):
    try:
        account = BankAccount.objects.get(source__id=id)
        type_ = 'BankAccount'
    except BankAccount.DoesNotExist:
        try:
            account = Wallet.objects.get(source__id=id)
            type_ = 'Wallet'
        except Wallet.DoesNotExist:
            account = CreditCard.objects.get(source__id=id)
            type_ = 'CreditCard'
    return account, type_
