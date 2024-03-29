class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return_list = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                return_list.append("FizzBuzz")
            elif i % 3 == 0:
                return_list.append("Fizz")
            elif i % 5 == 0:
                return_list.append("Buzz")
            else:
                return_list.append(str(i))
                
        return return_list
