from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def transaction_signal_checker(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is running in the same database transaction.")
    else:
        print("Signal is NOT running in the same database transaction.")
