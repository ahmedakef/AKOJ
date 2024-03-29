from .models import Problem, Submission , TestCase
from rest_framework import serializers


class ProblemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Problem
        fields = ('Problem_Name' , 'statement', 'solution', 'solution_language', 'Time_limit','Memory_limit', 'testcases')


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    Problem = serializers.CharField(source='Problem.id')


    class Meta:
        model = Submission
        fields = ('Problem', 'Code', 'Code_language', 'Verdict','Time','Memory','Score')
        read_only_fields = ('Verdict', 'Time','Memory','Score')



class TestCaseSerializer(serializers.HyperlinkedModelSerializer):
    Problem = serializers.CharField(source='Problem.id')


    class Meta:
        model = TestCase
        fields = ('Problem', 'Input','Output')
        read_only_fields = ('Output',)