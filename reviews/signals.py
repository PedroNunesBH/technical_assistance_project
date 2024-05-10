from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from devices.models import Devices


@receiver(post_save, sender=Devices)
def sent_email_for_review(sender, instance, **kwargs):
    if instance.status == "Entregue":
        subject = "Avalie o Nosso Serviço"
        message = (f"Olá {instance.client_name},"
                   "Gostaríamos de receber a sua avaliação sobre o nosso serviço para melhorarmos cada vez mais."
                   "Por gentileza, acesse o link : http://127.0.0.1:8000/create_review "
                   "e deixe suas avaliações/sugestões.")
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [f"{instance.client_email}"]
        send_mail(subject, message, from_email, to_email)
