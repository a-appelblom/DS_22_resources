import requests


def url(route: str):
    return f"http://127.0.0.1:8000{route}"


print("Hello from todo app")


def print_menu():
    print(
        """
    1: Add Todo
    2: Get Todo
    3: Delete Todo
    4: Update Todo
    5: Exit program
    """
    )
    pass


def add_todo():
    print("Add todo")
    res = requests.post(url("/add_todo"))
    print(res)
    pass


def delete_todo():
    print("Delete todo")
    res = requests.delete(url("/delete_todo/1"))
    print(res)
    pass


def update_todo():
    print("Update todo")
    res = requests.put(url("/update_todo/1"))
    print(res)
    pass


def get_todo():
    print("Get todo")
    res = requests.get(url("/todos"))
    print(res)
    pass


def main():
    print_menu()
    choice = input("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            add_todo()
        case 2:
            get_todo()
        case 3:
            delete_todo()
        case 4:
            update_todo()
        case 5:
            exit()
        case _:
            print("Please enter a valid choice")
    pass


while __name__ == "__main__":
    main()
