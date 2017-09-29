class Question:
    answer = None
    text = None


class Add(Question):
    def __init__(self, num1, num2):
        self.text = "{} + {}".format(num1, num2)
        self.answer = num1 + num2

class Subtract(Question):
    def __init__(self, num1, num2):
        self.text = "{} - {}".format(num1, num2)
        self.answer = num1 - num2


class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = "{} x {}".format(num1, num2)
        self.answer = num1 * num2

class Divide(Question):
    def __init__(self, num1, num2):
        higher = max(num1, num2)
        lower = min(num1, num2)
        if num1 != num2 and (higher % lower != 0):
            higher = higher * lower
            lower = lower
        self.text = "{} ÷ {}".format(higher, lower)
        self.answer = int(higher / lower)
