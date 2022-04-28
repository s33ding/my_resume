from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'myapp/home.html')

def about_me(request):
  return render(request, 'myapp/about_me.html')

def graduation(request):
  return render(request, 'myapp/graduation.html')

def certifications(request):
  return render(request, 'myapp/certifications.html')

def work_experience(request):
  return render(request, 'myapp/work_experience.html')

def contact(request):
  return render(request, 'myapp/contact.html')

def resume(request):
  return render(request, 'myapp/resume.html')
