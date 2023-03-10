import pandas as pd
import json
from jinja2 import Template

# Read in the data
education = pd.read_csv("media/education.csv")
experience = pd.read_csv("media/experience.csv")

# create an empty string to hold the HTML code
html_educ = ""
# iterate through each row of the DataFrame
for _, row in education.iterrows():
    # create an HTML list item (li) for each row
    li = f"""
    <li>
        <ul>{row['degree']} in {row['field_of_study']}.</ul>
        <ul>At: {row['school']}.</ul> 
        <ul>Date: {row['start_date']} - {row['end_date']}.</ul>
    </li>
    """
    # append the list item to the HTML string
    html_educ += li

# wrap the HTML code in an unordered list (ul) tag
ul_educ = f"<ul>{html_educ}</ul>"

# create an empty string to hold the HTML code
html_exp = ""

# iterate through each row of the DataFrame
for _, row in experience.iterrows():
    # create an HTML list item (li) for each row
    li = f"""
    <li>
        <strong>{row['title']}</strong>({row["job_type"]})
        <ul>
            <li>At: {row['company']}, {row['where']}.</li>
            <li>Date: {row['start']} - {row['end']}.</li>
            <li>Description: {row['description']}.</li>
            <li>Skills: {row['skills']}.</li>
        </ul>
    </li>"""
    # append the list item to the HTML string
    html_exp += li

# wrap the HTML code in an unordered list (ul) tag
ul_exp = f"<ul>{html_exp}</ul>"

certificates = pd.read_csv("media/certificates.csv")
certificates['DATE'] = pd.to_datetime(certificates['DATE']).dt.date
certificates = certificates.sort_values('DATE', ascending=False).reset_index(drop=True)

READMEmd = certificates.to_html()

# Add the link to the curso column
certificates["COURSE"] = "<a href='" + certificates["LINK"] + "'>" + certificates["COURSE"] + "</a>"

# Drop the link column
certificates = certificates.drop(columns=["LINK"])

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

linkedin_img = "{{ url_for('static', filename='linkedin.png') }}"
git_img = "{{ url_for('static', filename='git.png') }}"
email_img = "{{ url_for('static', filename='mail.png') }}"
telegram_img = "{{ url_for('static', filename='telegram.png') }}"

with open("template/home.html", "w") as f:
    f.write("""
   <!-- index.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="utf-8">
      <title>RESUME_IN_PROGRESS</title>"""
   +my_css+
  f"""</head>
   <body>
      <div class="icon-container">
         <a href="{dt['linkedin']}">
            <img src=" """ + linkedin_img + f""" " alt="LinkedIn">
            <span>{dt['linkedin']}</span>
         </a>
         <a href="{dt['github']}">
            <img src=" """ + git_img + f""" " alt="GitHub">
            <span>{dt['github']}</span>
         </a>
         <a href="{dt['e-mail']}">
            <img src=" """ + email_img + f""" " alt="Email">

            <span>{dt['e-mail']}</span>
         </a>
         <a href="{dt['telegram']}">
            <img src=" """ + telegram_img + f""" " alt="Telegram">
            <span>{dt['telegram']}</span>
         </a>
      </div>
      <h1>{dt['name']}</h1>
      <div>
         <br>
         <h3>About Me:</h3>
         <p>{dt["aboutme"]}</p>
         <h3>Education:</h3>
        """+ul_educ+f"""
         <h3>Experience:</h3>
        """+ul_exp+f"""
         {table_html}
      </div>
   </body>
</html>
""")

