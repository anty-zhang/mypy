# -*- coding: utf-8 -*-

from pprp.crypto_2 import rijndael
import base64
import urllib

KEY_SIZE = 16
BLOCK_SIZE = 32

AES_KEY = 'TopSecretKey'


def encrypt(key, plaintext):
    padded_key = key.ljust(KEY_SIZE, '\0')
    padded_text = plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * '\0'

    # could also be one of
    # if len(plaintext) % BLOCK_SIZE != 0:
    #    padded_text = plaintext.ljust((len(plaintext) / BLOCK_SIZE) + 1 * BLOCKSIZE), '\0')
    # -OR-
    # padded_text = plaintext.ljust((len(plaintext) + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE)), '\0')

    r = rijndael(padded_key, BLOCK_SIZE)

    ciphertext = ''
    for start in range(0, len(padded_text), BLOCK_SIZE):
        ciphertext += r.encrypt(padded_text[start:start + BLOCK_SIZE])

    encoded = base64.b64encode(ciphertext)

    return encoded


def decrypt(key, encoded):
    padded_key = key.ljust(KEY_SIZE, '\0')

    ciphertext = base64.b64decode(encoded)

    r = rijndael(padded_key, BLOCK_SIZE)

    padded_text = ''
    for start in range(0, len(ciphertext), BLOCK_SIZE):
        padded_text += r.decrypt(ciphertext[start:start + BLOCK_SIZE])

    plaintext = padded_text.split('\x00', 1)[0]

    return plaintext


if __name__ == '__main__':
#     key = 'TopSecretKey'
#     token = 'f6GfKc9NJ6QvRFBOzB1T+U1IJgiBZzI753vvMxj/CSE='
#     token = 'I0qRoKENUQuEHvGTq6hBzAhhc/7yr6olFFACP7QezIo='
#     token = urllib.unquote('knPbsNJtgwdZvhM5bPrj3P%2FVNpWgMYOlNJoIx5TaHQw%3D')
#     print token
#     token = 'Ca64U%2Fq2r%2F%2B3%2Fn3jJ8ULmObLAtHdzXvwgFdj58gNlkw%3D'
#     # token = 'knPbsNJtgwdZvhM5bPrj3P%2FVNpWgMYOlNJoIx5TaHQw%3D'
#     token = urllib.unquote(token)
#
# #     key = 'a6841c04403200a2c1f34d4994cb885f'
# #     token = '678910111211678910111211'
# #     print encrypt(key, '1234xxxxxxxxxxxxxxxxxxx')
# #     print decrypt(key, token)

    # uid = '13994595'
    # import json
    # plaintext = encrypt(AES_KEY, json.dumps({'uid': u'13994595'}))
    # print urllib.quote(plaintext)

    token = 'WujrlLPHA0xk39fD90eRLclOSjaXzBK%2F%2FhDGektvFbw%3D'
    # token = '7WnicXEucSwiIuoXlkXyLvg0O6DRL9%2BjaUtKZwRR0qU%3D'
    uid = decrypt(AES_KEY, urllib.unquote(token))
    import json
    data = json.loads(uid)
    print data
