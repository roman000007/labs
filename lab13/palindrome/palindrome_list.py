from arraystack import ArrayStack

def check_brackets(s):
    stack = ArrayStack()
    for i in s:
        if i == "(":
            stack.push("(")
        if i == ")":
            if stack.isEmpty():
                return False
            stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False


class Palindrome:
    def __init__(self):
        pass

    @staticmethod
    def check_palindrome(s):
        s = str(s)
        stack = ArrayStack()
        even = 1 if len(s) % 2 else 0
        half = len(s) // 2
        for i in range(half):
            stack.push(s[i])
        ind = half + even
        for i in range(half):
            if stack.pop() != s[ind + i]:
                return False
        return True

    @staticmethod
    def get_words(nm):
        f = open (nm, "r", encoding="utf-8")
        lines = f.read()
        f.close()
        lines = lines.split("\n")
        words = []
        for line in lines:
            try:
                words.append(line.split()[0])
            except:
                pass
        return words

    @staticmethod
    def get_list(fr):
        words = Palindrome.get_words(fr)
        good = []
        for word in words:
            if Palindrome.check_palindrome(word) and word not in good:
                good.append(word)
        return good

    @staticmethod
    def get_palindrome(fr, wh):
        words = Palindrome.get_list(fr)
        f = open(wh, "w", encoding="utf-8")
        for word in words:
            f.write(word + "\n")
        f.close()

Palindrome.get_palindrome("base.lst", "palindrome_uk.txt")
Palindrome.get_palindrome("words.txt", "palindrome_en.txt")



