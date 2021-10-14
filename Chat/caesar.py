# Set the first allowable character
start = ord(' ')
# Set the last allowable character
end = ord('~')
# Get the count of allowable characters
count = end - start + 1

key = 1

def setKey(k):
    global key
    key = k % count

def encrypt(msg):
    encryptedMsg = ''

    # TODO: Encrypt the msg
    return encryptedMsg

def decrypt(msg):
    decryptedMsg = ''

    for char in msg:
        number = ord(char) - start
        number = number - key
        if number < 0:
            number = number + count
        number = number + start
        decryptedMsg = decryptedMsg + chr(number)
    return decryptedMsg

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

    setKey(3)

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
