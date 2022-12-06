from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.QuestionnaireListCreateAPIView.as_view(), name="questionnaire"),
    path("<int:id>", views.QuestionnaireRetrieveAPIView.as_view(), name="questionnaire-detail"),
]


