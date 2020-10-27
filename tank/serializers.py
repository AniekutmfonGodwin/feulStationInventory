from rest_framework import serializers
from tank.models import Tank

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        read_only_fields = ['id','owner_id']
        fields = ['id','tank_name', 'product', 'capacity','owner_id']
