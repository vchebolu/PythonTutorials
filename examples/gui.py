import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")

input_box = sg.InputText(tooltip="Ener todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[
                       [label], [input_box], [add_button],
                       [list_box,edit_button]
                   ],
                   font=('Helvetica',20))
while True:
    event, values = window.read()
    print(1,event)
    print(2, values)
    print(3, values['todo'])

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
            print("Edit button clicked")
            todo_to_edit = values['todos'][0]
            print(f'todos in Edit buttons {todo_to_edit}')
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break;

window.close()
