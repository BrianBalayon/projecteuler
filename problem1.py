'''

Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

'''


def main():
    threes = 0
    fives = 0
    for i in range(1, 1000):
        if not i % 3:
            threes += i
        '''
        Using else-if to avoid adding the same number twice.
        Ex. 15, 75, and 150 are multiples of 3 and 5
        '''
        elif not i % 5:
            fives += i
    print("Sum of Multiples of 3: ", threes)
    print("Sum of Multiples of 5: ", fives)
    print("Combined sum of both: ", threes+fives)


if __name__ == "__main__":
    main()
