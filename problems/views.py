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
            print("compilation result : {}".format(compilar.codes[result]))

        Accepted = True
        i=0
        tescases = TestCase.objects.filter(Problem = created_submission.Problem )
        for testcase in tescases:
            i+=1
            result = compilar.run(testcase.Input, created_submission.Problem.Time_limit)
            print("{} on test case :{}".format(compilar.codes[result],i))
            Accepted = Accepted and compilar.match(testcase.Output)
            if Accepted == False:
                print("faild on test case".format(i))
                break

        Verdict = "ACC" if Accepted == True else "WA"
        created_submission.Verdict = Verdict
        created_submission.save()


class TestCaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer



    def perform_create(self, serializer):
        created_testcase = serializer.save()

        code_language = created_testcase.Problem.solution_language
        source_code = created_testcase.Problem.solution

        compilar = Compilar(source_code, code_language)

        if compilar.language != 'python':
            result = compilar.compile(compilar.file_name)
            print("compilation result : {}".format(compilar.codes[result]))

        result = compilar.run(created_testcase.Input, created_testcase.Problem.Time_limit)
        if compilar.codes[result] == 'success':
            created_testcase.Output = open(compilar.program_output, "r").read()

        created_testcase.save()