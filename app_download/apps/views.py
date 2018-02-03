from django.shortcuts import render
from .core import file_core

# Create your views here.
def home(request):
	return render(request, "home.html")

def packages(request):
	packages = file_core.get_all_packages()
	return render(request, "package.html", {"packages": packages})