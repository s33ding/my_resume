#%%
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import os

# Create your views here.
personalData = {
    "name":"Roberto Moreira Diniz",
    "role":"Data Engineer/Data Scientist", 
    "email":"robertomdiniz@protonmail.com",
    "cell_phone":"+55 (61) 98234-0088",
    "github":"@s33ding",
    "githubLink":"https://github.com/s33ding",
    "city":"Brasília",
    "country":"Brazil",
    "linkedin":"@robertomdiniz",
    "linkedinLink":"https://www.linkedin.com/in/robertomdiniz/",
    }
educationDct = {
    "university":"IESB, Brasília",
    "course":"Data Science & Artificial Intelligence, third semester.",
    }
summaryDct = {
  "p1":"Experienced Co-Founder with a demonstrated history of working in the information technology and services industry. Skilled in Python, SQL, Pandas, and Command Line. Professional with a Bachelor's degree focused in Data Science and Artiﬁcial Intelligence from IESB.",
}
experienceA = {
  "position" :  "Data Engineer",
  "place" :  "Ministery of Communication",
  "finished" :  "April 2022",
  "started" :  "November 2021",
  "description" :  "Support the analysis of problems and technical solutions of data integration on projects related to internet connectivity in the national.",
}
experienceB ={
  "position" :  "President of a junior enterprise.",
  "place" :  "DatAí",
  "finished" :  "now",
  "started" :  "July 2021",
  "description" :  "DatAí is a Junior company of IESB University, that aims to provide a business experience to students of Data Science and related areas.",
}
skills = {
  "Python":["Pandas","Subprocess","Plotly","Boto3","PySpark",], 
  "SQL":["PostgreSQL","SQLlite",], 
  "Linux":["Bash","Command Line","Data Processing in Shell"], 
  "Cloud":["AWS"],
}

os.system("cd ..")
lst = os.listdir()
certificationsLst = [x.split('_')[1].split('.')[0] for x in lst if '.pdf' in x]
context = {
    "contact" : personalData,
    "experienceA" : experienceA,
    "experienceB" : experienceB,
    "skills": skills,
    "education": educationDct,
    "summary" : summaryDct,
    "certifications": certificationsLst,
  }
def resume(request):
  template = loader.get_template("myapp/resume.html")
  return HttpResponse(template.render(context))



# %%
