import config
from shared_func.html_func import create_html_resume
from shared_func.latex_func import generate_resume_tex
from shared_func.s3_func import upload_file_to_s3
import os
import qrcode



# Define the generate_resume_files function
def generate_resume_files(data):

    img = qrcode.make(data.get("site_link"))
    img.save(config.path_qr_code)

    create_html_resume(data)
    generate_resume_tex(data, config.path_resume_latex)


    # Example usage
    upload_file_to_s3(config.path_resume_pdf, config.bucket_name, config.file_name_resume)
    upload_file_to_s3(config.path_index_html, config.bucket_name, config.file_name_index)
    upload_file_to_s3(config.path_styles_css, config.bucket_name, config.file_name_styles)
    upload_file_to_s3(config.path_qr_code, config.bucket_name, config.file_name_qr_code)

# Generate both files
generate_resume_files(config.resume_data)

