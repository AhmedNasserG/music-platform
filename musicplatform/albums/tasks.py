import os
from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings

from albums.models import Album


# send congratulation email to artist when album is created
# @shared_task
# def send_congratulation_email(album):
#     print('send congratulation email to artist when album is created')
#     send_mail(
#         'Congratulation!',
#         f'Your album {album} has been created!',
#         # f'Your album {album.name} has been created!',
#         os.environ.get('EMAIL_HOST_USER'),
#         ['ahmednasser217217@gmail.com'],
#         # [album.artist.user.email],
#         fail_silently=False,
#     )
#     print('email sent')

@shared_task
def send_congratulation_email(album):
    print('send congratulation email to artist when album is created')
    send_mail(
        'Congratulation!',
        f'Your album album has been created!',
        'settings.EMAIL_HOST_USER',
        ['ahmednasser217217@gmail.com'],
        fail_silently=False
    )
    print('email sent')


# @shared_task
# def send_email_task(email, subject, message):
#     send_mail(
#         subject,
#         message,
#         os.environ.get('EMAIL'),
#         [email],
#         fail_silently=False,
#     )
