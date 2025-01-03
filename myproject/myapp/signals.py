from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, LogEntry


@receiver(post_save, sender=MyModel)
def log_model_save(sender, instance, created, **kwargs):
    action = "Created" if created else "Updated"
    LogEntry.objects.create(
        action=action,
        model_name=instance.__class__.__name__,
    )
