from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    

    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    # user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)  # Store selected option as 'A', 'B', 'C', or 'D'

    def __str__(self):
        return f"{self.question.question_text} : {self.answer}"
