from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render (request,'home.html',{})

def about(request):
    if request.method == "POST":
        # do stuff
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Send Email
        send_mail(
            name, # subject
            message, # message
            email, # from email
            ['kucera131@gmail.com'], # to email
            fail_silently=False, # in production fail_silently=True,
            )


        return render (request,'about.html',{'name':name})

    else:
        #return page
        return render (request,'about.html',{})

def services(request):
    return render (request,'services.html',{})

def portfolio(request):
    return render (request,'portfolio.html',{})

def blog(request):
    return render (request,'blog.html',{})

def blog_details(request):
    return render (request,'blog_details.html',{})

def elements(request):
    return render (request,'elements.html',{})

def portfolio_details(request):
    return render (request,'portfolio_details.html',{})

def contact(request):
    if request.method == "POST":
        # do stuff
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        # Send Email
        send_mail(
            name, # subject
            message, # message
            email, # from email
            ['kucera131@gmail.com'], # to email
            fail_silently=False, # in production fail_silently=True,
            )


        return render (request,'contact.html',{'name':name})

    else:
        #return page
        return render (request,'contact.html',{})
