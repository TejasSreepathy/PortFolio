from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def education(request):
    return render(request, 'portfolio/education.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
