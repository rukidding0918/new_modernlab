from django.db import models

# Create your models here.
class Address(models.Model):
    # user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    address_detail = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address} {self.address_detail}"

    class Meta:
        verbose_name_plural = "주소"


class Contact(models.Model):
    contact = models.CharField(
        max_length=20,
        validators=[],
    )
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.contact
    
    class Meta:
        verbose_name_plural = "연락처"