from rest_framework import viewsets

from .serializers import ProblemSerializer, SubmissionSerializer , TestCaseSerializer
from .models import Problem, Submission , TestCase
# Create your views here.


class ProblemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer



class TestCaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer