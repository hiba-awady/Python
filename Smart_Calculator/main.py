import operations
import history
import utils

history.read_history()

menu = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
    "^": "Power",
    "%": "Percentage",
    "last": "Last Operation",
    "stats": "Statistics",
    "search": "Search History",
    "dl": "Delete Last Operation",
    "counter": "Count Operations",
    "square": "Square Root",
    "history": "Show history",
    "clear": "Clear history",
    "exit": "Exit program"
}

operations_map = {
    "+": operations.addition,
    "-": operations.subtraction,
    "*": operations.multiply,
    "/": operations.divide,
    "^": operations.power,
    "%": operations.percentage,
    "square": operations.square_root
}

while True:

    print("\n========== Calculator ==========\n")

    for key, value in menu.items():
        print(f"{key:<10} --> {value}")

    cmd = input("\nEnter command: ").lower()

    # ================= EXIT =================

    if cmd == "exit":
        print("Good bye")
        break

    # ================= HISTORY =================

    if cmd == "history":
        history.show_history()
        continue

    # ================= CLEAR =================

    if cmd == "clear":
        history.clear_history()
        continue
    
      # ================= Last =================
        
    if cmd == "last":

        result = history.last()

        if result is not None:
            print(result)

        continue
    

    # ================= Counter =================
    if cmd == "counter":

        result = history.counter()

        print("Total operations =", result)

        continue
    
    # ================= Search =================
    if cmd == "search":

        num = input("Search what = ")

        result = history.search(num)

        if len(result) == 0:

            print("No results found\n")

        else:

            print("\nSearch Results:\n")

            for item in result:
                print(item)

            print()

        continue

    # ================= Delete_last  =================


    if cmd == "dl":

        result = history.delete_last()

        if result is not None:
            print("Deleted:", result)

        continue
     # ================= Statistics =================

    
# ================= Statistics =================

    if cmd == "stats":

        result = history.statistics()

        total = 0

        for value in result.values():
            total += value

        print("Total Operations =", total)

        for key, value in result.items():

            if value > 0:
                print(f"{key:<15} : {value}")

        continue

        
    # ================= VALIDATION =================

    if cmd not in operations_map:
        print("Invalid command")
        continue

    # ================= SQUARE ROOT =================

    if cmd == "square":

        number = utils.get_number("Enter number: ")

        result = operations.square_root(number)

        if result is not None:
            print("Result =", result)

        continue

    # ================= NORMAL OPERATIONS =================

    a = utils.get_number("First number: ")
    b = utils.get_number("Second number: ")

    result = operations_map[cmd](a, b)

    if result is not None:
        print("Result =", result)