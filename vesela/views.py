from django.shortcuts import render
from .models import Images


def home(request):
	context = {}
	images = Images.objects.all()
	context["images"] = images

	return render(request, "index.html", context)
