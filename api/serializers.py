from rest_framework import serializers

from .calculate import (UNDERWEIGHT, NORMALWEIGHT, OVERWEIGHT, OBESE, GENDERS)


class BmiInputSerializer(serializers.Serializer):
    weight = serializers.IntegerField(required=True, allow_null=False)
    height = serializers.IntegerField(required=True, allow_null=False)
    gender = serializers.ChoiceField(choices=(GENDERS[0], GENDERS[1]), required=True, allow_null=False)
    year = serializers.IntegerField(required=True, allow_null=False)
    month = serializers.IntegerField(required=True, allow_null=False)
    day = serializers.IntegerField(required=True, allow_null=False)


class BmiOutputSerializer(serializers.Serializer):
    bmi = serializers.FloatField(required=True, allow_null=False)
    weight = serializers.ChoiceField(choices=(UNDERWEIGHT, NORMALWEIGHT, OVERWEIGHT, OBESE), required=True)
    age = serializers.IntegerField(required=True, allow_null=False)

