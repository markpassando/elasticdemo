from rest_framework import serializers

class CharacterSearchSerializer(serializers.Serializer):
  """Serializer for GET params of the users/<user> endpoint"""

  first_name = serializers.CharField(
        required=True, max_length=50
    )