from django.shortcuts import render,redirect
from . models import Quiz
from django.http import HttpResponse
from . forms import Register

# Create your views here.
a=[];b=[];

answer=Quiz.objects.all()
for i in answer:
    a.append(i.sol)
def index(request):
    context=Quiz.objects.all()
    items={
        'items':context
    }
    return render(request,'home.html',items)

def saveans(request):
    ans=request.GET['ans']
    print(ans)
    b.append(ans)
    print(b)
    return HttpResponse('success')
def register(request):
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quizpage')
    else:
        form=Register();
        context={'form':form}
        return render(request,'register.html',context)
    '''
    form=Register()
    context={'form':form}
    return render(request,'register.html',context)'''

def welcome(request):
    return render(request,'welcome.html')
def result(request):
    score=0;

    for i in range(min(len(a),len(b))):
        if(a[i]==b[i]):
            score+=1
    print(score)
    return render(request,'result.html',{'score':score})

