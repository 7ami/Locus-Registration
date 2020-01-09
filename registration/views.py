from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm

# Create your views here.
def home(request):
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

