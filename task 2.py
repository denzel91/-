email: str = input('Input email')

if '@' not in email:
    print('Invalid')
    sys.exit(0)
if '.' not in email:
    print('Invalid')
    sys.exit(0)
    at_sign_index = email.index('@')
    for sign in {'.', '@'}:
        if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
            print('Invalid')
            sys.exit(0)
        elif email[-1] == sign or email[0] ==sign:
            print('Invalid')
            sys.exit(0)ion}')

