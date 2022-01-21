pr_key,pu_key=generate_rsa_key(1e3,1e5)
print(pr_key)
print(pu_key)
message="hello"
cipher_text=encrypt(pu_key,message)
print(cipher_text)
plain_text=decrypt(pr_key,cipher_text)
print(plain_text)
#and gcd of 0 and value is the value we will use this in our recurssion base case
