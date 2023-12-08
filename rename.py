import os
import openpyxl
from PyPDF2 import PdfFileWriter, PdfFileReader

# 指定存储PDF文件的文件夹路径和Excel文件的路径
pdf_folder = "C:/Users/12944/Desktop/1/pdf"
excel_file = "C:/Users/12944/Desktop/1/姓名学号.xlsx"

workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

pdf_files = os.listdir(pdf_folder)

row_number = 2
for row in sheet.iter_rows(min_row=row_number, values_only=True):
    name, student_id = row
    new_pdf_filename = f"{name}_{student_id}.pdf"

    while pdf_files:
        pdf_file = pdf_files.pop(0) 
        if pdf_file.lower().endswith(".pdf"):
            old_pdf_path = os.path.join(pdf_folder, pdf_file)
            new_pdf_path = os.path.join(pdf_folder, new_pdf_filename)

            # 检查文件是否存在，然后重命名
            if os.path.exists(old_pdf_path):
                os.rename(old_pdf_path, new_pdf_path)
                print(f"已重命名文件: {pdf_file} 为 {new_pdf_filename}")
                break
            else:
                print(f"未找到文件: {pdf_file}")

workbook.close()

