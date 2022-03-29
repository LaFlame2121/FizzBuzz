from fizzbuzz import FizzBuzz


class TestFizzBuzz:

    def test_fizz(self):
        fizzbuzz_lijst = FizzBuzz(100).fizz_buzz()
        for i in range(0, len(fizzbuzz_lijst)):
            if (i+1) % 3 == 0 and (i+1) % 15 != 0:
                assert fizzbuzz_lijst[i] == "Fizz!"

    def test_buzz(self):
        fizzbuzz_lijst = FizzBuzz(100).fizz_buzz()
        for i in range(0, len(fizzbuzz_lijst)):
            if (i + 1) % 5 == 0 and (i+1) % 15 != 0:
                assert fizzbuzz_lijst[i] == "Buzz!"

    def test_fizzbuzz(self):
        fizzbuzz_lijst = FizzBuzz(100).fizz_buzz()
        for i in range(0, len(fizzbuzz_lijst)):
            if (i + 1) % 15 == 0:
                assert fizzbuzz_lijst[i] == "FizzBuzz!"
