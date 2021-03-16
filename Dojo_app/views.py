
from django.shortcuts import render, redirect

def form_page(request):
    return render(request, "index.html")

def result(request):
    print(request.POST)
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']

    context = {
        "name": name_from_form,
        "location": location_from_form,
        "language": language_from_form,
        "comment": comment_from_form,
    }
    return render(request, "result.html", context)