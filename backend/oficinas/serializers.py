from rest_framework import serializers
from oficinas.models import Office

class OfficeModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Office
        fields = (
            'pk',
            'name',
            'cod_int',
            'user_in_charge',
            'max_people',
            'has_phone',
            'has_bathroom',
            'has_wifi',
        )
     

class OfficeSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    cod_int = serializers.CharField(max_length=255)
    user_in_charge = serializers.CharField(max_length=255)
    max_people = serializers.IntegerField()
    has_phone = serializers.BooleanField()
    has_bathroom = serializers.BooleanField()
    has_wifi = serializers.BooleanField()


    def create(self, data):

        off = Office.objects.create(**data)
        return off