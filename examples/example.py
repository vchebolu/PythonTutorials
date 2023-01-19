# todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit.. \n")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo activity") + "\n"

            # file = open("files/todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open(r"\python\course-examples\python\files\todos.txt",'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt','w')
            # file.writelines(todos)
            # file.close()

            with open(r"\python\course-examples\python\files\todos.txt",'w') as file:
                file.writelines(todos)


        case 'show' | 'display':
            # file = open(r"\python\course-examples\python\files\todos.txt",'r')
            # todos = file.readlines()

            todos=[]

            with open(r"\python\course-examples\python\files\todos.txt",'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip() for item in todos]
            for index, item in enumerate(todos):
                # item = item.title()
                # print(index, '-', item)
                item = item.strip()
                row = f"{index + 1}-{item}"
                print(row)
            print(f"length is {index +1}")
        case 'exit':
            break;
        case 'complete':
            with open(r"\python\course-examples\python\files\todos.txt",'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo item to complete: "))
            item_to_remove = todos[number - 1]
            item_to_remove = item_to_remove.strip("\n")
            todos.pop(number - 1)

            with open(r"\python\course-examples\python\files\todos.txt",'w') as file:
                file.writelines(todos)

            message = f"item {item_to_remove} was removed from todos"
            print(message)

        case 'edit':
            number = int(input("Number of the todo item to edit"))
            number = number - 1
            new_todo = input("Enter new todo") + "\n"

            with open(r"\python\course-examples\python\files\todos.txt",'r') as file:
                todos = file.readlines()

            todos[number] = new_todo

            with open(r"\python\course-examples\python\files\todos.txt",'w') as file:
                file.writelines(todos)
        case whatever:
            print("Hey, you have entered incorrect command")

print("Bye")
