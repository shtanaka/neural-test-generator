import math


class Calculator:
    def __init__(self):
        self.title = "Calculadora"

    def resolve_eq(self, a, b, c):
        if b * b >= 4 * a * c:
            r1 = ((b * -1) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
            r2 = ((b * -1) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        else:
            r1 = 'nr'
            r2 = 'nr'
        return [r1, r2]

    def resolve_log(self, b, a):
        return math.log(a, b)
