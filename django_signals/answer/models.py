from django.db import models

# Create your models here.
class AnswerModel(models.Model):
    message = models.CharField(max_length=130)

    def __str__(self):
        return self.message
