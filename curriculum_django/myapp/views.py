from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

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
  mySummary_p1 = "Experienced Co-Founder with a demonstrated history of working in the information technology and services industry. Skilled in Python, SQL, Pandas, Numpy, Sympy and Command Line. Professional with a Bachelor's degree focused in Data Science and Artiﬁcial Intelligence from IESB."  
  mySummary_p2 = "Interested in AWS tools, Spark, Airﬂow, PostgreSQL, No-SQL, Docker, ETL, Scrap, CLI, Django and becoming an expert in Python."
  pos_wk1 = "Data Engineer"  
  place_wk1 = "Ministery of Communication"  
  finished_wk1 = "April 2022"  
  start_wk1 = "November 2021"
  description_wk1 = "Support the analysis of problems and technical solutions of data integration on projects related to internet connectivity in the national."  


  context = {
    "name":"Roberto Moreira Diniz",
    "role":"Data Engineer/DataScientist", 
    "email":"robertomdiniz@protonmail.com",
    "cell_phone":"+55 (61) 98234-0088",
    "github":"https://github.com/s33ding",
    "city":"Brasília",
    "country":"Brazil",
    "university":"IESB, Brasília",
    "course":"Data Science & Artificial Intelligence",
    "telegram":"robertomdiniz",

    "summary_p1": mySummary_p1,
    "summary_p2": mySummary_p2,

    "pos_wk1" :  pos_wk1,
    "place_wk1" :  place_wk1,
    "finished_wk1" :  finished_wk1,
    "start_wk1" :  start_wk1,
    "description_wk1" :  description_wk1,



    "py1":"Pandas",
    "py2":"Subprocess",
    "py3":"Plotly",
    "py4":"Boto3",
    "py5":"PySpark",
    
    "SQL1":"PostgreSQL",
    "SQL2":"SQLlite",
    
    "linux1":"Bash",
    "linux2":"Command Line",
    "linux3":"Data Processing in Shell",
    "backend1":"django",
    "backend2":"HTML",
    "backend3":"CSS",
    "others1":"AWS",
    }
  template = loader.get_template("myapp/resume.html")
  return HttpResponse(template.render(context))
