from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import IdCards

@receiver(post_save, sender=IdCards)
def create_user_by_id_card(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(username=instance.id_card, password=instance.id_card)


@receiver(post_delete, sender=IdCards)
def delete_user_by_id_card(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.id_card)
        user.delete()
    except:
        pass