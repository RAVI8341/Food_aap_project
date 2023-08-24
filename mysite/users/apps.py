from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    #lets configure the signals.py to app
    def ready(self):
        import users.signals
