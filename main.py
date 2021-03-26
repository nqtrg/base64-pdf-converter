import codecs
import typer


app = typer.Typer()


@app.command()
def decode(file_path: str, output: str = 'results/output.pdf'):
    """
    Convert base64 to PDF file
    """
    with open(file_path, 'rb') as f:
        base64bytes = f.read()

    with open(f'{output}', "wb") as f:
        f.write(codecs.decode(base64bytes, "base64"))


@app.command()
def encode(file_path: str, output: str = 'results/output.txt'):
    """
    Convert PDF file to base64
    """
    with open(file_path, 'rb') as f:
        base64bytes = f.read()

    with open(f'{output}', "wb") as f:
        f.write(codecs.encode(base64bytes, "base64"))


if __name__ == "__main__":
    app()
