import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="new todo item",placeholder="Add newtodo...",
              on_change=add_todo, key='new_todo')

print("Hello")