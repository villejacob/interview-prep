'''
Two massive numbers, in the millions, or billions, arbitrarily large.

1. Write a method to add the two numbers
    - figure out how to represent the numbers
2. Write a method to multiply the two numbers
    - must use the addition method from 1.
3. Modify the multiplication method to complete in linear time
'''

def addTwoNumbers(n, m):
    if not n or not m:
        return n or m
    nlen = len(n)
    mlen = len(m)
    longest = max(n, m, key=len)
    carry = index = 0
    sum = []
    for i in xrange(min(nlen, mlen)):
        current = int(n[nlen-i-1]) + int(m[mlen-i-1]) + carry
        carry, current = divmod(current, 10)
        sum.append(`current`)
        index = i
    for i in reversed(xrange(len(longest)-index-1)):
        if carry > 0:
            current = int(longest[i]) + carry
            carry, current = divmod(current, 10)
            sum.append(`current`)
        else:
            sum.append(longest[i])
    if carry > 0:
        sum.append(`carry`)
    return ''.join(reversed(sum))

def multiplyTwoNumbers(n, m):
    nlen = len(n)
    mlen = len(m)
    sums, current, zeroes = [], [], []
    carry = 0
    for i in xrange(nlen):
        current = zeroes[:]
        for j in xrange(mlen):
            product = int(n[nlen-i-1]) * int(m[mlen-j-1]) + carry
            carry, product = divmod(product, 10)
            current.append(product)
        if carry > 0:
            current.append(carry)
        sums.append(''.join(reversed(map(str, current))))
        zeroes.append(0)
    product = ""
    for sum in sums:
        product = addTwoNumbers(product, sum)
    return product

def multiplyLinearTime(n, m):
    nlen = len(n)
    mlen = len(m)
#    if mlen < nlen:
#        n, m = m, n
    sums, zeroes = [], []
    carry = 0
    multiples = {}
    for i in xrange(nlen):
        current = zeroes[:]
        if n[nlen-i-1] not in multiples:
            for j in xrange(mlen):
                product = int(n[nlen-i-1]) * int(m[mlen-j-1]) + carry
                carry, product = divmod(product, 10)
                current.append(product)
            if carry > 0:
                current.append(carry)
            multiples[n[nlen-i-1]] = ''.join(reversed(map(str, current)))
        sums.append(multiples[n[nlen-i-1]])
        zeroes.append(0)
    product = ""
    for sum in sums:
        product = addTwoNumbers(product, sum)
    return product


        



print multiplyLinearTime("122", "10")
