from fpdf import FPDF
import json

from flask import Flask, request
app = Flask(__name__)

@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    form_data = json.loads(request.data)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.text(10, 10, "Name:")
    pdf.cell(40, 10, form_data["name"])
    pdf.text(10, 20, "Email:")
    pdf.cell(40, 20, form_data["email"])
    pdf_content = pdf.output(dest='S').encode('latin1')
    response = make_response(pdf_content)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=form.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)

