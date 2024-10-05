import config
from shared_func.html_func import create_html_resume, create_html_resume_pt
from shared_func.latex_func import generate_resume_tex, generate_resume_tex_pt
from shared_func.s3_func import upload_file_to_s3
import os
import qrcode



# Define the generate_resume_files function
def generate_resume_files(data):
    img = qrcode.make(data.get("site_link"))
    img.save(config.path_qr_code)

    create_html_resume(data, config.path_index_html)
    generate_resume_tex(data, config.path_resume_latex)

    # Example usage
    upload_file_to_s3(config.path_index_html, config.bucket_name, config.file_name_index)
    upload_file_to_s3(config.path_styles_css, config.bucket_name, config.file_name_styles)
    upload_file_to_s3(config.path_resume_pdf, config.bucket_name, config.file_name_resume)
    upload_file_to_s3(config.path_qr_code, config.bucket_name, config.file_name_qr_code)

# Define the generate_resume_files function
def generate_resume_files_pt(data):
    img = qrcode.make(data.get("site_link"))
    img.save(config.path_qr_code_pt)

    create_html_resume_pt(data, config.path_index_html_pt)
    generate_resume_tex_pt(data, config.path_resume_latex_pt)

    upload_file_to_s3(config.path_index_html_pt, config.bucket_name, config.file_name_index_pt)
    upload_file_to_s3(config.path_resume_pdf_pt, config.bucket_name, config.file_name_resume_pt)
    upload_file_to_s3(config.path_qr_code_pt, config.bucket_name, config.file_name_qr_code_pt)

# Generate both files
generate_resume_files(config.resume_data)
generate_resume_files_pt(config.resume_data_pt)

