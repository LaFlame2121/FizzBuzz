class FizzBuzz:
    def __init__(self, nummer):
        self.nummer = nummer

    def fizz_buzz(self):
        fizzbuzz_lijst = []
        for i in range(1, self.nummer + 1):
            if i % 15 == 0:
                fizzbuzz_lijst.append("FizzBuzz!")
            elif i % 5 == 0:
                fizzbuzz_lijst.append("Buzz!")
            elif i % 3 == 0:
                fizzbuzz_lijst.append("Fizz!")
            else:
                fizzbuzz_lijst.append(i)
        return fizzbuzz_lijst

    def fizz_buzz_print(self):
        for i in range(1, self.nummer + 1):
            if i % 15 == 0:
                print("FizzBuzz!")
            elif i % 5 == 0:
                print("Buzz!")
            elif i % 3 == 0:
                print("Fizz!")
            else:
                print(i)
