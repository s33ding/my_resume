import config

# Define the functions for generating the files
def create_html_resume(data):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{data['name']} - Resume</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>{data['name']}</h1>
                <p>{data['title']}</p>
                <p>{data['contact']['city']} • {data['contact']['phone']} • 
                <a href="mailto:{data['contact']['email']}">{data['contact']['email']}</a> • 
                <a href="{data['contact']['linkedin']}">LinkedIn</a> • 
                <a href="{data['contact']['github']}">GitHub</a></p>
            </div>
            <div class="section about">
                <h3>About Me</h3>
                <p>{data['about']}</p>
            </div>
            <div class="section experience">
                <h3>Professional Experience</h3>
    """
    for job in data['experience']:
        html_content += f"""
        <div class="experience-item">
            <h4>{job['position']} <span>{job['dates']}</span></h4>
            <p>{job['company']}, {job['location']}</p>
            <ul>
        """
        for detail in job['details']:
            html_content += f"<li>{detail}</li>"
        html_content += "</ul></div>"
    
    html_content += f"""
            </div>
            <div class="section education">
                <h3>Education</h3>
                <p>{data['education']['degree']} <br>
                {data['education']['institution']} <br>
                <em>{data['education']['dates']}</em></p>
            </div>
            <div class="section skills">
                <h3>Technical Skills</h3>
                <ul>
    """
    for skill in data['skills']:
        html_content += f"<li>{skill}</li>"
    
    html_content += """
                </ul>
            </div>
            <div class="section languages">
                <h3>Languages</h3>
                <ul>
    """
    for language in data['languages']:
        html_content += f"<li><strong>{language['language']}:</strong> {language['certification']}</li>"
    
    html_content += f"""
                </ul>
            </div>
            <div class="footer">
                <button onclick="window.location.href='{data['resume_download_link']}';" class="download-btn">Download Resume</button>
                <p>View certificates: <a href="https://github.com/s33ding/my_resume/tree/main/my_certificates">Link</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    with open("site/index.html", "w") as file:
        file.write(html_content)


