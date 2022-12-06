from rest_framework import serializers
from .models import Questionnaire


class QuestionnaireSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        exclude = []


class QuestionnaireSerializerIn(serializers.Serializer):
    email = serializers.EmailField(required=False)
    gender = serializers.CharField()
    age_range = serializers.CharField()
    annual_income = serializers.CharField()
    intervals = serializers.IntegerField()
    survey_type = serializers.CharField()
    comment = serializers.CharField(required=False)
    survey = serializers.DictField()

    def create(self, validated_data):
        email = validated_data.get("email")
        gender = validated_data.get("gender")
        age_range = validated_data.get("age_range")
        annual_income = validated_data.get("annual_income")
        intervals = validated_data.get("intervals")
        survey_type = validated_data.get("survey_type")
        survey = validated_data.get("survey")
        comment = validated_data.get("comment")

        survey = Questionnaire.objects.create(
            email=email, gender=gender, age_range=age_range, annual_income=annual_income, intervals=intervals,
            survey=survey, comment=comment, survey_type=survey_type
        )

        return QuestionnaireSerializerOut(survey).data


