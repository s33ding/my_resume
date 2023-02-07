import pandas as pd
import json
from jinja2 import Template

# Read in the data
education = pd.read_csv("midia/education.csv")
education.set_index("school")

experience = pd.read_csv("midia/experience.csv")
experience.set_index("company")

certificates = pd.read_csv("midia/certificates.csv")
certificates['date'] = pd.to_datetime(certificates['date']).dt.date
certificates = certificates.sort_values('date', ascending=False).reset_index(drop=True)

READMEmd = certificates.to_html()

# Add the link to the curso column
certificates["curso"] = "<a href='" + certificates["link"] + "'>" + certificates["curso"] + "</a>"

# Drop the link column
certificates = certificates.drop(columns=["link"])

# Create a Jinja template for the table
table_template = """
<table>
    <tr>
    {% for column in table.columns %}
        <th>{{ column }}</th>
    {% endfor %}
    </tr>
    {% for row in table.values %}
    <tr>
    {% for cell in row %}
        <td>{{ cell }}</td>
    {% endfor %}
    </tr>
    {% endfor %}
</table>
"""

# Render the table using Jinja
template = Template(table_template)
table_html = template.render(table=certificates)

with open("midia/aboutMe.json") as f:
    dt = json.load(f)

with open("README.md",'w') as f:
    f.write(READMEmd)

with open("resume_in_progress.html","w") as f:
    f.write(f"""
   <!-- index.html -->

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="utf-8">
      <title>RESUME_IN_PROGRESS</title>
      <link rel="stylesheet" href="midia/style.css"> 
   </head>
   <body>
     <h1>{dt['name']}</h1>
      <br>
        <h3>About Me:</h3>
        <p>{dt["aboutme"]}</p>
        {table_html}
    </body>
    """)

