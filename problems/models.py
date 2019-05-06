from django.db import models

# Create your models here.


Languages = (
    ('py', 'Python'),
    ('cpp', 'C++'),
    ('c', 'C Language'),
    ('java', 'Java'),
)

Verdicts = (
    ('ACC', 'Accepted'),
    ('TLE', 'Time Limit Exceeded'),
    ('WA', 'Wrong Answer'),
    ('MLE', 'Memory Limit Exceeded'),
)

class Problem(models.Model):
    Problem_Name = models.CharField(max_length = 90)
    statement = models.TextField()
    solution = models.TextField()
    solution_language = models.CharField(max_length=4, choices=Languages)
    Time_limit = models.DecimalField(max_digits=5, decimal_places=3)
    Memory_limit = models.DecimalField(max_digits=1000, decimal_places=8)

    def __str__(self):
        return self.Problem_Name



class Submission(models.Model):
    Problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Code = models.TextField()
    Code_language = models.CharField(max_length=4, choices=Languages)
    Verdict = models.CharField(max_length=4, choices=Verdicts)
    Time = models.DecimalField(max_digits=5, decimal_places=3 ,null=True)
    Memory = models.DecimalField(max_digits=5, decimal_places=3 ,null=True)
    Score = models.DecimalField(max_digits=5, decimal_places=3 ,null=True)




class TestCase(models.Model):
    Problem = models.ForeignKey(Problem, related_name='testcases', on_delete=models.CASCADE)
    Input  = models.TextField()
    Output = models.TextField(null=True)

    def __str__(self):
        return "test case {} for problem {}".format(self.pk, self.Problem.Problem_Name)
