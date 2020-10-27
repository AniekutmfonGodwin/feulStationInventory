from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# Create your models here.
class Tank(models.Model):

    tank_name = models.CharField(_("Tank name"), max_length=50)
    product = models.CharField(_("Product"), max_length=50)
    capacity = models.TextField(_("Capacity"))
    owner_id = models.ForeignKey(User, verbose_name=_("Owner ID"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tank")
        verbose_name_plural = _("Tanks")

    def __str__(self):
        return self.tank_name

    def get_absolute_url(self):
        return reverse("Tank_detail", kwargs={"pk": self.pk})
