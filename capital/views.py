from django.http import HttpResponse
from django.shortcuts import render
import requests
import random
# Create your views here.



r = requests.get("https://countriesnow.space/api/v0.1/countries/capital")
# Storing Data From API
data = r.json()

def index(request):
    # Landing Page
    return render(request,"base.html")
def home(request):
    # Questions Displaying Form
    l = random.sample((data['data']),1)[0]
    return render(request,'index.html',context={'name':l})

def answer_view(request):
    if request.method == "POST":
        capitalobj = (request.POST.get("capitalobj"))
        #User Answer Goes here
        name = request.POST["name"]
        answer = data['data']
        for i in answer:
            if i["name"]==capitalobj:
                ans =i
        #Correct Answer
        ans = ans["capital"]
        if name.strip().lower() == ans.lower():
            # checking user input with correct answer
            return HttpResponse("Correct Answer")
        elif name == "":
            return HttpResponse(f"Please Enter Your Answer")
        else:
            return HttpResponse(f"The correct answer is {ans}")