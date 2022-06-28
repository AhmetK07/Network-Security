import random

# This functions is for our random prime  number generation.
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)

    return prime_list

# Here we print prime number between 17 and 98 and list them.

print(primesInRange(17, 98))

# We define a prime list that is in range for 17, 98.
prime_list = primesInRange(17, 98)
randomPrime = random.choice(prime_list)

# After that we get a random prime number from the list we have created.

print('Our prime number: ', randomPrime)

# Our integer value and  private key will be in the range of 1 to our prime number.

IntegerVal = random.randint(1, randomPrime)

PrivateKey = random.randint(1, randomPrime)

print("Our Integer number:", IntegerVal)

print("#################################")

print("Our private number:", PrivateKey)

# Our public key will be calculated  integer over private key modulo prime.

OurPublicKey = IntegerVal ** PrivateKey % randomPrime

print("Our public Key", OurPublicKey)

print("#################################")

# Time for Alice's private key.

PrivateKeyAlice = random.randint(1, randomPrime)

print("Alice's private number: ", PrivateKeyAlice)

# Same operation for Alice's public key integer over private key modulo prime number.

AlicePublicKey = IntegerVal ** PrivateKeyAlice % randomPrime

print("Alice's public key:", AlicePublicKey)

print("#################################")

# Now for our secret key Alice's public key over our private key modulo prime number.

OurSecretKey = AlicePublicKey ** PrivateKey % randomPrime

print("Our Secret key: ", OurSecretKey)

print("#################################")

# And Alice's secret key is found exactly the same way except it's our public key over Alice's private key modulo prime.

AliceSecretKey = OurPublicKey ** PrivateKeyAlice % randomPrime

print("Alice's secret key:", AliceSecretKey)

print("#################################")


# Here is a function for caesar shifting.

def ascii_caesar_shift(message, distance):
    encrypted = ""
    for char in message:
        value = ord(char) + distance
        encrypted += chr(value % 128)  # 128 for ASCII
    return encrypted


selam = ascii_caesar_shift("1234", 5)

selam2 = ascii_caesar_shift("6789", -5)

# We shift a message by the amount of the secret keys so in the output we can discover they are identical.

PrivateKeyCp = ascii_caesar_shift("Your secret key is 1", AliceSecretKey)

PrivateKeyCp2 = ascii_caesar_shift("Your secret key is 1", OurSecretKey)


print(selam)

print(selam2)

print(PrivateKeyCp)

print(PrivateKeyCp2)