from RSA import decrypt
import random

class Rsa :
    def is_prime(number) :
        if number < 2 :
            return False
        for _ in range(10) :
            a = random.randint(2,number) - 1
            if pow(a,number-1,number) != 1 :
                return False
        return True

    def generating_prime(start, end) :
        number = random.randint(start, end)

    for c in plaintext:
        a=ord(c)
        cipher_text.append(pow(a,e,n))
        while not is_prime(number) :
            number = random.randint(start, end)
        return number

    def gcd(a, b) :
        while b != 0:
            a, b = b, a % b
        return a

    def modular_inverse(a, b) :
        if a == 0:
            return b, 0, 1
        div, x1, y1 = modular_inverse(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return div, x, y

    def generate_rsa_key(start, end) :
        p = generating_prime(start,end)
        q = generating_prime(start,end)
        n = p * q
        phi = (p-1) * (q-1)
        e = random.randint(1, phi)
        while gcd(e, phi) !=1:
            e = random.randint(1, phi)
        d = modular_inverse(e,phi)[1]
        return (d, n), (e, n)

    def encrypt(public_key, plaintext) :
        e, n = public_key
        cipher_text = [ ]
        for c in plaintext:
            a = ord(c)
            cipher_text.append(pow(a, e, n))
        return cipher_text

    def decryption(cipher_text,private_key) :
        d, n = private_key
        plaintext = " "
        for num in cipher_text :
            a = pow(num, d, n)
            plaintext += str(chr(a))
        return plaintext

    

