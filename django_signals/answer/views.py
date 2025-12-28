import time
import threading
from django.http import HttpResponse
from .models import AnswerModel
from django.db import transaction

def answers(request):
    results = []

    #answer 1:
    # Here we actually calculate time and check whether it is equal to the time we set to sleep in signal
    results.append("<h3> Answer 1: </h3>")
    start = time.time()

    #Here we trigger save
    AnswerModel.objects.create(message ='question1')

    end = time.time()
    duration = end - start
    #we can check in result, if time waited is around 4 then it is synchronous because it waited for the signal
    results.append(f"Time waited: <b> {duration: .2f} </b>")


    #answer 2:
    results.append("<h3> Answer 2: </h3>")
    #Here we get our current thread id
    thread_id = threading.get_ident()
    results.append(f"Caller thread ID: <b> {thread_id} </b>")
    #we trigger save, so there will be id printed in our terminal because of our signal
    #we can check whether the id generated in terminal and id in results are same or not
    #If they are same, then that proves they share same execution thread
    AnswerModel.objects.create(message ='question2')


    #answer 3:
    results.append("<h3> Answer 3: </h3>")
    try:
        #open transaction
        with transaction.atomic():
            #this object with message 'question3' will be holding in temporary memory of DB
            AnswerModel.objects.create(message ='question3') 
            #after this signal will be called and exception will be raised
            print("This line will never print") #because transcation detect exception and everything will be roll backed
    except Exception as e:
        #signal will crash due to the exception we raised for this particular message 
        print(f"Caught Exception: {e}")

    #verify whether our message is there or not
    check = AnswerModel.objects.filter(message ='question3').exists()

    results.append(f"Did our object save in DB? <b> {check} </b>")
    #If it is False, they are running in same transaction


    return HttpResponse("".join(results))




