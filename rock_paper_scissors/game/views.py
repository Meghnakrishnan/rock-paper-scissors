from django.shortcuts import render,redirect
import random

# Create your views here.
def options(request):
    return render(request,'index.html')

def computer_choice(request):
    if request.method=='POST':
        items = ['stone', 'paper', 'scissor']
        random_item = random.choice(items)
        result=None
        action=request.POST.get('action')

        if random_item==action:
            result="IT IS A TIE!!"

        elif action=='stone'and random_item=='paper':
            result="HEY..Computer won!"

        elif action=='stone' and random_item=='scissor':
            result="CONGRATULATIONS..you won!"

        elif action=='paper' and random_item=='stone':
            result='CONGRATULATIONS..you won!'

        elif action=='paper' and random_item=='scissor':
            result="HEY..Computer won!"

        elif action=='scissor' and random_item=='stone':
            result="HEY..Computer won!"

        elif action=='scissor' and random_item=='paper':
            result="CONGRATULATIONS..you won!"

          

    return render(request,'choice.html',{'result':result,'random_item': random_item,'action':action})