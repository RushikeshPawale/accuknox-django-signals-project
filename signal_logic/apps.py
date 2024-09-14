from django.apps import AppConfig

class SignalLogicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_logic'

    def ready(self):
        import signal_logic.sync_or_async_signal
        import signal_logic.thread_identification_signal
        import signal_logic.transaction_signal_handler
