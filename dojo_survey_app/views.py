from django.shortcuts import render, redirect

# Create your views here.

def root(request):
    return render(request, 'index.html')

def results(request):
    print(request.POST)
    name = request.POST["name"],
    dojo_location = request.POST["dojo_location"]
    favorite_language = request.POST["favorite_language"]
    comments = request.POST['comments']
    context = {
        "name" : name,
        "dojo_location" : dojo_location,
        "favorite_language" : favorite_language,
        "comments" : comments
    }
    return render(request, 'results.html', context)