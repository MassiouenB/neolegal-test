from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from typing import List

PDF_PATH = 'public/media/pdf'
def generate_pdf(users: List[list]) -> str:
    pdf_name = PDF_PATH+"/users_table.pdf"
    # Define the table headers
    headers = ["Nom d'utilisateur", "Nom", "Prénom"]

    # Create a new PDF file and write the table
    doc = SimpleDocTemplate(pdf_name, pagesize=letter)
    elements = []
    # Add a title to the document
    styles = getSampleStyleSheet()
    title_style = styles["Title"]

    if (users):
        title = Paragraph("Liste des utilisateurs", title_style)
        elements.append(title)
        elements.append(Paragraph(" ", styles["Normal"]))

        # Add the table to the document
        table = Table([headers] + users)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        elements.append(table)
    else:
        empty_table = Paragraph("Liste des utilisateurs est vide", title_style)
        elements.append(empty_table)

    doc.build(elements)
    return pdf_name
    