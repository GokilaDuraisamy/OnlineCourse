from django.shortcuts import render
from .models import contactusform,Enquiry
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"templates/index.html")
def home(request):
    return render(request,"templates/index.html")
def aboutus(request):
    return render(request,"templates/aboutus.html")
def courses(request):
    return render(request,"templates/courses.html")
def courses1(request):
    return render(request,"templates/courses1.html")
def courses2(request):
    return render(request,"templates/courses2.html")
def courses3(request):
    return render(request,"templates/courses3.html")
def contactus(request):
    return render(request,"templates/contactus.html")
def enquiry(request):
   return render(request,"templates/enquiry.html")

def process_contactus(request):

    if request.method=='POST':
        fname = request.POST['fname']
        empid = request.POST['empid']
        message = request.POST['message']
        contactusform1 = contactusform.objects.create(fname=fname, empid=empid,message=message)
        messages.success(request,'Your message has been successfully sent')
        return render(request,"templates/contactus.html",{'fname':fname})
    else:
        return HttpResponse("Invalid request method.")

def process_enquiry(request):

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        courses=request.POST['courses']
        message = request.POST['message']
        Enq = Enquiry.objects.create(name=name, email=email,courses=courses,message=message)
        messages.success(request,'Your enquiry has been successfully sent')
        return render(request,"templates/enquiry.html",{'name':name})
    else:
        return HttpResponse("Invalid request method.")