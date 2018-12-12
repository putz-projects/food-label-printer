from users import set_kerb

if __name__ == "__main__":
    print('Enter LOLcode:')
    lolcode = input()
    print('Enter kerberos:')
    kerb = input()

    set_kerb(lolcode, kerb)

    print('All done!')
