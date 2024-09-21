# config.py
bucket_name="s33ding"
path_resume_pdf = "latex/resume.pdf"
path_index_html = "site/index.html"
path_styles_css = "site/styles.css"

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
        "I am an accomplished data professional with nearly three years of experience in data engineering, "
        "including two years in a full data engineer role. My expertise includes crafting robust data pipelines, "
        "implementing efficient data lakes, and orchestrating seamless data integration within cloud environments. "
        "I have honed my skills in PySpark, Exploratory Data Analysis, serverless architecture, AWS Cloud services, "
        "Docker, and Linux. I actively manage data quality routines and implement automated testing to ensure data integrity. "
        "Currently, I am pursuing AWS Developer certification and studying for the KCNA exam while continuing my education in Machine Learning."
    ),
    "experience": [
        {
            "position": "Data Engineer (Full-Time)",
            "company": "Ti.Saúde",
            "location": "Recife, Brazil",
            "dates": "Jul 2022 - Present",
            "details": [
                "Create data pipelines",
                "Maintain and build data storage systems on the cloud to be used by other areas of the company",
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
        "institution": "The Higher Education Institute of Brasilia (IESB)",
        "dates": "Feb 2021 - Present"
    },
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
        {"language": "English", "certification": "TOEFL (Oct 2020)"},
        {"language": "English", "certification": "Casa Thomas Jefferson (Sep 2017)"}
    ],
    "resume_download_link": "https://s33ding.s3.us-east-1.amazonaws.com/resume.pdf"
}
