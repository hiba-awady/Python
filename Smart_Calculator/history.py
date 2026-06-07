History = []


def add_to_memory(text):
    History.append(text)


def save_to_file(text):
    with open("history.txt", "a") as f:
        f.write(text + "\n")


def read_history():
    History.clear()

    try:
        with open("history.txt", "r") as f:
            data = f.read()

            if data == "":
                print("File is empty")
            else:
                History.extend(data.splitlines())

    except FileNotFoundError:
        print("No history file yet")


def show_history():
    if len(History) == 0:
        print("No history yet")
    else:
        for item in History:
            print(item)


def clear_history():
    History.clear()

    with open("history.txt", "w") as f:
        pass

    print("History cleared")
   
    
    
def last():

    if len(History) == 0:
        return None

    return History[-1]


def counter():
    return len(History)


def search(x):
    result=[]
    for i in History:
        if x  in i:
            result.append(i)
    
    return result


def delete_last():

    if len(History) == 0:
        print("No history yet")
        return None

    deleted = History.pop()

    with open("history.txt", "w") as f:

        for item in History:
            f.write(item + "\n")

    return deleted



def statistics():

    stats = {
        "addition": 0,
        "subtraction": 0,
        "multiply": 0,
        "divide": 0,
        "power": 0,
        "percentage": 0,
        "square_root": 0
    }


    for item in History:

        if " + " in item:
            stats["addition"] += 1

        elif " - " in item:
            stats["subtraction"] += 1

        elif " * " in item:
            stats["multiply"] += 1

        elif " / " in item:
            stats["divide"] += 1

        elif "%" in item:
            stats["percentage"] += 1

        elif "√" in item:
            stats["square_root"] += 1

        elif "^" in item:
            stats["power"] += 1
        

    return stats
