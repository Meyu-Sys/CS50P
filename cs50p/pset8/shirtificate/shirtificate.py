from fpdf import FPDF

name = input("Name: ")
shirt = FPDF(orientation='P', format='A4')
shirt.add_page()
shirt.set_font("Helvetica", size=50)
shirt.set_text_color(14, 14, 14)
shirt.cell(0, 50, text="CS50 Shirtificate",  align="C")
shirt.image("shirtificate.png", keep_aspect_ratio=True, x=5, y=80, w=200)
shirt.set_font("Helvetica", size=30)
shirt.set_text_color(227, 236, 236)
shirt.cell(-200,250, text=f"{name} took CS50", align="C")
shirt.output("shirtificate.pdf")
