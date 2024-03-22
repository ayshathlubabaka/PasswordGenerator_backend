from rest_framework import serializers

class PasswordGenerationSerializer(serializers.Serializer):
    strength = serializers.ChoiceField(choices=["weak","medium","strong"])
    length = serializers.IntegerField(min_value = 1)


