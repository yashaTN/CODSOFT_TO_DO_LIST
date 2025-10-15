import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="To-Do List", page_icon="📝", layout="centered")

# --- Title ---
st.title("📝 To-Do List App")
st.write("Organize your tasks efficiently using this simple Streamlit app.")

# --- Initialize Session State ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Add New Task ---
st.subheader("Add a New Task")
new_task = st.text_input("Enter a task", key="new_task_input")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success(f"✅ Task added: {new_task}")
        st.rerun()
    else:
        st.warning("⚠️ Please enter a valid task.")

# --- Display To-Do List ---
st.subheader("Your Tasks")
if len(st.session_state.tasks) == 0:
    st.info("No tasks yet. Add a new task above.")
else:
    for i, task_data in enumerate(st.session_state.tasks):
        cols = st.columns([0.7, 0.15, 0.15])
        task_name = task_data["task"]
        is_done = task_data["done"]

        # Checkbox to mark completion
        with cols[0]:
            if is_done:
                st.markdown(f"✅ ~~{task_name}~~")
            else:
                st.write(task_name)

        # Button to mark as done
        with cols[1]:
            if not is_done:
                if st.button("Done", key=f"done_{i}"):
                    st.session_state.tasks[i]["done"] = True
                    st.rerun()

        # Button to delete task
        with cols[2]:
            if st.button("❌", key=f"delete_{i}"):
                del st.session_state.tasks[i]
                st.rerun()

# --- Footer ---
st.markdown("---")
st.caption("✨ Built with Streamlit & Python — A simple To-Do manager by [Your Name]")
