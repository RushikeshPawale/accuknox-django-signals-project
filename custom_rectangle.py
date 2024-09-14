class CustomRectangle:
    def __init__(self, rect_length: int, rect_width: int):
        self.rect_length = rect_length
        self.rect_width = rect_width

    def __iter__(self):
        yield {'length': self.rect_length}
        yield {'width': self.rect_width}

if __name__ == "__main__":
    # instance of CustomRectangle
    my_rectangle = CustomRectangle(rect_length=50, rect_width=25)

    # loop for iteration
    for dimension in my_rectangle:
        print(dimension)
