from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    # name_user = models.CharField(max_length=100, null=True)
    # surname_user = models.CharField(max_length=100, null=True)
    # email_user = models.CharField(max_length=255, null=True)
    #
    # def __str__(self) -> str:
    #     return self.name_user



























    phone_number = models.CharField(max_length=100)



