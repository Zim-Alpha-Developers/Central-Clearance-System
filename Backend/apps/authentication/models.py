from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, "admin"),
        (2, "user"),
    )
    email = models.CharField(max_length=50, unique=True)
    _user = models.CharField(
        _("_user_id"), max_length=255
    )  
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(_("staff"), default=False)
    last_login = models.DateTimeField(null=True)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. "
            "A user will get all permissions granted to each of their groups."
        ),
        related_name="customuser_set",  
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="customuser_set", 
        related_query_name="customuser",
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["_user", "email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"

    def __str__(self):
        return str(self.email)