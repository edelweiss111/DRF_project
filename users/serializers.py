from rest_framework import serializers

from study.serializers import PaymentSerializer
from users.models import User


class OwnerSerializer(serializers.ModelSerializer):
    payment_list = PaymentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'last_name')
