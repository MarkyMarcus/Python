def setKey(key):
    pass

def encrypt(msg):
    return msg

def decrypt(msg):
    return msg

if __name__ == '__main__':
    import string

    test_cases = [
        'HELLO',
        'test',
        '1234',
        ' !#"',
        'The quick brown fox jumps over the lazy dog',
        string.ascii_letters,
        string.digits,
        string.punctuation
    ]

    for t in test_cases:
        en = encrypt(t)
        de = decrypt(en)
        print '''
           Text:      %s
           Encrypted: %s
           Decrypted: %s
        ''' % (t, en, de)
        assert(de == t)

    print 'All tests passed'
