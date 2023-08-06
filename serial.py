"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.original = start
        self.flag = True

    def generate(self):
        """Will return the next sequential number"""
        if self.flag:
            self.flag = False
            return self.original
        self.start += 1
        return self.start

    def reset(self):
        """Will reset the number back to original start number"""
        self.start = self.original
        self.flag = True
