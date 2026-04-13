from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

# ===== Colors =====
MSU_MAROON = colors.HexColor("#660000")
LIGHT_GRAY = colors.HexColor("#666666")
YELLOW_HIGHLIGHT = colors.HexColor("#FFFF00")

# ===== Configuration =====
# Update these fields for each job application
COMPANY_NAME = "Affirm"
HIRING_MANAGER = "Hiring Team"  # or use actual name if known
POSITION_TITLE = "Software Engineer, Early Career"
DATE = "January 10, 2026"

# Optional: Customize the body paragraphs
CUSTOM_INTRO = (
    f"I am writing to express my strong interest in the {POSITION_TITLE} position at Affirm. "
    "Having followed Affirm's mission to reinvent credit by making it honest and friendly, I am inspired by the "
    "impact your team has on giving consumers financial flexibility without hidden fees. As a Master of Science "
    "candidate in Software Engineering at Mississippi State University with a 4.0 GPA, I am eager to leverage my "
    "full-stack development skills and passion for scalable software to contribute to your engineering team."
)

CUSTOM_BODY = (
    "In my current role as Technology & Support Services Coordinator at MSU Libraries, I have honed my ability "
    "to take complex problems and transform them into efficient technical solutions. "
    "I have designed and built automation tools and desktop applications that directly interact with multiple "
    "software components to enhance operational workflows. My experience managing large codebases and integrating "
    "systems via RESTful APIs has prepared me to write the clear, testable, and extensible code that Affirm values. "
    "Whether debugging legacy systems or architecting new analytics dashboards using Angular and React, "
    "I prioritize balancing speed with quality to ensure system reliability."
)

CUSTOM_CLOSING = (
    "I am drawn to Affirm not only for its technical challenges but also for its collaborative, people-first culture. "
    "I thrive in environments where ownership and proactive feedback are encouraged, and I am excited about the "
    "opportunity to collaborate with a global engineering team, whether in-person in San Francisco or remotely. "
    "I am confident that my technical foundation and commitment to continuous growth would make me a valuable addition "
    "to the Affirm team."
)

# Template detection for highlighting
IS_TEMPLATE = False  # Disabled - update COMPANY_NAME as needed per application

# ===== Output file =====
filepath = "Brandon_Temple_Cover_Letter.pdf"

styles = getSampleStyleSheet()


def ascii_clean(text: str) -> str:
    """Ensure ASCII-safe text (no em/en dash etc.)."""
    return text.replace("—", "-").replace("–", "-")


# ===== Styles =====
header_name = ParagraphStyle(
    "header_name",
    parent=styles["Heading1"],
    alignment=TA_LEFT,
    fontSize=24,
    textColor=MSU_MAROON,
    fontName="Helvetica-Bold",
    leading=28,
    spaceAfter=4,
)

contact_info = ParagraphStyle(
    "contact_info",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    textColor=LIGHT_GRAY,
    leading=14,
    spaceAfter=20,
)

date_style = ParagraphStyle(
    "date_style",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    leading=14,
    spaceAfter=8,
)

address_style = ParagraphStyle(
    "address_style",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    leading=14,
    spaceAfter=12,
    backColor=YELLOW_HIGHLIGHT if IS_TEMPLATE else None,
)

salutation = ParagraphStyle(
    "salutation",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    fontName="Helvetica",
    leading=14,
    spaceAfter=10,
    backColor=YELLOW_HIGHLIGHT if IS_TEMPLATE else None,
)

body_text = ParagraphStyle(
    "body_text",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    leading=14,
    spaceAfter=10,
    textColor=colors.HexColor("#333333"),
)

closing_style = ParagraphStyle(
    "closing_style",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    leading=14,
    spaceAfter=24,
)

signature_style = ParagraphStyle(
    "signature_style",
    parent=styles["BodyText"],
    alignment=TA_LEFT,
    fontSize=10,
    fontName="Helvetica-Bold",
    leading=14,
)

width, height = letter
HEADER_H = 2.0 * inch  # header strip height


# ===== Page header drawing =====
def on_page(canvas, doc):
    canvas.saveState()

    # Full-width maroon header bar
    canvas.setFillColor(MSU_MAROON)
    canvas.rect(0, height - HEADER_H, width, HEADER_H, fill=1, stroke=0)

    # Header text
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 26)
    canvas.drawString(0.75 * inch, height - 0.5 * inch, "BRANDON TEMPLE")
    
    canvas.setFont("Helvetica", 11)
    canvas.drawString(0.75 * inch, height - 0.75 * inch, "SOFTWARE ENGINEER")

    canvas.setFont("Helvetica", 10)
    contact_lines = [
        "Starkville, MS",
        "(601) 934-9208",
        "bt1142@msstate.edu",
        "github.com/bt1142msstate",
    ]

    y = height - 1.05 * inch
    for line in contact_lines:
        canvas.drawString(0.75 * inch, y, ascii_clean(line))
        y -= 0.22 * inch

    canvas.restoreState()


# ===== Body frame (below header) =====
frame = Frame(
    x1=0.75 * inch,
    y1=0.75 * inch,
    width=width - 1.5 * inch,
    height=height - HEADER_H - 1.0 * inch,  # Ensure content stays below header
    id="body",
)

doc = BaseDocTemplate(
    filepath,
    pagesize=letter,
    pageTemplates=[PageTemplate(id="main", frames=[frame], onPage=on_page)],
)

story = []

# ===== Salutation =====
story.append(Paragraph("Dear Hiring Team,", salutation))

# ===== Body Paragraphs =====

# Introduction
intro = CUSTOM_INTRO or (
    f"I am excited to express my interest in the {POSITION_TITLE} position at National General. As a Master of Science candidate "
    "in Software Engineering at Mississippi State University with a 4.0 GPA, I bring proven experience designing and building "
    "enterprise web applications using ASP.NET Core and C#. My expertise in full-stack development, including MVC architecture, "
    "RESTful APIs, modern JavaScript frameworks (Angular, React, Vue), and SQL Server with T-SQL, directly aligns with National "
    "General's requirements for developing scalable and maintainable insurance products and services."
)
story.append(Paragraph(ascii_clean(intro), body_text))

# Body - Technical Skills and Experience
body_para1 = CUSTOM_BODY or (
    "In my current role as Technology & Support Services Coordinator at MSU Libraries, I design and build enterprise web "
    "applications using ASP.NET Core, C#, and modern JavaScript frameworks including Angular, React, and Vue. I have solid "
    "experience with MVC architecture, developing and consuming RESTful APIs, and working extensively with SQL Server databases "
    "including writing and optimizing T-SQL queries. My development follows best practices for scalable and maintainable systems, "
    "leveraging test-driven development, version control with Git, and CI/CD pipelines. I am proficient in HTML5, CSS3, SASS, "
    "and responsive design principles, with strong problem-solving and debugging skills across both front-end and back-end environments."
)
story.append(Paragraph(ascii_clean(body_para1), body_text))

# Body - Projects and Problem-Solving
body_para2 = (
    "I thrive in Agile environments, actively contributing to standups, planning, and retrospectives to drive team growth and product quality. "
    "Collaboration is central to my workflow, whether through paired programming or knowledge sharing. My experience building production "
    "analytics dashboards and automation tools demonstrates my ability to deliver scalable solutions while maintaining high code quality and reliability."
)
story.append(Paragraph(ascii_clean(body_para2), body_text))

# Closing
closing_para = CUSTOM_CLOSING or (
    "I am excited about the opportunity to join National General, part of The Allstate Corporation, and contribute to developing "
    "innovative insurance solutions. With my MS in Software Engineering, extensive experience in ASP.NET Core and C# enterprise "
    "application development, proficiency in modern JavaScript frameworks and SQL Server, and commitment to agile best practices, "
    "I am confident I can make immediate contributions to your team. I look forward to the opportunity to challenge the status quo "
    "and help shape the future of protection technology at National General."
)
story.append(Paragraph(ascii_clean(closing_para), body_text))

# ===== Closing =====
story.append(Paragraph("Thank you for your time and consideration.", body_text))
story.append(Paragraph("Sincerely,", closing_style))
story.append(Paragraph("Brandon Temple", signature_style))

# ===== Build PDF =====
if IS_TEMPLATE:
    print("⚠️  WARNING: Using template values!")
    print("   Generic fields are highlighted in yellow.")
    print("   Please update: COMPANY_NAME, HIRING_MANAGER, POSITION_TITLE")
    print()

doc.build(story)

# ===== Verify Single Page =====
from PyPDF2 import PdfReader
reader = PdfReader(filepath)
page_count = len(reader.pages)

if page_count > 1:
    print(f"WARNING: Cover letter is {page_count} pages long! Should be 1 page.")
    print("Consider reducing content or adjusting spacing.")
else:
    print(f"✓ Generated: {filepath} (1 page)")
