def my_function(n):  # created a function which can use an input number
    input = [number for number in range(n) if number % 3 == 0 or number % 5 == 0] #created the numbers which divisible by 3 or 5 from 1 to n
    output = sum(input) #summed these numbers
    return output

def main():
    n = 1000
    print("The sum of the numbers which are multiples of 3 and 5 from 1 to 1000 is : ", my_function(n))


if __name__ == '__main__':
    main()
