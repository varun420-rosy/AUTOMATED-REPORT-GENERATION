#COD TECH IT SOLUTIONS.
#TASK-2 AUTOMATED REPORT GENERATION
#PROGRAM TO GENERATE A REPORT IN PDF FILE FROM A EXCEL FILE

import pandas as pd
from fpdf import FPDF
def generate_report(data):
    pdf = FPDF(unit="pt", format="A3")
    pdf.add_page()
    pdf.set_font("Arial", size=7)   
    column_widths = [60] * len(data.columns)   
    for i, col in enumerate(data.columns):
        pdf.cell(column_widths[i], 15, txt=str(col), border=1, align='C')
    pdf.ln(15)
    for index, row in data.iterrows():
        for i, value in enumerate(row.values):
            pdf.cell(column_widths[i], 15, txt=str(value), border=1, align='C')
        pdf.ln(15)
    pdf.output("report.pdf")
def main():
    file_name = r"C:\Users\AVITA\Desktop\CODE TECH\TASK2.CSV.xlsx"
    data = pd.read_excel(file_name)
    print(data.to_string())
    generate_report(data)
if __name__ == "__main__":
    main()
