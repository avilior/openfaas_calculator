def handle(s):
    # s is a string  -- todo check
    # parse it looking for two numbers
    # if there are more just take the first two

    try:
        numbers = s.strip().split()

        if len(numbers) == 2:
            if float(numbers[1]) != 0:
                print(F"{float(numbers[0]) / float(numbers[1])}")
            else:
                print(F"*** Divide by zero.")
        else:
            print(F"*** Need two values got {len(numbers)}")

    except ValueError as v:
        print(F"*** Value Error: {v}")
    except Exception as x:
        print(F"*** Error: {x}")
