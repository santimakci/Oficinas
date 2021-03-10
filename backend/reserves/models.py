from django.db import models

from oficinas.models import Office
import datetime

class Reserve(models.Model):

    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='reserve')
    client = models.CharField(max_length=255, null=False)
    user_create_reserve = models.CharField(max_length=255, null=False)
    date_reserve = models.DateField(default=datetime.date.today)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=False)

    def __str__(self):
        """Return education and first_name and last_name."""
        return f'{self.Office.name} {self.client} {self.date_start}'

    @classmethod
    def reserve_by_date_and_id(self, date, id_office):
        res = self.objects.filter(date_start=date, office_id=id_office)
        return res
