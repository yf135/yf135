import random
random_max=10# 默认值

# （类）包含各种数据的格式转换函数 还有数据的随机生成和运算功能 主要负责对分数的格式、生成、运算
class Fraction():
    def __init__(self):
        cinque = random.randint(1, 10)  # 摇骰子1点到10点
        if cinque <= 7:
            self.numerator = random.randint(1, random_max)
            self.denominator = 1
            self.interger = 0
        else:
            self.numerator = random.randint(1, random_max)
            self.denominator = random.randint(1, random_max)
            self.integer = 0

    def to_string_simplified(self):
        if self.numerator // self.denominator > 0 and self.numerator % self.denominator != 0:
            integer = self.numerator // self.denominator
            numerator = self.numerator % self.denominator
            gcd1 = Fraction.gcd(numerator, self.denominator)
            numerator = numerator // gcd1
            self.denominator = self.denominator // gcd1
            if self.denominator == 1:
                return f"{integer}\'{numerator}"
            return f"{integer}\'{numerator}/{self.denominator}"
        if self.numerator == self.denominator:
            self.integer = 1
            self.numerator = 0
            self.denominator = 1
            return f"{1}"
        gcd1 = Fraction.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd1
        self.denominator = self.denominator // gcd1
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def from_string(self, Fraction_str):
        self.integer = 0
        if "\'" in Fraction_str:
            integer_part, Fractional_part = Fraction_str.split("\'")
            self.integer = int(integer_part)
            numerator, denominator = Fractional_part.split("/")
            self.denominator = int(denominator)
            self.numerator = self.integer * self.denominator + int(numerator)

        # 处理普通分数
        elif "/" in Fraction_str:
            numerator, denominator = Fraction_str.split("/")
            self.denominator = int(denominator)
            self.numerator = int(numerator)

        # 处理整数
        else:
            self.integer = int(Fraction_str)
            self.numerator = 0
            self.denominator = 1
        return self

    # 辗转相除法求最大公约数
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Fraction.gcd(b, a % b)

    def common_denominator(self, fraction_str):
        if '\'' in fraction_str:
            integer_part, Fractional_part = fraction_str.split("\'")
            integer_part = int(integer_part)
            numerator, denominator = Fractional_part.split("/")
            denominator = int(denominator)
            numerator = integer_part * denominator + int(numerator)
            return f"{numerator}/{denominator}"
        if '/' not in fraction_str:
            return f"{fraction_str}/1"
        else:
            return fraction_str

    def add(self, fraction_a, fraction_b):
        fraction_a = self.common_denominator(fraction_a)
        fraction_b = self.common_denominator(fraction_b)
        numerator_a, denominator_a = fraction_a.split("/")
        numerator_b, denominator_b = fraction_b.split("/")
        numerator = int(numerator_a) * int(denominator_b) + int(numerator_b) * int(denominator_a)
        denominator = int(denominator_a) * int(denominator_b)
        gcd = Fraction.gcd(numerator, denominator)
        return f"{numerator // gcd}/{denominator // gcd}"

    def sub(self, fraction_b, fraction_a):
        fraction_a = self.common_denominator(fraction_a)
        fraction_b = self.common_denominator(fraction_b)
        numerator_a, denominator_a = fraction_a.split("/")
        numerator_b, denominator_b = fraction_b.split("/")
        numerator = int(numerator_a) * int(denominator_b) - int(numerator_b) * int(denominator_a)
        if numerator < 0:
            return "fail"
        denominator = int(denominator_a) * int(denominator_b)
        gcd = Fraction.gcd(numerator, denominator)
        return f"{numerator // gcd}/{denominator // gcd}"

    def mul(self, fraction_a, fraction_b):
        fraction_a = self.common_denominator(fraction_a)
        fraction_b = self.common_denominator(fraction_b)
        numerator_a, denominator_a = fraction_a.split("/")
        numerator_b, denominator_b = fraction_b.split("/")
        numerator = int(numerator_a) * int(numerator_b)
        denominator = int(denominator_a) * int(denominator_b)
        gcd = Fraction.gcd(numerator, denominator)
        return f"{numerator // gcd}/{denominator // gcd}"

    def div(self, fraction_b, fraction_a):
        fraction_a = self.common_denominator(fraction_a)
        fraction_b = self.common_denominator(fraction_b)
        numerator_a, denominator_a = fraction_a.split("/")
        numerator_b, denominator_b = fraction_b.split("/")
        if int(numerator_b) == 0:
            return "fail"
        numerator = int(numerator_a) * int(denominator_b)
        denominator = int(numerator_b) * int(denominator_a)
        gcd = Fraction.gcd(numerator, denominator)
        return f"{numerator // gcd}/{denominator // gcd}"
