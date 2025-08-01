import os

bucket_name = "s33ding"
bucket_name = "robertomdiniz"

# Full paths
path_resume_latex = "latex/roberto-resume"
path_resume_latex_pt = "latex/roberto-resume-pt-br"
path_resume_pdf = f"{path_resume_latex}.pdf"
path_resume_pdf_pt = f"{path_resume_latex_pt}.pdf"
path_index_html = "site/index.html"
path_index_html_pt = "site/index-pt-br.html"
path_accomplishments_html = "accomplishments.html"

path_styles_css = "site/styles.css"
path_qr_code = "site/media/qr_code.png"
path_qr_code_pt = "site/media/qr_code-pt-br.png"

accomplishments_csv = "my_certificates/learning_records/accomplishments.csv"
accomplishments_html = "site/accomplishments.html"

# Extract file names from paths
file_name_resume = path_resume_pdf.split("/")[-1]
file_name_resume_pt = path_resume_pdf_pt.split("/")[-1]
file_name_index = path_index_html.split("/")[-1]
file_name_index_pt = path_index_html_pt.split("/")[-1]
file_name_styles = path_styles_css.split("/")[-1]
file_name_qr_code = path_qr_code.split("/")[-1]
file_name_qr_code_pt = path_qr_code_pt.split("/")[-1]

# Ensure directory exists
for path in [path_resume_pdf, path_resume_pdf_pt, path_index_html, path_styles_css, path_qr_code, path_qr_code_pt]:
    os.makedirs(os.path.dirname(path), exist_ok=True)


# Resume Data
resume_data = {
    "name": "Roberto Moreira Diniz",
    "title": "Data Engineer",
    "contact": {
        "city": "Brasilia, Brazil",
        "phone": "+55(61) 98234-0088",
        "email": "robertomdiniz@protonmail.com",
        "linkedin": "https://www.linkedin.com/in/s33ding/",
        "github": "https://github.com/s33ding"
    },
    "about": (
        "I am a data engineer with three years of experience building scalable data pipelines, "
        "managing data lakes, and integrating cloud solutions. Skilled in PySpark, AWS, Docker, and Linux, "
        "I focus on data quality, automation, and efficiency. I hold the AWS Developer Associate and KCNA certifications, "
        "and am currently preparing for the CKA and AWS DevOps Engineer Professional exams."
    ),
    "experience": [
        {
            "position": "Data Engineer (Full-Time)",
            "company": "Ti.Saúde",
            "location": "Recife, Brazil",
            "dates": "Jul 2022 - Present",
            "details": [
                "Create data pipelines",
                "Maintain and build data storage systems in the cloud to be used by other areas of the company",
                "Analyze and extract insights from the data"
            ]
        },
        {
            "position": "Data Engineer (Internship)",
            "company": "Ministry of Communications (Government)",
            "location": "Brasilia, Federal District, Brazil",
            "dates": "Nov 2021 - Apr 2022",
            "details": [
                "Support the analysis of problems and technical solutions of data integration on projects related to internet connectivity in the national territory"
            ]
        }
    ],
    "education": {
        "degree": "Bachelor’s degree in Data Science and Artificial Intelligence",
        "institution": "Instituto de Educação Superior de Brasília (IESB)",
        "dates": "Feb 2021 - Present"
    },
    "education-2": {
            "degree": "Bachelor’s degree in Architecture and Urbanism",
            "institution": "Centro Universitário de Brasília (UniCEUB)",
            "dates": "Graduated on September 16, 2020"
        },
    "certificates": [
        {
        "course": "AWS Certified Cloud Practitioner (CLF-C01)",
        "link": "https://www.credly.com/badges/e84a8faf-0385-4c17-b24e-f8caa5ff1e88/linked_in_profile",
        "date": "2023-11-20",
        "expires": "2028-03-17"
        },
        {
        "course": "AWS Certified Developer Associate (DVA-C02)",
        "link": "https://www.credly.com/badges/e84a8faf-0385-4c17-b24e-f8caa5ff1e88/linked_in_profile",
        "date": "2023-11-20",
        "expires": "2028-03-17"
        }
    ]
    ,
    "skills": [
        "Programming: Python, SQL, Bash",
        "Cloud: AWS (Boto3, Lambda, Glue, S3, EC2, AWS CLI, Terraform, VPC, RDS, Secret Manager, IAM, SSM, QuickSight, AWS Lake Formation, Amazon Athena, EventBridge, SNS, Rekognition, RedShift, DynamoDB)",
        "Databases: PostgreSQL, MySQL, Redis, MongoDB, Hadoop",
        "Data Analysis: Pandas, EDA, Probability, Statistics, Sympy, Scipy, Itertools, NumPy",
        "Data Processing: Docker, Git, PySpark, Shell scripting, Regex, Vim, Airflow, Crontab",
        "Machine Learning: Scikit-learn, MLlib (Spark), spaCy",
        "Others: Flask, Django, PowerBI, Plotly, MetaBase, Linux Servers"
    ],
    "languages": [
            {"language": "English", "certification": "TOEFL (Oct 2020)", "link":"https://github.com/s33ding/my_resume/blob/main/my_certificates/english_TOEFL_my_score.pdf"},
            {"language": "English", "certification": "Casa Thomas Jefferson (Sep 2017)","link":"https://github.com/s33ding/my_resume/blob/main/my_certificates/english_Casa%20Thomas%20Jefferson.pdf"}
    ],
    "resume_download_link": f"https://{bucket_name}.s3.amazonaws.com/{file_name_resume}",
    "qr_code": f"https://{bucket_name}.s3.amazonaws.com/qr_code.png",
    "site_translated": f"https://{bucket_name}.s3.amazonaws.com/{file_name_index_pt}",
    "site_link": f"https://{bucket_name}.s3.amazonaws.com/{file_name_index}",
    "accomplishments": f"https://{bucket_name}.s3.amazonaws.com/{path_accomplishments_html}"
}


resume_data_pt = {
  "name": "Roberto Moreira Diniz",
  "title": "Engenheiro de Dados",
  "contact": {
    "city": "Brasília, Brasil",
    "phone": "+55(61) 98234-0088",
    "email": "robertomdiniz@protonmail.com",
    "linkedin": "https://www.linkedin.com/in/s33ding/",
    "github": "https://github.com/s33ding"
  },
  "about": (
    "Sou um engenheiro de dados com três anos de experiência no desenvolvimento de pipelines escaláveis, "
    "gerenciamento de data lakes e integração de soluções em nuvem. "
    "Especialista em PySpark, AWS, Docker e Linux, com foco na qualidade de dados, automação e eficiência. "
    "Possuo as certificações AWS Developer Associate e KCNA. "
    "Atualmente, estou me preparando para os exames CKA e AWS DevOps Engineer Professional, "
    "com o objetivo de expandir meu conhecimento em Kubernetes e práticas de DevOps."
    ),
  "experience": [
    {
      "position": "Engenheiro de Dados (Tempo Integral)",
      "company": "Ti.Saúde",
      "location": "Recife, Brasil",
      "dates": "Jul 2022 - Presente",
      "details": [
        "Criar pipelines de dados",
        "Manter e construir sistemas de armazenamento de dados na nuvem, utilizados por outras áreas da empresa",
        "Analisar e extrair insights dos dados"
      ]
    },
    {
      "position": "Engenheiro de Dados (Estágio)",
      "company": "Ministério das Comunicações (Governo)",
      "location": "Brasília, Distrito Federal, Brasil",
      "dates": "Nov 2021 - Abr 2022",
      "details": [
        "Apoiar a análise de problemas e soluções técnicas de integração de dados em projetos relacionados à conectividade de internet no território nacional"
      ]
    }
  ],
  "education": {
    "degree": "Bacharelado em Ciência de Dados e Inteligência Artificial",
    "institution": "Instituto de Educação Superior de Brasília (IESB)",
    "dates": "Fev 2021 - Presente"
  },
  "education-2": {
      "degree": "Bacharelado em Arquitetura e Urbanismo",
      "institution": "Centro Universitário de Brasília (UniCEUB)",
      "dates": "Graduado em 16 de Setembro de 2020"
    },
  "certificates": [
        {
        "course": "AWS Certified Cloud Practitioner (CLF-C01)",
        "link": "https://www.credly.com/badges/e84a8faf-0385-4c17-b24e-f8caa5ff1e88/linked_in_profile",
        "platform": "Treinamento e Certificação da Amazon Web Services",
        "date": "2023-11-20",
        "expires": "2028-03-17"
        },
        {
        "course": "AWS Certified Developer Associate (DVA-C02)",
        "link": "https://www.credly.com/badges/c90e1b8d-a98d-41f7-9084-724fbf3660bd/linked_in_profile",
        "platform": "Treinamento e Certificação da Amazon Web Services",
        "date": "2025-03-17",
        "expires": "2028-03-17"
        },

    ],

  "skills": [
    "Programação: Python, SQL, Bash",
    "Nuvem: AWS (Boto3, Lambda, Glue, S3, EC2, AWS CLI, Terraform, VPC, RDS, Secret Manager, IAM, SSM, QuickSight, AWS Lake Formation, Amazon Athena, EventBridge, SNS, Rekognition, RedShift, DynamoDB)",
    "Bancos de Dados: PostgreSQL, MySQL, Redis, MongoDB, Hadoop",
    "Análise de Dados: Pandas, AED, Probabilidade, Estatística, Sympy, Scipy, Itertools, NumPy",
    "Processamento de Dados: Docker, Git, PySpark, Shell scripting, Regex, Vim, Airflow, Crontab",
    "Machine Learning: Scikit-learn, MLlib (Spark), spaCy",
    "Outros: Flask, Django, PowerBI, Plotly, MetaBase, Servidores Linux"
  ],
  "languages": [
    {
      "language": "Inglês",
      "certification": "TOEFL (Out 2020)",
      "link": "https://github.com/s33ding/my_resume/blob/main/my_certificates/english_TOEFL_my_score.pdf"
    },
    {
      "language": "Inglês",
      "certification": "Casa Thomas Jefferson (Set 2017)",
      "link": "https://github.com/s33ding/my_resume/blob/main/my_certificates/english_Casa%20Thomas%20Jefferson.pdf"
    }
  ],
  "resume_download_link": f"https://{bucket_name}.s3.amazonaws.com/{file_name_resume_pt}",
  "qr_code": f"https://{bucket_name}.s3.amazonaws.com/qr_code-pt-br.png",
    "site_translated": f"https://{bucket_name}.s3.amazonaws.com/{file_name_index}",
    "site_link": f"https://{bucket_name}.s3.amazonaws.com/{file_name_index_pt}",
    "accomplishments": f"https://{bucket_name}.s3.amazonaws.com/{path_accomplishments_html}"
}

