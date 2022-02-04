import click



@click.command()
@click.option("--parent", help="parent file")
@click.option("--target", help="file to insert contents")
def main(parent, target):
    """Append a file contents with a from file"""
    with open(target, 'r') as fh:
        data = fh.read()
    with open(parent, 'a') as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
