def get_todos():
    with open(r"\python\course-examples\python\files\todos.txt",'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

todos = []


while True:
    user_action = input("Type add, show, edit, complete or exit.. \n")
    user_action = user_action.strip()

    # if 'add' in user_action or 'new' in user_action:

    if user_action.startswith('add'):

        todo = user_action[4:]
        todo = todo + "\n"
        todos = get_todos()

        todos.append(todo)

        # file = open('todos.txt','w')
        # file.writelines(todos)
        # file.close()

        with open(r"\python\course-examples\python\files\todos.txt",'w') as file:
            file.writelines(todos)


    elif  user_action.startswith('show'):
        # file = open(r"\python\course-examples\python\files\todos.txt",'r')
        # todos = file.readlines()

        todos = get_todos()

        # new_todos = [item.strip() for item in todos]
        for index, item in enumerate(todos):
            # item = item.title()
            # print(index, '-', item)
            item = item.strip()
            row = f"{index + 1}-{item}"
            print(row)
        print(f"length is {index +1}")
    elif  user_action.startswith('exit'):
        break;
    elif  user_action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            item_to_remove = todos[number - 1]
            item_to_remove = item_to_remove.strip("\n")
            todos.pop(number - 1)

            with open(r"\python\course-examples\python\files\todos.txt",'w') as file:
                file.writelines(todos)

            message = f"item {item_to_remove} was removed from todos"
            print(message)
        except:
            print("You have entered incorrect item for completion. Retry again..")
            continue

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter a new todo item')
            todos[number] = new_todo + "\n"

            with open(r"\python\course-examples\python\files\todos.txt",'w') as file:
                file.writelines(todos)
        except ValueError:
            print("your command is not valid")
            continue
    else:
        print("Hey, you have entered incorrect command")

print("Bye")
