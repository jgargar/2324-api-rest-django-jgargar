from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from patinetes.models import Usuario, Patinete, Alquiler


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username',
        many=True,
        read_only=True
    )

    class Meta:
        model = Usuario
        fields = ['url','user', 'debito']


class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['url', 'numero', 'tipo', 'precio_desbloqueo', 'precio_minuto']


class AlquilerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alquiler
        fields = ['url', 'usuario', 'patinete', 'fecha_desbloqueo', 'fecha_entrega',
                  'coste_final']
