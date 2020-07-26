from django.shortcuts import render
from lfapp.forms import user_form
from django.http import HttpResponse,HttpResponseRedirect
from lfapp.models import user_data,question,imdb_data
from django.contrib import messages
from django.db.models import Q
import random
import csv, io
# Create your views here.

def user_login(request):
    nu = str(random.randint(1000, 9999))
    file2 = open("code.txt", "w+")
    file2.write(nu)
    file2.close()

    if request.method == "POST":
        form = user_form(request.POST)
        username = request.POST['user']
        password = request.POST['password']
        userscore = user_data.objects.all().order_by('-score')
        if username:
            if password:
                username1 = user_data.objects.filter(Q(user_name=username)&
                                                     Q(user_password=password))
                if username1:
                    n = random.randint(1, 20)
                    qz = question.objects.all()[n:n + 10]

                    user_name = username

                    return render(request, 'question.html', {'user':user_name,'us':userscore,'qz': qz,'scor':username1})
                    #return render(request, 'question.html')
                else:
                    messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request,'login.html')






def user_signup(request):
    '''
    nu = str(random.randint(1000,9999))
    file2 = open("code.txt", "w+")
    file2.write(nu)
    file2.close()'''

    #frm = user_form()
    if request.method == "POST":
        frm = user_form(request.POST)
        file = open("code.txt", "r")
        n = str(file.read())
        file.close()
        #print(n)
        verify_code = request.POST['code']
        #a = nu
        if frm.is_valid():
            print("random",n)
            print("enter",verify_code)
            try:
                if verify_code == n:

                    frm.save()
                    return HttpResponseRedirect('/login/create_account/')
                else:
                    messages.error(request, 'Enter the correct code')
                #file2 = open("code.txt", "w+")
                #file2.write(nu)
                #file2.close()

            except:
                pass
    else:
        frm = user_form()
        #nu = random.randint(000, 999)
        #file2 = open("code.txt", "w+")
        #file2.write(nu)
        #file2.close()
    return render(request,"signup.html",{'frm':frm})



