
def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 51):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()