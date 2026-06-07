def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid number")