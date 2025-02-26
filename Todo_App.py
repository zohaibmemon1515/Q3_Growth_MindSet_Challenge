import streamlit as st
import datetime
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

st.set_page_config(page_title="🚀 Growth_MindSet_Todo_App", layout="wide")

st.markdown(
    """
    <style>
        .glass-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
            margin-bottom: 15px;
        }
        .glass-card:hover {
            transform: scale(1.02);
        }
        .edit-input {
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🚀 Growth_MindSet_Todo_App")
st.sidebar.header("➕ Add New Task")

task_name = st.sidebar.text_input("Task Name")
priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"], index=1)
due_date = st.sidebar.date_input("Due Date", datetime.date.today())

if st.sidebar.button("Add Task"):
    if task_name.strip():
        tasks.append({
            "task": task_name.strip(),
            "priority": priority,
            "due_date": str(due_date),
            "completed": False
        })
        save_tasks(tasks)
        st.rerun()
    else:
        st.sidebar.warning("Task name cannot be empty!")

st.subheader("📋 To-Do List")

pending_tasks = [task for task in tasks if not task["completed"]]

for index, task in enumerate(pending_tasks):
    with st.container():
        st.markdown(
            f"""
            <div class='glass-card'>
                <strong>{task['task']}</strong> - {task['priority']} - Due: {task['due_date']}
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("✅ Done", key=f"done_{index}"):
                task["completed"] = True
                save_tasks(tasks)
                st.rerun()
        
        with col2:
            if st.button("✏️ Edit", key=f"edit_{index}"):
                st.session_state[f"edit_mode_{index}"] = True
                st.rerun()

        with col3:
            if st.button("❌ Delete", key=f"delete_{index}"):
                tasks.remove(task)
                save_tasks(tasks)
                st.rerun()

        if st.session_state.get(f"edit_mode_{index}", False):
            new_task_name = st.text_input("Edit Task", task["task"], key=f"input_{index}", label_visibility="collapsed")
            if st.button("💾 Save", key=f"save_{index}"):
                if new_task_name.strip():
                    task["task"] = new_task_name.strip()
                    save_tasks(tasks)
                    st.session_state[f"edit_mode_{index}"] = False
                    st.rerun()
                else:
                    st.warning("Task name cannot be empty!")

st.subheader("✔️ Completed Tasks")
completed_tasks = [task for task in tasks if task["completed"]]

if completed_tasks:
    for task in completed_tasks:
        st.markdown(f"✅ **{task['task']}** - {task['priority']} - {task['due_date']}")
else:
    st.info("No completed tasks yet.")

if st.button("🗑️ Clear All Tasks"):
    save_tasks([])
    st.rerun()
