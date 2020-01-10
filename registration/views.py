from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm
from .models import Contact

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


def home(request):
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
    return render(request, "registration/home.html", {"look": look})
