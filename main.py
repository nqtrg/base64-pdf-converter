import codecs
import typer


app = typer.Typer()


@app.command()
def decode(
    input: typer.FileBinaryRead = typer.Argument(..., help='Specify an input file path'),
    output: typer.FileBinaryWrite = typer.Option(None, help='Specify an output file path. Default, write to STDOUT'),
):
    '''
    Convert base64 to PDF file
    '''

    base64bytes = input.read()

    if output:
        output.write(codecs.decode(base64bytes, 'base64'))
    else:
        typer.echo(codecs.decode(base64bytes, 'base64'))


@app.command()
def encode(
    input: typer.FileBinaryRead = typer.Argument(..., help='Specify an input file path'),
    output: str = typer.Option('', help='Specify an output file path. Default, write to STDOUT'),
):
    '''
    Convert PDF file to base64
    '''

    base64bytes = input.read()

    if output:
        with open(f'{output}', 'wb') as f:
            f.write(codecs.encode(base64bytes, 'base64'))
    else:
        typer.echo(
            codecs.encode(
                base64bytes,
                'base64',
            ).decode(
                'utf-8'
            )
        )

if __name__ == '__main__':
    app()
