from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def sync_signal_handler(sender, instance, **kwargs):
    print("Signal is triggered")
    time.sleep(2)  # Simulating a slow task
    print("Signal handled synchronously")
