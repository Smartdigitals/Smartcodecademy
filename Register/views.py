from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.core.mail import send_mail

from django.conf import settings


from .models import Myreg

# Create your views here.

def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        num = request.POST['num']
        location = request.POST['location']
        email = request.POST['email']

        reg = Myreg(
            fname = fname,
            lname = lname,
            gender = gender,
            whatsapp = num,
            location = location,
            email = email
        )
        reg.save()
    
        # mymail = send_mail(
        #     'Welcome',
        #     f'Hi {fname} {lname}, \n Your registration concerning our free Python class has been recieved. \n Make sure you download our syllabus and send us a message on whatsapp. \n You are welcome. \n \n \n \n Mr. Smart. \n CEO SmartCodecademy',
        #     settings.EMAIL_HOST_USER,
        #     [email]
        # )

        # mymail.fail_silently = True
        # mymail.send()

        return render(request, "register/message.html")

    return render(request, "register/index.html")


def message(request):
    return render(request, "register/message.html") 




