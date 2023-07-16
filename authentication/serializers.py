from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Retrieve the password from validated_data

        user = User.objects.create(**validated_data)  # Create the user object without the password

        if password is not None:
            user.set_password(password)  # Set the password separately

        user.save()  # Save the user object with the updated password

        return user
