from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("이메일", unique=True)
    cell_phone = models.CharField("휴대폰", max_length=20, null=False, blank=False)
    name = models.CharField("이름", max_length=30, null=False, blank=False)
    date_joined = models.DateTimeField("가입일", auto_now_add=True)
    is_staff = models.BooleanField("운영진", default=False)
    is_active = models.BooleanField("이용가능여부", default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = "원장님"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    license_number = models.PositiveSmallIntegerField(
        "면허번호", unique=True, null=False, blank=False
    )
    license_image = models.ImageField(upload_to="license", blank=False)

    class Meta:
        verbose_name = verbose_name_plural = "원장님 정보"


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="business")
    name = models.CharField("한의원명", max_length=30, null=False, blank=False)
    address = models.CharField("주소", max_length=100, null=False, blank=False)
    business_phone = models.CharField("전화번호", max_length=20, null=False, blank=False)
    cell_phone = models.CharField("휴대폰", max_length=20, null=False, blank=False)
    fax = models.CharField("팩스", max_length=20, null=False, blank=False)
    business_number = models.PositiveSmallIntegerField(
        "사업자번호", unique=True, null=False, blank=False
    )
    business_image = models.ImageField("사업자등록증", upload_to="business", blank=False)

    class Meta:
        verbose_name = verbose_name_plural = "한의원 정보"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="address")
    reciever_name = models.CharField("받는 사람", max_length=30, null=False, blank=False)
    address = models.CharField("주소", max_length=100, null=False, blank=False)
    address_detail = models.CharField("상세주소", max_length=100, null=False, blank=False)
    cell_phone = models.CharField("휴대폰", max_length=20, null=False, blank=False)
    is_default = models.BooleanField("기본배송지", default=False)

    class Meta:
        verbose_name = verbose_name_plural = "배송지 정보"
