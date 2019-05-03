# Generated by Django 2.2.1 on 2019-05-03 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Problem_Name', models.CharField(max_length=10)),
                ('statement', models.TextField()),
                ('solution', models.TextField()),
                ('solution_language', models.CharField(choices=[('py', 'Python'), ('cpp', 'C++'), ('c', 'C Language'), ('java', 'Java')], max_length=4)),
                ('Time_limit', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Memory_limit', models.DecimalField(decimal_places=8, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Input', models.TextField()),
                ('Output', models.TextField()),
                ('Problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.TextField()),
                ('Code_language', models.CharField(choices=[('py', 'Python'), ('cpp', 'C++'), ('c', 'C Language'), ('java', 'Java')], max_length=4)),
                ('Verdict', models.CharField(choices=[('ACC', 'Accepted'), ('TLE', 'Time Limit Exceeded'), ('WA', 'Wrong Answer'), ('MLE', 'Memory Limit Exceeded')], max_length=4)),
                ('Time', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Memory', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Score', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
            ],
        ),
    ]