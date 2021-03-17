
value: str = input( 'Tell me your number phone: ')
role: str = input ('Tell me your role: ')

if all([value.isdigit(), int(value) < +380669323083, role != 'admin']):
    print(f'Not allowed!!!!! Your phone number must start with +38 {value}')
    sys.exit(0)
    print('You are welcome!!!')