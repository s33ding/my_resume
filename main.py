#%%
import pandas as pd
import json

education = pd.read_csv("midia/education.csv")
education.set_index("school")

experience = pd.read_csv("midia/experience.csv")
experience.set_index("company")

certificates = pd.read_csv("midia/certificates.csv") 
certificates['date'] = certificates['date'].apply(lambda x: pd.to_datetime(x))
certificates = certificates.sort_values('date', ascending=False).reset_index(drop=True)
certificates.head()
certificates = certificates.to_html() 

with open("midia/aboutMe.json") as f:
    dt = json.load(f)

with open("README.md",'w') as f:
    f.write(certificates)

with open("resume_in_progress.html","w") as f:
    f.write(f"""
   <!-- index.html -->

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="utf-8">
      <title>RESUME_IN_PROGRESS</title>
      <link rel="stylesheet" href="midia/mystyle.css"> 
   </head>
   <body>
     <h1>{dt['name']}</h1>
      <br>
        <h3>About Me:</h3>
        <p>{dt["aboutme"]}</p>
    <table>
        {"""
        """}
    </table>
    </body>
    """)
    
