"""Position of number in the fibonacci sequence."""
def fibonnacci(number):
    fibonnacci_numbers = [0, 1]
    n = len(fibonnacci_numbers)
    i = 0
    #adding to the fibonnacci list
    while n <= 10:
        numbers = fibonnacci_numbers[i] + fibonnacci_numbers[i+1]
        i = i + 1
        fibonnacci_numbers.append(numbers)
        n+=1
        print(fibonnacci_numbers)
    if number in fibonnacci_numbers:
        print(fibonnacci_numbers.index(number))


fibonnacci(3) #should return the fourth position
fibonnacci(13) #should return the seventh position