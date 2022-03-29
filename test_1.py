from fizzbuzz import FizzBuzz


class TestFizzBuzz:

    def test_fizz(self):
        for i in range(1, 100):
            FizzBuzz(i).fizz_buzz()
            if i % 3 == 0:
                assert i == "Fizz!"

    def test_buzz(self):
        for i in range(FizzBuzz(100)):
            if i % 5 == 0:
                assert i == "Buzz!"

    def test_fizzbuzz(self):
        for i in range(FizzBuzz(100)):
            if i % 15 == 0:
                assert i == "FizzBuzz!"
