class Literal:
    def __init__(self, name, is_negative=False):
        self.name = name
        self.is_negative = is_negative

    def __str__(self):
        if self.is_negative:
            return f'¬{self.name}'
        else:
            return self.name

    def __eq__(self, other):
        if not isinstance(other, Literal):
            return False
        return self.name == other.name and self.is_negative == other.is_negative


# x = Literal('x')
# print(x)

# not_x = Literal("x", is_negative=True)
# print(not_x)

# x1 = Literal("x")
# print(x == x1)
