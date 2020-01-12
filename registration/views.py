from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
"""def home(request):
    check = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            check = True

    else:
        form = RegistrationForm()
    context = {"form": form, "check": check}
    return render(request, "registration/home.html", context)
"""


def loginhandle(request):

    if request.method == "POST":
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass1")
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            # print(uname, pass1)
            return redirect("member")
        else:
            messages.error(request, "Invalid,please try again")
            # print(uname, pass1)

    return render(request, "registration/login.html")


def member(request):
    if request.method == "POST":
        pass
    return render(request, "registration/members.html")


"""
 look = 0
    if request.method == "POST":
        look = 1
        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        college = request.POST.get("college", "")
        con = Contact(
            fname=fname, lname=lname, email=email, phone=phone, college=college
        )
        con.save()
    return render(request, "registration/login.html", {"look": look})  
"""

