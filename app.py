from flask import Flask, request
import json
import PyPDF2

app = Flask(__name__)

@app.route("/get_pdf", methods=['POST'])
def get_read_pdf():
    return "success"

@app.route("/get_cred_score", methods=['POST'])
def generate_credit_score():
    if request.method == 'POST':
        try:
            pdf_file = request.files['pdf_file']


            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages

            extracted_data = []

            for page_number in range(num_pages):
                page = pdf_reader.getPage(page_number)
                text = page.extractText()

                extracted_data.append(text)

            #storing the object data into the "body_data" and implemeting the manipulation and slicing
            body_data = request.get_json()
            print(body_data)

            response = {
                "success": True,
                "score": "812"
            }
        except Exception as e:
            response = {
                "success": False,
                "message": str(e)
            }
    
    return response

if __name__ == '__main__': 
    app.run()