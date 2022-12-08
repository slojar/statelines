import json

from rest_framework import serializers
from .models import Questionnaire


class QuestionnaireSerializerOut(serializers.ModelSerializer):
    survey = serializers.SerializerMethodField()

    def get_survey(self, obj):
        if obj.survey:
            # items = str(obj.survey).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
            # result = items.split(",")
            import json

            # return json.dumps(obj.survey)
            return json.decoder.JSONDecoder().decode(obj.survey)

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
    survey = serializers.ListField()

    def create(self, validated_data):
        email = validated_data.get("email")
        gender = validated_data.get("gender")
        age_range = validated_data.get("age_range")
        annual_income = validated_data.get("annual_income")
        intervals = validated_data.get("intervals")
        survey_type = validated_data.get("survey_type")
        survey = validated_data.get("survey")
        comment = validated_data.get("comment")

        my_survey = json.dumps(survey)

        survey = Questionnaire.objects.create(
            email=email, gender=gender, age_range=age_range, annual_income=annual_income, intervals=intervals,
            survey=my_survey, comment=comment, survey_type=survey_type
        )

        return QuestionnaireSerializerOut(survey).data


