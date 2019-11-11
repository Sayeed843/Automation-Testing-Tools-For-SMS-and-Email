from rest_framework import serializers
from pepypro.models import (UserEmail,
                            UserMessage)

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = [
            'user_name',
            'campaign_name',
            'api_key',
            'sender_email',
            'receiver_email',
            'email_subject',
            'email_body'
        ]




class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = [
            'user_name',
            'campaign_name',
            'api_key',
            'sender_number',
            'receiver_number',
            'mess_body'
        ]
