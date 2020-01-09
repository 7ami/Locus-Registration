from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import OurForm

# Create your views here.
def home(request):
    return render(request, "registration/home.html")


def get_data(request):
    if request.method == "POST":
        form = OurForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/regis")
    else:
        form = OurForm()
    return render(request, "home.html", {"form": form})

