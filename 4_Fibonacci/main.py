def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter a number: "))
    
    for i in range(n):
        print("Fibonacci series: ", fibonacci(i))

if __name__ == "__main__":
    main()