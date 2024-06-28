def main():
    number = int(input('Enter your input: '))
    result = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while number >= 2:
        remainder = number % 2
        result.append(remainder)
        number = number // 2
    result.append(number)

    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
