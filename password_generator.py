import argparse
import secrets
import string

def override_args(func):
    """ Stops parsing args and calls a function. """

    class OverrideAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            func()
            parser.exit()
    return OverrideAction

def get_args():
    """ Program arguments. """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                    epilog='''Example:\n\npassword_generator.py -a -u -s -l 10\nRoT^"nRD.J''')

    parser.add_argument('--alpha', '-a', action='store_true', help='Include lowercase alpha characters')
    parser.add_argument('--upper', '-u', action='store_true', help='Enable capitalization')
    parser.add_argument('--symbol', '-s', action='store_true', help='Include symbols')
    parser.add_argument('--number', '-n', action='store_true', help='Include numbers')
    parser.add_argument('--length', '-l', type=int, default=15, help='Length of password to generate [Default=15]')
    parser.add_argument('--count', '-c', type=int, default=1, help='Number of passwords to generate [Default=1]')
    parser.add_argument('--grid', '-g', nargs=0, action=override_args(generate_password_grid), help='Generate password grid')

    return parser.parse_args()

def generate_password_grid():
    """ Generates a password grid. """

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Print top row of grid
    print('$ ', end='')
    print(' '.join(string.ascii_uppercase))

    # Print grid rows
    for letter in string.ascii_uppercase:
        # Print alphabet on left side of grid
        print(letter, end=' ')

        # Fill rows with random characters
        for _ in range(len(string.ascii_uppercase)):
            print(''.join(secrets.choice(characters)), end=' ')
        print()

def generate_password(characters: str, length: int) -> str:
    """ Generates random, cryptographically strong password. """

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))

        # Ensure there's at least one lowercase and one digit
        if string.ascii_lowercase in characters and string.digits in characters:
            if (any(c.islower() for c in password)
                and any(c.isdigit() for c in password)):
                break
        # Ensure there's at least one lowercase and one symbol
        elif string.ascii_lowercase in characters and string.punctuation in characters:
            if (any(c.islower() for c in password)
                and any(string.punctuation for c in password)):
                break
        # Ensure there's at least one uppercase and one symbol
        elif string.ascii_uppercase in characters and string.punctuation in characters:
            if (any(c.isupper() for c in password)
                and any(string.punctuation for c in password)):
                break
        # Ensure there's at least one uppercase and one digit
        elif string.ascii_uppercase in characters and string.digits in characters:
            if (any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
                break
        # Ensure there's at least one digit and one symbol
        elif string.digits in characters and string.punctuation in characters:
            if (any(c.isdigit() for c in password)
                and any(string.punctuation for c in password)):
                break
        # Ensure there's at least one lowercase and one uppercase
        elif string.ascii_letters in characters:
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)):
                break
        # Ensure there's at least one lowercase, one uppercase, and one digit
        elif string.ascii_letters in characters and string.digits in characters:
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
                break
        # Ensure there's at least one lowercase, one uppercase, and one symbol
        elif string.ascii_letters in characters and string.punctuation in characters:
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(string.punctuation for c in password)):
                break
        # Ensure there's at least one lowercase, one uppercase, one symbol, and one digit
        elif string.ascii_letters in characters and string.punctuation in characters and string.digits in characters:
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(string.punctuation for c in password)):
                break
        else:
            break

    return password

if __name__ == '__main__':
    args = get_args()

    characters = ''

    if args.length <= 3:
        raise ValueError('Length Error: Length must be greater than 3.')
    if args.count < 0:
        raise argparse.ArgumentTypeError('Type Error: Must be a positive number.')
    if args.alpha:
        characters += string.ascii_lowercase
    if args.upper:
        characters += string.ascii_uppercase
    if args.symbol:
        characters += string.punctuation
    if args.number:
        characters += string.digits

    for _ in range(args.count):
        print(generate_password(characters, args.length))