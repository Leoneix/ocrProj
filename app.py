from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfMerger

app = Flask(__name__)
app.secret_key = "secretkey"  # Needed for flash messages
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Paths to Poppler and Tesseract (adjust for your system)
POPLER_PATH = r"C:\poppler-25.07.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def make_pdf_searchable(input_pdf, output_pdf):
    images = convert_from_path(input_pdf, poppler_path=POPLER_PATH)
    temp_files = []
    for i, img in enumerate(images):
        page_pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang='eng')
        temp_file = os.path.join(UPLOAD_FOLDER, f"temp_page_{i+1}.pdf")
        with open(temp_file, "wb") as f:
            f.write(page_pdf)
        temp_files.append(temp_file)

    merger = PdfMerger()
    for temp in temp_files:
        merger.append(temp)
    merger.write(output_pdf)
    merger.close()

    # cleanup
    for temp in temp_files:
        os.remove(temp)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["pdf"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(input_path)

        output_name = "searchable_" + filename
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_name)

        try:
            make_pdf_searchable(input_path, output_path)
            flash("Processing complete!")
            return redirect(url_for("download_file", filename=output_name))
        except Exception as e:
            flash(f"Error: {e}")
            return redirect(request.url)

    return render_template("index.html")


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
