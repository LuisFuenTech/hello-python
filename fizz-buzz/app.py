def fizz_buzz(input):
    result = ""
    if input % 3 == 0:
        result = "Fizz"
    if input % 5 == 0:
        return f"{result}Buzz"

    return result or input


print(fizz_buzz(10))
