from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom user model that extends AbstractUser.
    """
    company = models.ForeignKey(
        "base.Company",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Company"),
        related_name="users",
    )

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
