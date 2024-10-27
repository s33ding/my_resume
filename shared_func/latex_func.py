from pylatex import Document, Section, Tabularx, Command, Package, NewLine, Itemize, NoEscape
from pylatex.utils import italic, bold

def generate_resume_tex(resume_data, path):
    # Create a new LaTeX document
    doc = Document(documentclass="article", document_options="letterpaper,11pt")

    # Add necessary packages
    doc.packages.append(Package("latexsym"))
    doc.packages.append(Package("fullpage", options="empty"))
    doc.packages.append(Package("titlesec"))
    doc.packages.append(Package("marvosym"))
    doc.packages.append(Package("color", options="usenames,dvipsnames"))
    doc.packages.append(Package("verbatim"))
    doc.packages.append(Package("enumitem"))
    doc.packages.append(Package("hyperref", options="hidelinks"))
    doc.packages.append(Package("fancyhdr"))
    doc.packages.append(Package("babel", options="english"))
    doc.packages.append(Package("tabularx"))
    doc.packages.append(Package("multicol"))
    doc.packages.append(Package("baskervillef"))
    doc.packages.append(Package("fontenc", options="T1"))


    # Add custom settings
    doc.preamble.append(NoEscape(r"\pagestyle{fancy}"))
    doc.preamble.append(NoEscape(r"\fancyhf{}"))
    doc.preamble.append(NoEscape(r"\fancyfoot{}"))
    doc.preamble.append(NoEscape(r"\setlength{\footskip}{10pt}"))
    doc.preamble.append(NoEscape(r"\renewcommand{\headrulewidth}{0pt}"))
    doc.preamble.append(NoEscape(r"\renewcommand{\footrulewidth}{0pt}"))
    doc.preamble.append(NoEscape(r"\addtolength{\oddsidemargin}{0.0in}"))
    doc.preamble.append(NoEscape(r"\addtolength{\evensidemargin}{0.0in}"))
    doc.preamble.append(NoEscape(r"\addtolength{\textwidth}{0.0in}"))

    # Adjust the top margin and vertical offset
    doc.preamble.append(NoEscape(r"\addtolength{\topmargin}{0.2in}"))  # Further decrease top margin
    doc.preamble.append(NoEscape(r"\addtolength{\textheight}{1.0in}"))  # Increase text height to fit more content
    doc.preamble.append(NoEscape(r"\urlstyle{same}"))
    doc.preamble.append(NoEscape(r"\raggedright"))
    doc.preamble.append(NoEscape(r"\setlength{\tabcolsep}{0in}"))
    doc.preamble.append(NoEscape(r"\titleformat{\section}{\it\vspace{3pt}}{}{0em}{}[\color{black}\titlerule\vspace{-5pt}]"))
    doc.preamble.append(NoEscape(r"\pdfgentounicode=1"))


    # Adjust the top margin and vertical offset
    doc.preamble.append(NoEscape(r"\addtolength{\topmargin}{-1.0in}"))  # Further decrease top margin
    doc.preamble.append(NoEscape(r"\addtolength{\textheight}{1.0in}"))  # Increase text height to fit more content
    doc.preamble.append(NoEscape(r"\urlstyle{same}"))
    doc.preamble.append(NoEscape(r"\raggedright"))
    doc.preamble.append(NoEscape(r"\setlength{\tabcolsep}{0in}"))
    doc.preamble.append(NoEscape(r"\titleformat{\section}{\it\vspace{3pt}}{}{0em}{}[\color{black}\titlerule\vspace{-5pt}]"))
    doc.preamble.append(NoEscape(r"\pdfgentounicode=1"))

    # Define custom commands
    doc.preamble.append(NoEscape(r"\newcommand{\resumeItem}[1]{\item{#1 \vspace{-3pt}}}"))  # Reduce item spacing
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubheading}[4]{\vspace{-1pt}\item"
                                 r"\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}"
                                 r"\textbf{#1} & #2 \\"
                                 r"\textit{\small #3} & \textit{\small #4} \\"
                                 r"\end{tabular*}\vspace{-8pt}}"))  # Reduce subheading spacing
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-2pt}}"))  # Reduce sub-item spacing
    doc.preamble.append(NoEscape(r"\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}"))
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}, itemsep=0pt, parsep=0pt]}"))  # Compact list
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}"))
    doc.preamble.append(NoEscape(r"\newcommand{\resumeItemListStart}{\begin{itemize}[itemsep=0pt, parsep=0pt]}"))  # Compact list
    doc.preamble.append(NoEscape(r"\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-1pt}}"))  # Reduce spacing after item list

    # Title Section
    with doc.create(Section("", numbering=False)) as title:
        title.append(NoEscape(r"\begin{center}"))
        title.append(NoEscape(f"{{\\LARGE {resume_data['name']}}} \\\\ \\vspace{{5pt}}"))
        title.append(NoEscape(f"{{\\large {resume_data['title']}}} \\\\ \\vspace{{5pt}}"))
        title.append(NoEscape(r"\end{center}"))
        title.append(NoEscape(r"\begin{center}"))
        contact = resume_data["contact"]
        title.append(NoEscape(
            f"City: {contact['city']} \\quad \\textbullet \\quad "
            f"\\href{{https://wa.me/qr/UYOUX2DZ7BYHI1}}{{Phone: +55 (61) 98234-0088}} \\quad \\textbullet \\quad "
            f"\\href{{https://www.linkedin.com/in/s33ding/}}{{LinkedIn: @s33ding}} \\quad \\textbullet \\quad "
            f"\\href{{mailto:{contact['email']}}}{{Email: {contact['email']}}} \\quad \\textbullet \\quad "
            f"\\href{{{contact['github']}}}{{Github: @s33ding}}"
        ))
        title.append(NoEscape(r"\end{center}"))

    # About Me Section
    with doc.create(Section('About Me', numbering=False)):
        doc.append(resume_data['about'])

    # Professional Experience Section
    with doc.create(Section('Professional Experience', numbering=False)):
        doc.append(NoEscape(r"\resumeSubHeadingListStart"))
        for job in resume_data['experience']:
            doc.append(NoEscape(
                r"\resumeSubheading"
                f"{{{job['position']}}}{{{job['dates']}}}"
                f"{{{job['company']}}}{{{job['location']}}}"
            ))
            doc.append(NoEscape(r"\resumeItemListStart"))
            for detail in job['details']:
                doc.append(NoEscape(rf"\resumeItem{{{detail}}}"))
            doc.append(NoEscape(r"\resumeItemListEnd"))
        doc.append(NoEscape(r"\resumeSubHeadingListEnd"))

    # Education Section
    with doc.create(Section('Education', numbering=False)):
        doc.append(NoEscape(r"\resumeSubHeadingListStart"))
        education = resume_data['education']
        doc.append(NoEscape(
            f"\\resumeSubheading"
            f"{{{education['degree']}}}{{{education['dates']}}}"
            f"{{{education['institution']}}}{{}}"
        ))
        doc.append(NoEscape(r"\resumeSubHeadingListEnd"))
        doc.append(NoEscape(r"\resumeSubHeadingListStart"))
        education = resume_data['education-2']
        doc.append(NoEscape(
            f"\\resumeSubheading"
            f"{{{education['degree']}}}{{{education['dates']}}}"
            f"{{{education['institution']}}}{{}}"
        ))
        doc.append(NoEscape(r"\resumeSubHeadingListEnd"))

    # Technical Skills Section with two columns
    with doc.create(Section('Technical Skills', numbering=False)):
        doc.append(NoEscape(r"\begin{multicols}{2}"))
        doc.append(NoEscape(r"\resumeItemListStart"))
        for skill in resume_data['skills']:
            doc.append(NoEscape(f"\\item {skill}"))
        doc.append(NoEscape(r"\resumeItemListEnd"))
        doc.append(NoEscape(r"\end{multicols}"))

    # Languages Section
    with doc.create(Section('Languages', numbering=False)):
        with doc.create(Itemize(options=NoEscape("leftmargin=0.15in, label={}"))) as itemize:
            for language in resume_data['languages']:
                itemize.add_item(NoEscape(
                    f"\\textbf{{{language['language']}}}: {language['certification']} "
                    f"- \\href{{{language['link']}}}{{View certificate: (Link)}}"
                ))

    doc.generate_pdf(path, clean_tex=False)


def generate_resume_tex_pt(resume_data, path):
    # Create a new LaTeX document
    doc = Document(documentclass="article", document_options="letterpaper,11pt")

    # Add necessary packages
    doc.packages.append(Package("latexsym"))
    doc.packages.append(Package("fullpage", options="empty"))
    doc.packages.append(Package("titlesec"))
    doc.packages.append(Package("marvosym"))
    doc.packages.append(Package("color", options="usenames,dvipsnames"))
    doc.packages.append(Package("verbatim"))
    doc.packages.append(Package("enumitem"))
    doc.packages.append(Package("hyperref", options="hidelinks"))
    doc.packages.append(Package("fancyhdr"))
    doc.packages.append(Package("babel", options="english"))
    doc.packages.append(Package("tabularx"))
    doc.packages.append(Package("multicol"))
    doc.packages.append(Package("baskervillef"))
    doc.packages.append(Package("fontenc", options="T1"))

    # Add custom settings
    doc.preamble.append(NoEscape(r"\pagestyle{fancy}"))
    doc.preamble.append(NoEscape(r"\fancyhf{}"))
    doc.preamble.append(NoEscape(r"\fancyfoot{}"))
    doc.preamble.append(NoEscape(r"\setlength{\footskip}{10pt}"))
    doc.preamble.append(NoEscape(r"\renewcommand{\headrulewidth}{0pt}"))
    doc.preamble.append(NoEscape(r"\renewcommand{\footrulewidth}{0pt}"))
    doc.preamble.append(NoEscape(r"\addtolength{\oddsidemargin}{0.0in}"))
    doc.preamble.append(NoEscape(r"\addtolength{\evensidemargin}{0.0in}"))
    doc.preamble.append(NoEscape(r"\addtolength{\textwidth}{0.0in}"))
    # Adjust the top margin and vertical offset
    doc.preamble.append(NoEscape(r"\addtolength{\topmargin}{-0.7in}"))  # Further decrease top margin
    doc.preamble.append(NoEscape(r"\addtolength{\textheight}{1.4in}"))  # Increase text height to fit more content
    doc.preamble.append(NoEscape(r"\urlstyle{same}"))
    doc.preamble.append(NoEscape(r"\raggedright"))
    doc.preamble.append(NoEscape(r"\setlength{\tabcolsep}{0in}"))
    doc.preamble.append(NoEscape(r"\titleformat{\section}{\it\vspace{3pt}}{}{0em}{}[\color{black}\titlerule\vspace{-5pt}]"))
    doc.preamble.append(NoEscape(r"\pdfgentounicode=1"))

    # Define custom commands
    doc.preamble.append(NoEscape(r"\newcommand{\resumeItem}[1]{\item{#1 \vspace{-3pt}}}"))  # Reduce item spacing
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubheading}[4]{\vspace{-1pt}\item"
                                 r"\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}"
                                 r"\textbf{#1} & #2 \\"
                                 r"\textit{\small #3} & \textit{\small #4} \\"
                                 r"\end{tabular*}\vspace{-8pt}}"))  # Reduce subheading spacing
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-2pt}}"))  # Reduce sub-item spacing
    doc.preamble.append(NoEscape(r"\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}"))
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}, itemsep=0pt, parsep=0pt]}"))  # Compact list
    doc.preamble.append(NoEscape(r"\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}"))
    doc.preamble.append(NoEscape(r"\newcommand{\resumeItemListStart}{\begin{itemize}[itemsep=0pt, parsep=0pt]}"))  # Compact list
    doc.preamble.append(NoEscape(r"\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-1pt}}"))  # Reduce spacing after item list

    # Title Section
    with doc.create(Section("", numbering=False)) as title:
        title.append(NoEscape(r"\begin{center}"))
        title.append(NoEscape(f"{{\\LARGE {resume_data['name']}}} \\\\ \\vspace{{5pt}}"))
        title.append(NoEscape(f"{{\\large {resume_data['title']}}} \\\\ \\vspace{{5pt}}"))
        title.append(NoEscape(r"\end{center}"))
        title.append(NoEscape(r"\begin{center}"))

        contact = resume_data["contact"]

        title.append(NoEscape(r"\small"))  # Make only this section very small
        title.append(NoEscape(
            f"Cidade: {contact['city']} \\quad \\textbullet \\quad "
            f"\\href{{https://wa.me/qr/UYOUX2DZ7BYHI1}}{{Celular: +55 (61) 98234-0088}} \\quad \\textbullet \\quad "
            f"\\href{{https://www.linkedin.com/in/s33ding/}}{{LinkedIn: @s33ding}} \\quad \\textbullet \\quad "
            f"\\href{{mailto:{contact['email']}}}{{Email: {contact['email']}}} \\quad \\textbullet \\quad "
            f"\\href{{{contact['github']}}}{{Github: @s33ding}}"
        ))
        title.append(NoEscape(r"\normalsize"))  # Return to normal size for the rest of the document
        title.append(NoEscape(r"\end{center}"))


    # About Me Section
    with doc.create(Section('Sobre Mim', numbering=False)):
        doc.append(resume_data['about'])

    # Professional Experience Section
    with doc.create(Section('Experiência Profissional', numbering=False)):
        doc.append(NoEscape(r"\resumeSubHeadingListStart"))
        for job in resume_data['experience']:
            doc.append(NoEscape(
                r"\resumeSubheading"
                f"{{{job['position']}}}{{{job['dates']}}}"
                f"{{{job['company']}}}{{{job['location']}}}"
            ))
            doc.append(NoEscape(r"\resumeItemListStart"))
            for detail in job['details']:
                doc.append(NoEscape(rf"\resumeItem{{{detail}}}"))
            doc.append(NoEscape(r"\resumeItemListEnd"))
        doc.append(NoEscape(r"\resumeSubHeadingListEnd"))

    # Education Section
    with doc.create(Section('Formação Acadêmica', numbering=False)):
        doc.append(NoEscape(r"\resumeSubHeadingListStart"))
        education = resume_data['education']
        doc.append(NoEscape(
            f"\\resumeSubheading"
            f"{{{education['degree']}}}{{{education['dates']}}}"
            f"{{{education['institution']}}}{{}}"
        ))
        doc.append(NoEscape(r"\resumeSubHeadingListEnd"))
        doc.append(NoEscape(r"\resumeSubHeadingListStart"))
        education = resume_data['education-2']
        doc.append(NoEscape(
            f"\\resumeSubheading"
            f"{{{education['degree']}}}{{{education['dates']}}}"
            f"{{{education['institution']}}}{{}}"
        ))
        doc.append(NoEscape(r"\resumeSubHeadingListEnd"))

    # Technical Skills Section with two columns
    with doc.create(Section('Competências Técnicas', numbering=False)):
        doc.append(NoEscape(r"\begin{multicols}{2}"))
        doc.append(NoEscape(r"\resumeItemListStart"))
        for skill in resume_data['skills']:
            doc.append(NoEscape(f"\\item {skill}"))
        doc.append(NoEscape(r"\resumeItemListEnd"))
        doc.append(NoEscape(r"\end{multicols}"))

    # Languages Section
    with doc.create(Section('Idiomas', numbering=False)):
        with doc.create(Itemize(options=NoEscape("leftmargin=0.15in, label={}"))) as itemize:
            for language in resume_data['languages']:
                itemize.add_item(NoEscape(
                    f"\\textbf{{{language['language']}}}: {language['certification']} "
                    f"- \\href{{{language['link']}}}{{Ver certificado: (Link)}}"
                ))

    doc.generate_pdf(path, clean_tex=False)
