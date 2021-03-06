from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    OPEN_ADS_ALLOWED = 10

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user_id = self.context['request'].user.id
        opened_advs = self.Meta.model.objects.filter(
            creator=user_id, 
            status='OPEN'
        )
        if self.context.get('view').action == 'create' or data.get('status') == 'OPEN':
            if len(opened_advs) >= self.OPEN_ADS_ALLOWED:
                msg = f'Only {self.OPEN_ADS_ALLOWED} opened ads allowed!'
                raise serializers.ValidationError(msg)

        return data
