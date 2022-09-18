from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    name = request.POST['name']
    id = request.POST['id']
    description = request.POST['description']
    ticker = request.POST['ticker']
    #gender=request.POST['gender']
    #vehicle=request.POST['vehicle']
    start_date=request.POST['start_date']
    #salary=int(request.POST['salary'])
    
    return render(request,'result.html',{'ticker':ticker,'start_date':start_date,'description':description,'name':name,'id':id})
    