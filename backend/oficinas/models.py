from django.db import models

class Office(models.Model):

    name = models.CharField(max_length=255, null=False)
    cod_int = models.CharField(max_length=255, null=False)
    user_in_charge = models.CharField(max_length=255, null=False)
    max_people = models.IntegerField(null=False)
    has_phone = models.BooleanField(null=False, default=False)
    has_bathroom = models.BooleanField(null=False, default=False)
    has_wifi = models.BooleanField(null=False, default=False)


    def __str__(self):
        """Return education and first_name and last_name."""
        return f'{self.cod_int} {self.name}'
