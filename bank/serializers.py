from rest_framework import serializers
from .models import InfoUser

class InfoUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfoUser
        fields = ('id','socio', 'tasa', 'mon_max')