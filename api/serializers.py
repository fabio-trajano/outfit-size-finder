from rest_framework import serializers

class SizePredictionSerializer(serializers.Serializer):
    height = serializers.FloatField()
    weight = serializers.FloatField()
    preference = serializers.ChoiceField(choices=["tight", "regular" "loose"])
    age = serializers.IntegerField()
    body_shape = serializers.ChoiceField(choices=["slim", "average", "athletic", "plus-size"])
