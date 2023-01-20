import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todods.txt"):
    with open("todos.txt","w") as file:
        pass

# sg.theme("Black")
label = sg.Text("Type in a todo")
clock = sg.Text("",key="clock")

el = sg.Text("")
input_box = sg.InputText(tooltip="Ener todo", key="todo")
add_button = sg.Button(mouseover_colors="LightBlue2", image_source="add.png",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[
                       [clock],
                       [label], [input_box], [add_button],
                       [list_box,edit_button, complete_button],
                       [exit_button]
                   ],
                   font=('Helvetica',20))
while True:
    event, values = window.read(timeout=10)
    print(1,event)
    print(2, values)
    print(3, values['todo'])
    window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    match(event):
        case 'Add':
            print('Add button clicked')
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            print(todos)

        case 'Edit':
            try:
                print("Edit button clicked")
                todo_to_edit = values['todos'][0]
                print(f'todos in Edit buttons {todo_to_edit}')
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=('Helvetica',20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetics',20))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break;

window.close()
