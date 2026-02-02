
if t < -20:
    print('Stay at home')
elif t < 0:
    print('It is cold')
else:
    shopping = input('Maybe shopping?').lower().strip()
    if shopping == 'yes': # YES, Yes,   yes
        print('You need $')
    else:
        print('Ok!')
    print('It is normal')

print('Have a nice day!')