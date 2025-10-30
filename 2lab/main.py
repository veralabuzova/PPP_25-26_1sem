class RomanCalculator:
    def __init__(self):
        self.roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.arabic_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    def to_arabic(self, roman):
        result = 0
        prev = 0
        for char in roman[::-1]:
            value = self.roman_map[char]
            result += value if value >= prev else -value
            prev = value
        return result
    def to_roman(self, num):
        if num <= 0:
            raise ValueError("Римские числа не могут быть ≤ 0")
        result = ""
        for value, symbol in self.arabic_map:
            while num >= value:
                result += symbol
                num -= value
        return result
    def calculate(self, a, b, operation):
        x, y = self.to_arabic(a), self.to_arabic(b)
        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            result = x // y
        else:
            raise ValueError("Неверная операция")
        if result <= 0:
            raise ValueError("Результат ≤ 0")
        return self.to_roman(result)
calc = RomanCalculator()
print(calc.calculate("X", "I", "+"))
