import pandas as pd
import json
from jinja2 import Template

# Read in the data
education = pd.read_csv("media/education.csv")
education.set_index("school")

experience = pd.read_csv("media/experience.csv")
experience.set_index("company")

certificates = pd.read_csv("media/certificates.csv")
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

with open("media/data.json") as f:
    dt = json.load(f)


with open("static/styles.css", 'r') as f:
    my_style = f.read()

my_css = f"""
<style>
    {my_style}
</style>
"""

with open("template/home.html", "w") as f:
    f.write("""
   <!-- index.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="utf-8">
      <title>RESUME_IN_PROGRESS</title>
   """ + my_css + f"""
   </head>
   <body>
      <div class="icon-container">
         <a href="{dt['linkedin']}">
            <img src="media/icons/linkedin.png" alt="LinkedIn">
            <span>{dt['linkedin']}</span>
         </a>
         <a href="{dt['github']}">
            <img src="media/icons/git.png" alt="GitHub">
            <span>{dt['github']}</span>
         </a>
         <a href="{dt['e-mail']}">
            <img src="media/icons/mail.png" alt="Email">
            <span>{dt['e-mail']}</span>
         </a>
         <a href="{dt['telegram']}">
            <img src="media/icons/telegram.png" alt="Telegram">
            <span>{dt['telegram']}</span>
         </a>
      </div>
      <h1>{dt['name']}</h1>
      <div>
         <br>
         <h3>About Me:</h3>
         <p>{dt["aboutme"]}</p>
         {table_html}
      </div>
   </body>
</html>
""")

