def decrypt(key, cyphertext):
    plaintext = ''
    key = key.encode('utf-8')
    kidx = 0
    for i in range(0, len(cyphertext), 2):
        byte = int(cyphertext[i:i+2], 16)
        k = key[kidx]
        kidx += 1
        kidx = kidx % len(key)
        c = chr(byte ^ k)
        plaintext += c
    return plaintext


def encrypt(key, plaintext):
    plaintext = plaintext.encode('utf8')
    cyphertext = ''
    key = key.encode('utf8')
    kidx = 0
    for plainbyte in plaintext:
        k = key[kidx]
        kidx += 1
        kidx = kidx % len(key)
        byte = plainbyte ^ k
        cyphertext += str.format('{:02X}', byte)
    return cyphertext


def main():
    # password from default.xml in razor dir
    # omit the 1+
    # the actual problem was not the code, but finding this algorithm
    cyphertext = '0500000E0E4D3223302D29'
    key = 'melba'  # windows username

    print(decrypt(key, cyphertext))
    print(encrypt(key, 'hello WORLD'))

    # random test
    plaintext = 'hello world'
    assert plaintext == decrypt(key, encrypt(key, plaintext))

if __name__ == '__main__':
    main()
