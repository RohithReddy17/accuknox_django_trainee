import threading
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AnswerModel


# Question 1:
# By default are django signals executed synchronously or asynchronously? 
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.

@receiver(post_save, sender=AnswerModel)
def question_1(sender, instance, created, **kwargs):
    if instance.message == 'question1':
        print("Start")
        time.sleep(4)
        print("End")


# Question 2: 
# Do django signals run in the same thread as the caller?
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.

@receiver(post_save, sender=AnswerModel)
def question_2(sender, instance, created, **kwargs):
    if instance.message == 'question2':
        print(f"Thread ID: {threading.get_ident()}")


# Question 3:
# By default do django signals run in the same database transaction as the caller?
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.

@receiver(post_save, sender=AnswerModel)
def question_3(sender, instance, created, **kwargs):
    if instance.message == 'question3':
        raise Exception("Crash to test")

