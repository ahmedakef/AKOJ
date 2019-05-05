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

    def post(self, request, *args, **kwargs):
        code_language = request.data["Code_language"]
        source_code = request.data["Code"]

        compilar = Compilar(source_code, code_language)

        if compilar.language != 'python':
            result = compilar.compile(compilar.file_name)
            print(compilar.codes[result])

        result = compilar.run(compilar.testin, compilar.timeout)
        print(compilar.codes[result])
        Accepted = compilar.match(compilar.testout)  # True implies that code is accepted.
        print(Accepted)


        return self.create(request, *args, **kwargs)



class TestCaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer