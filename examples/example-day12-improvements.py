def get_todos(filepath):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath,todos_arg):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)


todos = []


while True:
    user_action = input("Type add, show, edit, complete or exit.. \n")
    user_action = user_action.strip()

    # if 'add' in user_action or 'new' in user_action:

    if user_action.startswith('add'):

        todo = user_action[4:]
        todo = todo + "\n"

        todos = get_todos(filepath=r"\python\course-examples\python\files\todos.txt")

        todos.append(todo)

        # file = open('todos.txt','w')
        # file.writelines(todos)
        # file.close()

        write_todos(filepath=r"\python\course-examples\python\files\todos.txt",todos_arg=todos)


    elif  user_action.startswith('show'):
        # file = open(r"\python\course-examples\python\files\todos.txt",'r')
        # todos = file.readlines()

        todos = get_todos(filepath=r"\python\course-examples\python\files\todos.txt")

        # new_todos = [item.strip() for item in todos]
        for index, item in enumerate(todos):
            # item = item.title()
            # print(index, '-', item)
            item = item.strip()
            row = f"{index + 1}-{item}"
            print(row)
        # print(f"length is {index +1}")
    elif  user_action.startswith('exit'):
        break;
    elif  user_action.startswith('complete'):
        try:
            todos = get_todos(filepath=r"\python\course-examples\python\files\todos.txt")

            number = int(user_action[9:])
            item_to_remove = todos[number - 1]
            item_to_remove = item_to_remove.strip("\n")
            todos.pop(number - 1)

            write_todos(filepath=r"\python\course-examples\python\files\todos.txt",todos_arg=todos)

            message = f"item {item_to_remove} was removed from todos"
            print(message)
        except:
            print("You have entered incorrect item for completion. Retry again..")
            continue

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos(filepath=r"\python\course-examples\python\files\todos.txt")

            new_todo = input('Enter a new todo item')
            todos[number] = new_todo + "\n"

            write_todos(filepath=r"\python\course-examples\python\files\todos.txt",todos_arg=todos)
        except ValueError:
            print("your command is not valid")
            continue
    else:
        print("Hey, you have entered incorrect command")

print("Bye")
