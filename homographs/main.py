import typer

def fn():
    print(f'Specify the first filename:')
    fname = input()
    print(f'Specify the second filename:')
    fname2 = input()

    if fname == fname2:
        print(f'The paths are homographs')
    else:
        print(f'The paths are not homographs')

def main():
    typer.run(fn)
