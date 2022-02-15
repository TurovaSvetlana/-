
class An_exception:
    def __init__ (self, divider, denominator):
        self.divider = divider
        self.denominator = denominator
    @staticmethod
    def division_by_zero(divider,denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")

div=An_exception(3,18)
print(An_exception.division_by_zero(10,0))
print(An_exception.division_by_zero(20,0.3))
print(div.division_by_zero(70,0))


