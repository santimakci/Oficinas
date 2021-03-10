from rest_framework import serializers
from reserves.models import Reserve
from oficinas.models import Office

class ReserveModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reserve
        fields = (
            'pk',
            'client',
            'user_create_reserve',
            'date_reserve',
            'date_start',
            'date_end',
        )

class ReserveSerializer(serializers.Serializer):

    office_id = serializers.IntegerField()
    client = serializers.CharField(max_length=255)
    user_create_reserve = serializers.CharField(max_length=255)
    date_start = serializers.DateField()
    date_end = serializers.DateField()

    def validate(self, data):

        res = Reserve.reserve_by_date_and_id(data['date_start'], data['office_id'])
        if res:
            raise serializers.ValidationError('Ya existe una reserva para esa oficina en esa fecha')
        
        return data

    def create(self, data):

        res = Reserve.objects.create(**data)
        return res