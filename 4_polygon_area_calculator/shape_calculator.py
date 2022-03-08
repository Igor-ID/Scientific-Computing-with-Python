class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width < 50 and self.width < 50:
            row = '*' * self.width
            res = ''
            for i in range(self.height):
                res += row + '\n'
            return res
        return "Too big for picture."

    def get_amount_inside(self, figure):
        return self.get_area() // figure.get_area()


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

    def __repr__(self):
        return f'Square(side={self.height})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side