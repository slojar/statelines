from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import QuestionnaireSerializerIn, Questionnaire, QuestionnaireSerializerOut


class CustomPagination(PageNumberPagination):
    page_size = 12
    max_page_size = 20


class QuestionnaireListCreateAPIView(ListCreateAPIView):
    serializer_class = QuestionnaireSerializerOut
    pagination_class = CustomPagination
    queryset = Questionnaire.objects.all().order_by("-id")

    def create(self, request, *args, **kwargs):
        serializer = QuestionnaireSerializerIn(data=request.data)
        if serializer.is_valid():
            serializer = serializer.save()
            return Response({"status": "Submitted", "data": serializer})
        else:
            return Response({"status": "Failed", "error": serializer.errors})


class QuestionnaireRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionnaireSerializerOut
    queryset = Questionnaire.objects.all()
    lookup_field = "id"


