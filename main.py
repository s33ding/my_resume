import config
from shared_func.html_func import create_html_resume
from shared_func.latex_func import generate_resume_tex
from shared_func.s3_func import upload_file_to_s3
import os



# Define the generate_resume_files function
def generate_resume_files(data):
    create_html_resume(data)
    generate_resume_tex(data)
    upload_file_to_s3(config.path_resume_pdf, config.bucket_name, "resume.pdf")
    upload_file_to_s3(config.path_index_html, config.bucket_name, "index.html")
    upload_file_to_s3(config.path_styles_css, config.bucket_name, "styles.css")
    

# Generate both files
generate_resume_files(config.resume_data)

