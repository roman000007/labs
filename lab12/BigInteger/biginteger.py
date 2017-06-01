class BigInteger:

    def __init__(self, initValue="0"):
        self.change_value(initValue)

    def fill_zeroes(self, count):
        for i in range(count):
            self.add_digit("0")

    def change_value(self, initValue="0"):
        self._head = None
        self._tail = None
        self._length = 0
        initValue = str(initValue)
        self.is_negative = False
        if initValue == "":
            initValue = "0"
        for i in range(len(initValue)):
            if initValue[i] == "-" and i == 0:
                self.is_negative = True
                continue
            self.add_digit(initValue[i])
        self.remove_zeroes()

    def add_digit(self, d="0"):
        d = _Digit(d)
        if self._head is None:
            self._head = d
        else:
            d.prev = self._tail
            self._tail.next = d
        self._length += 1
        self._tail = d

    def add_digit_reverse(self, d="0"):
        d = _Digit(d)
        if self._tail is None:
            self._tail = d
        else:
            d.next = self._head
            self._head.prev = d
        self._length += 1
        self._head = d

    def remove_zeroes(self):
        curr = self._head
        while curr is not None:
            if curr.digit == 0 and len(self) > 1:
                curr.next.prev = None
                curr = curr.next
                self._length -= 1
            else:
                self._head = curr
                return

    def __len__(self):
        return self._length

    def __str__(self):
        curr = self._head
        res = ""
        while curr is not None:
            res += str(curr.digit)
            curr = curr.next
        return "-" + res if self.is_negative else res

    # < - override
    def __lt__(self, other):
        if len(self) < len(other):
            return True
        elif len(self) > len(other):
            return False
        else:
            currA = self._head
            currB = other._head
            while currA is not None:
                if currA.digit < currB.digit:
                    return True
                elif currA.digit > currB.digit:
                    return False
                else:
                    currA = currA.next
                    currB = currB.next

    # > - override
    def __gt__(self, other):
        if len(self) > len(other):
            return True
        elif len(self) < len(other):
            return False
        else:
            currA = self._head
            currB = other._head
            while currA is not None:
                if currA.digit > currB.digit:
                    return True
                elif currA.digit < currB.digit:
                    return False
                else:
                    currA = currA.next
                    currB = currB.next
        return False

    # <= - override
    def __le__(self, other):
        return not self > other

    # >= - override
    def __ge__(self, other):
        return not self < other

    # == - override
    def __eq__(self, other):
        if len(self) > len(other) or len(self) < len(other):
            return False
        else:
            currA = self._head
            currB = other._head
            while currA is not None:
                if currA.digit > currB.digit or currA.digit < currB.digit:
                    return False
                else:
                    currA = currA.next
                    currB = currB.next
        return True

    # != override
    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        minus = False
        if self.is_negative and other.is_negative:
            minus = True
        if self.is_negative and not other.is_negative:
            return BigInteger(str(other)) - BigInteger(str(self)[1:])
        if not self.is_negative and other.is_negative:
            return BigInteger(str(self)) - BigInteger(str(other)[1:])
        currA = self._tail
        currB = other._tail
        rest = 0
        tmp = BigInteger()
        tmp.is_negative = minus
        tmp.fill_zeroes((max(len(self), len(other))+ 1))
        res = tmp._tail
        while currA is not None and currB is not None:
            res.digit = (currA.digit + currB.digit + rest) % 10
            rest = (currA.digit + currB.digit + rest) // 10
            currA = currA.prev
            currB = currB.prev
            res = res.prev
        while currA is not None:
            res.digit = (currA.digit + rest) % 10
            rest = (currA.digit + rest) // 10
            currA = currA.prev
            res = res.prev
        while currB is not None:
            res.digit = (currB.digit + rest) % 10
            rest = (currB.digit + rest) // 10
            currB = currB.prev
            res = res.prev
        if rest != 0:
            res.digit = rest
        tmp.remove_zeroes()
        return tmp


    def __sub__(self, other):
        minus = False
        if self.is_negative and other.is_negative:
            return BigInteger(str(other)[1:]) - BigInteger(str(self)[1:])
        if self.is_negative and not other.is_negative:
            return BigInteger(str(self)) + BigInteger("-" + str(other))
        if not self.is_negative and other.is_negative:
            return BigInteger(str(self)) + BigInteger(str(other)[1:])
        if self >= other:
            currA = self._tail
            currB = other._tail
        else:
            currA = other._tail
            currB = self._tail
            minus = not minus
        rest = 0
        tmp = BigInteger()
        tmp.is_negative = minus
        tmp.fill_zeroes((max(len(self), len(other))))
        res = tmp._tail
        while currA is not None and currB is not None:
            res.digit = (currA.digit - currB.digit - rest + 10) % 10
            rest = 0 if currA.digit - currB.digit - rest >= 0 else 1
            currA = currA.prev
            currB = currB.prev
            res = res.prev
        while currA is not None:
            res.digit = (currA.digit - rest + 10) % 10
            rest = 0 if currA.digit - rest >= 0 else 1
            currA = currA.prev
            res = res.prev

        tmp.remove_zeroes()
        return tmp

    def link(self):
        curr = self._head
        while curr is not None:
            print(curr.digit,end="->")
            curr = curr.next

    def link_reverse(self):
        curr = self._tail
        while curr is not None:
            print(curr.digit,end="<-")
            curr = curr.prev

    def __mul__(self, other):
        currA = self._tail
        currB = other._tail
        rest = 0
        tmp = BigInteger()
        tmp.is_negative = bool((self.is_negative + other.is_negative) % 2)
        tmp.fill_zeroes(len(self) * len(other) + 1)
        curr_res = tmp._tail
        while currB is not None:
            res = curr_res
            while currA is not None:
                res.digit += (currA.digit * currB.digit + rest) % 10
                rest = (currA.digit * currB.digit + rest) // 10
                currA = currA.prev
                res = res.prev
                if rest != 0:
                    res.digit += rest
                    rest = 0
            currB = currB.prev
            currA = self._tail
            curr_res = curr_res.prev
        if rest != 0:
            curr_res.digit += rest
        tmp.remove_zeroes()
        return tmp

    def __floordiv__(self, other):
        res = 0
        if self.is_negative:
            currA = BigInteger(str(self)[1:])
        else:
            currA = BigInteger(str(self))

        if other.is_negative:
            currB = BigInteger(str(other)[1:])
        else:
            currB = BigInteger(str(other))
        modulo = bool((self.is_negative + other.is_negative) % 2)
        while True:
            if currA < currB:
                r = BigInteger(str(res))
                r.is_negative = modulo
                return r
            elif len(currA) == len(currB):
                currA -= currB
                res += 1
            else:
                res += 10 ** (len(currA) - len(currB) - 1)
                currA -= BigInteger(str(currB) + "0" * (len(currA) - len(currB) - 1))

    def __pow__(self, power, modulo=None):
        b = BigInteger(str(self))
        w = BigInteger(str(self))
        p = BigInteger(str(power))
        while int(p) != 1:
            p -= BigInteger(1)
            w *= b
        return w

    def __int__(self):
        return int(str(self))


    def __and__(self, other):
        return int(self) & int(other)

    def __or__(self, other):
        return int(self) | int(other)

    def __xor__(self, other):
        return int(self) ^ int(other)

    def __lshift__(self, other):
        return self * (BigInteger(2) ** other)

    def __rshift__(self, other):
        return self // (BigInteger(2) ** other)






class _Digit:
    def __init__(self, s):
        self.next = None
        self.prev = None
        self.digit = int(s)

    @staticmethod
    def links_from_reverse(f):
        curr = f
        while curr is not None:
            print(curr.digit, end="<-")
            curr = curr.prev
        print()