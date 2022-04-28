from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'myapp/home.html')


def forms(request):
  return render(request, 'myapp/myForms.html')

def profile(request):
  return render(request, 'myapp/profile.html')

def videos(request):
  return render(request, 'myapp/videos.html')


def test(request):
  return render(request, 'myapp/test.html')

