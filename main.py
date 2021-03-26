from io import BytesIO
import base64
import json
import os
import PyPDF2
import typer


app = typer.Typer()


@app.command()
def encode(file_path: str, output_dir: str = './results'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, 'r') as f:
        pdf_result = f.read()

    for i, file_bytes in enumerate(base64.b64decode(pdf_result).split(b'%%EOF')[:-1]):
        pdf_bytes_io = BytesIO(file_bytes + b'%%EOF')
        pdf = PyPDF2.PdfFileReader(pdf_bytes_io)

        with open(f'{output_dir}/file_{i}.pdf', 'wb') as f:
            output = PyPDF2.PdfFileWriter()
            num_of_pages = pdf.getNumPages()
            for page_number in range(0, num_of_pages):
                output.addPage(pdf.getPage(page_number))
            output.write(f)

if __name__ == "__main__":
    app()
