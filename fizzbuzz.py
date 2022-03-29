class FizzBuzz:
    def __init__(self, nummer):
        self.nummer = nummer

    def fizz_buzz(self):
        for i in range(1, self.nummer + 1):
            if i % 3 == 0:
                print("Fizz!")
            elif i % 5 == 0:
                print("Buzz!")
            elif i % 15 == 0:
                print("FizzBuzz!")
            else:
                print(i)
