from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def thread_signal_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal is executed successfully in thread: {current_thread}")
