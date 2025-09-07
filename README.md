
# ocrProj
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This project converts scanned PDFs into **searchable PDFs** using **Tesseract OCR** and **Poppler**.  

Features : 
* Converting scanned PDFs or images into editable text using OCR (Optical Character Recognition).

### Future Updates
* Automatically transfer extracted text into a new, editable file for easier usage and sharing.
* For questions, categorizing by topic using keywords or NLP embeddings.
* Export selected sub-parts as PDF.
* Search and filter questions by keywords or topic.

## Installation
* Download Poppler - https://github.com/oschwartz10612/poppler-windows

* Download Tessaract - https://github.com/UB-Mannheim/tesseract/wiki

* Add your Poppler bin path to PATH

* Open the app.ipynb file in your IDE
```bash
  input_pdf_filename = 'q1.pdf' --> your preferred pdf file path
```
```bash
  poppler = r"C:\poppler-25.07.0\Library\bin" --> Your Poppler path
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" --> Your Tesseract.exe path
```
* Run and get Machine-readable text
## Acknowledgements

 - [Universitätsbibliothek Mannheim](https://github.com/UB-Mannheim)
 - [oschwartz10612](https://github.com/oschwartz10612)



## License

[MIT](https://choosealicense.com/licenses/mit/)




