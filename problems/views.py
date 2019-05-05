from rest_framework import viewsets, generics

from .serializers import ProblemSerializer, SubmissionSerializer , TestCaseSerializer
from .models import Problem, Submission , TestCase
# Create your views here.

from .compilar import Compilar

class ProblemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class SubmissionViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer



    def perform_create(self, serializer):
        created_submission = serializer.save()

        code_language = created_submission.Code_language
        source_code = created_submission.Code

        compilar = Compilar(source_code, code_language)

        if compilar.language != 'python':
            result = compilar.compile(compilar.file_name)
            print(compilar.codes[result])

        Accepted = True
        tescases = TestCase.objects.filter(Problem = created_submission.Problem )
        for testcase in tescases:
            result = compilar.run(testcase.Input, created_submission.Problem.Time_limit)
            print(compilar.codes[result])
            Accepted = Accepted and compilar.match(testcase.Output)
            print(Accepted)

        Verdict = "ACC" if Accepted == True else "WA"
        created_submission.Verdict = Verdict



class TestCaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer