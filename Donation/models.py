from django.db import models
from Donor.models import DonorClass
# Create your models here.
class DonationClass(models.Model):
    donor_id = models.ForeignKey(DonorClass, on_delete=models.SET_NULL, blank=True, null=True)
    donation_id = models.IntegerField(unique=True, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __int__(self):
        return self.donation_id
