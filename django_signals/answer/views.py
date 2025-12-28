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
    results.append('''<p>I proved this by setting a start time before creating the object and an end time right after.
    In my signal, I added a time.sleep(4) command. When I ran the code, the total duration was a little over 4 seconds.
    This proves that my View stopped and waited for the Signal to finish sleeping before it could continue. 
    If signals were asynchronous, the view would have finished instantly</p>''')


    #answer 2:
    results.append("<h3> Answer 2: </h3>")
    #Here we get our current thread id
    thread_id = threading.get_ident()
    results.append(f"Caller thread ID: <b> {thread_id} </b>")
    #we trigger save, so there will be id printed in our terminal because of our signal
    #we can check whether the id generated in terminal and id in results are same or not
    #If they are same, then that proves they share same execution thread
    AnswerModel.objects.create(message ='question2')
    results.append('''<p> I proved this by using the threading library. I printed the current Thread ID in my View, 
                   and then I triggered the signal which printed its own Thread ID in the terminal. When I compared them, the IDs were exactly the same.
                    This confirms that Django did not create a new background thread for the signal; it ran strictly inside the caller's thread. </p>''')


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

    results.append(f"Did our object save in DB?: <b> {check} </b>")
    #If it is False, they are running in same transaction
    results.append('''<p> I proved this by opening a transaction.atomic() block. Inside this block, I successfully created a database object.
                    However, the signal that ran immediately after was designed to raise an Exception. Because the Signal crashed, 
                   the atomic block triggered a Rollback. When I checked the database afterwards, the object was gone (False). 
                   This proves the Signal is part of the same transaction—if it fails, the initial save is undone. </p>''')
    

    results.append("<h4> To view code go to - django_signals/answer/views.py </h4>")


    return HttpResponse("".join(results))
