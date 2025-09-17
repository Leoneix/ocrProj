import pytesseract
from pdf2image import convert_from_path
import os
from PyPDF2 import PdfMerger

# file paths
input_pdf_filename = 'Input-file.pdf'
output_pdf_filename = 'Output-file.pdf'

# paths to Poppler and Tesseract
poppler = r"C:\poppler-25.07.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def make_pdf_searchable(input_pdf, output_pdf):
    print(f"OCR starting: {input_pdf}")

    if not os.path.exists(input_pdf):
        print(f"File not found: {input_pdf}")
        return

    try:
        print("Converting PDF to images...")
        images = convert_from_path(input_pdf, poppler_path=poppler)
        print(f"Pages found: {len(images)}")

        print("Running OCR...")
        temp_files = []
        for i, img in enumerate(images):
            print(f"Processing page {i+1}")
            page_pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang='eng')
            temp_file = f"temp_page_{i+1}.pdf"
            with open(temp_file, "wb") as f:
                f.write(page_pdf)
            temp_files.append(temp_file)

        print("Merging pages...")
        merger = PdfMerger()
        for temp in temp_files:
            merger.append(temp)
        merger.write(output_pdf)
        merger.close()

        # cleanup
        for temp in temp_files:
            os.remove(temp)

        print(f"Done! Created: {output_pdf}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    make_pdf_searchable(input_pdf_filename, output_pdf_filename)

if __name__ == "__main__":
    main()
