from BigInteger.biginteger import BigInteger
test_ints = True
test_links = True
test_compare = True
test_arithmetic = True
test_positive = True
test_bytes = True
while True:
    i1 = input()
    i2 = input()
    b1 = BigInteger(i1)
    b2 = BigInteger(i2)
    if test_ints:
        print(b1)
        print(b2)
    if test_links:
        print(b1.link())
        print(b1.link_reverse())
        print(b2.link())
        print(b2.link_reverse())
    if test_compare:
        print("<:", b1 < b2)
        print(">:", b1 > b2)
        print("<=:", b1 <= b2)
        print(">=:", b1 >= b2)
        print("==:", b1 == b2)
        print("!=:", b1 != b2)
    if test_arithmetic:
        print("+:", b1 + b2)
        print("-:", b1 - b2)
        print("*:", b1 * b2)
        print("//:", b1 // b2)
        print("**:", b1 ** b2)
    if test_positive:
        print("Negative:", b1.is_negative)
        print("Negative:", b2.is_negative)
    if test_bytes:
        print("6 & 5 =", 6 & 5)
        print("&:", b1 & b2)
        print("6 | 5 =", 6 | 5)
        print("|:", b1 | b2)
        print("6 ^ 5 =", 6 ^ 5)
        print("^:", b1 ^ b2)
        print("6 >> 5 =", 6 >> 5)
        print(">>:", b1 >> b2)
        print("6 << 5 =", 6 << 5)
        print("<<:", b1 << b2)