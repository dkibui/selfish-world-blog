from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm
from blog.models import Blog


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "main/index.html", context=context)


def service(request):
    return render(request, "main/service.html")

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Valid")
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/contact.html", {"form": form})
    else:
        return render(request, "main/contact.html", {"form": form})


def team(request):
    return render(request, "main/about.html")
