from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Devices


@receiver(pre_save, sender=Devices)
def device_status_update(sender, instance, **kwargs):
    if instance.pk is not None:  # Verifica se não é a criação de um objeto
        device = Devices.objects.get(pk=instance.pk)  # Captura o objeto
        if device.status != instance.status:  # Verifica se o status sofreu alguma alteração
            subject = f'Atualização do Status do Seu Produto {instance.model}'  # Assunto do email
            message = (f'Olá {instance.client_name}.\n'
                       f'Estamos passando para informar que o status do seu produto {instance.model}'
                       f' foi atualizado para {instance.status}.\n'
                       f'Qualquer coisa fique a vontade para entrar em contato com nossa equipe.')
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [f'{instance.client_email}']  # Email do destinatário

            send_mail(subject, message, from_email, to_email)
