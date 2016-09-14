from rest_framework import serializers
from shop.models import Producto


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre ', 'marca', 'imagen', 'descripcion', 'precio')