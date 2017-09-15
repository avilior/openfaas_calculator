def handle(s):
    # s is a string  -- todo check
    # parse it looking for two numbers
    # if there are more just take the first two

    try:
        numbers = s.strip().split()
        accumulator = 0
        count = 0
        for n in numbers:
            accumulator += float(n)
            count += 1
            if count == 2:
                break
        print(F"{accumulator}")

    except ValueError as v:
        print(F"*** Value Error: {v}")
    except Exception as x:
        print(F"*** Error: {x}")
