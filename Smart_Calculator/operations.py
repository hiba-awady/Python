import math
from datetime import datetime
import history



def addition(a, b):

    now = datetime.now()
    tm = now.strftime("%Y-%m-%d %H:%M:%S")

    result = a + b

    text = f"{a} + {b} = {result},    ({tm})"

    history.add_to_memory(text)

    history.save_to_file(text)


    return result


def subtraction(a, b):

    now = datetime.now()
    tm = now.strftime("%Y-%m-%d %H:%M:%S")
    
    result = a - b

    text = f"{a} - {b} = {result},    ({tm})"

    history.add_to_memory(text)

    history.save_to_file(text)

    return result


def multiply(a, b):


    now = datetime.now()
    tm = now.strftime("%Y-%m-%d %H:%M:%S")
    
    result = a * b

    text = f"{a} * {b} = {result},     ({tm})"

    history.add_to_memory(text)

    history.save_to_file(text)

    return result


def divide(a, b):

    try:

        now = datetime.now()
        tm = now.strftime("%Y-%m-%d %H:%M:%S")
        result = a / b

        text = f"{a} / {b} = {result},    ({tm})"

        history.add_to_memory(text)

        history.save_to_file(text)

        return result

    except ZeroDivisionError:

        print("Cannot divide by zero")

        return None


def square_root(x):

    try:
        now = datetime.now()
        tm = now.strftime("%Y-%m-%d %H:%M:%S")
        result = math.sqrt(x)

        text = f"sqrt({x}) = {result},    ({tm})"

        history.add_to_memory(text)

        history.save_to_file(text)

        return result

    except ValueError:

        print("Cannot calculate square root of a negative number")

        return None
    
    

def power(a, b):
    now = datetime.now()
    tm = now.strftime("%Y-%m-%d %H:%M:%S")

    result = a**b

    text = f" {a}^{b} = {result},    ({tm})"
    history.add_to_memory(text)

    history.save_to_file(text)

    return result


def percentage(a, b):

    now = datetime.now()
    tm = now.strftime("%Y-%m-%d %H:%M:%S")

    result = (a * b) / 100

    text = f"{b}% of {a} = {result}, ({tm})"

    history.add_to_memory(text)
    history.save_to_file(text)

    return result