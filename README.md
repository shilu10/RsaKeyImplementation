# RsaKeyImplementation


# euler's phi theorem->> a ** phi(n) mod p=1 it is the generalization for the fermat little theorem
#where phi(n) it will count all the postive natural number upto n all should be relative prime or co prime of n
#relative prime or co-prime is a set of number whose gcd (greatest common divisor) is equal to "1"
#for prime numbers we can easily find the relative prime --////  phi(prime)=prime-1  ///---


#Rsa alogrithm (public key-e) and (private key-d)
#1. Generate a large prime(p and q) WE will use fermat theorem for generating the prime ,we can also use the rabin miller theorem also
#2. Calculate n=p*q for the euler's theorem phi(n)=(p-1) (q-1)
#3. Calculate public key (e)  formula-->> gcd (e,phi(n))=1 ,so e and phi(n) are relative prime we will use eucliader theorem
#4. Calculate private key(d) formula -->>  d*e mod phi(n)=1 where d is the inverse of e so we can find the inverse easily using euclidear theorem
#5.  we will use euclidean extended theorem for finding both inverse of prime and the gcd

# in algebra inverse of a =a%apow -1 =1
#in modular Arthimetic inverse is a*apow-1 congruence of 1 mod m
#we need the inverse for the d ->private key
#for the modular inverse ,we will use extended euclidean algorithm

#formula for E.E.A--->> ax=by=gcd(a,b)
#we can solve this by first we need to implement it in the standard euclidean algorithm way
#and need to rearrange the equations and we need to substitute the values in the equation
#we will do the substitution # euler's phi theorem->> a ** phi(n) mod p=1 it is the generalization for the fermat little theorem
#where phi(n) it will count all the postive natural number upto n all should be relative prime or co prime of n
#relative prime or co-prime is a set of number whose gcd (greatest common divisor) is equal to "1"
#for prime numbers we can easily find the relative prime --////  phi(prime)=prime-1  ///---


#Rsa alogrithm (public key-e) and (private key-d)
#1. Generate a large prime(p and q) WE will use fermat theorem for generating the prime ,we can also use the rabin miller theorem also
#2. Calculate n=p*q for the euler's theorem phi(n)=(p-1) (q-1)
#3. Calculate public key (e)  formula-->> gcd (e,phi(n))=1 ,so e and phi(n) are relative prime we will use eucliader theorem
#4. Calculate private key(d) formula -->>  d*e mod phi(n)=1 where d is the inverse of e so we can find the inverse easily using euclidear theorem
#5.  we will use euclidean extended theorem for finding both inverse of prime and the gcd

# in algebra inverse of a =a%apow -1 =1
#in modular Arthimetic inverse is a*apow-1 congruence of 1 mod m
#we need the inverse for the d ->private key
#for the modular inverse ,we will use extended euclidean algorithm

#formula for E.E.A--->> ax=by=gcd(a,b)
#we can solve this by first we need to implement it in the standard euclidean algorithm way
#and need to rearrange the equations and we need to substitute the values in the equation
#we will do the substitution 
#and gcd of 0 and value is the value we will use this in our recurssion base case

