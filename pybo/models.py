from django.db import models
# Create your models here.
# Question - subject, content, create_date
# Answer - subject, content, create_date

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    # Question.objects.all()
    # Question.objects.filter(조건) -> 빈 querySet (없으면)
    # Question.objects.get(id=1) -> 오류 (없으면)
    # Question.objects.filter(subject__contains='장고') -> subject like '%장고%'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content

