from .models import Problem, Submission , TestCase
from rest_framework import serializers


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem
        fields = ('Problem_Name' , 'statement', 'solution', 'solution_language', 'Time_limit','Memory_limit')


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ('Problem', 'Code', 'Code_language','Time','Memory','Score')



class TestCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestCase
        fields = ('Problem', 'Input','Output')