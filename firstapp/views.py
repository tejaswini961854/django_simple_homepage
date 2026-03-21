from django.shortcuts import render

def home(request):
    context={'name':'sachin'}
    return render(request,'app/home.html',context)

