import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")

input_box = sg.InputText(tooltip="Ener todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print("Hello")

    match(event):
        case 'Add':
            print('Add button clicked')

            todo = todo + "\n"
            todos = get_todos()

            todos.append(todo)

        # file = open('todos.txt','w')
        # file.writelines(todos)
        # file.close()

            write_todos(todos)

        case WIN_CLOSED:
            break;
            window.close()



