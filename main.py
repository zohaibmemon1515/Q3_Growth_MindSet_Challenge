import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import os

Data_File = "Library_data.csv"

def load_data():
    if os.path.exists(Data_File):
        return pd.read_csv(Data_File)
    return pd.DataFrame(columns=["Title", "Author", "Genre", "Year", "ISBN", "Read Status"])

def save_data(data):
    data.to_csv(Data_File, index=False)

def text_to_speech(text):
    tts = gTTS(text, lang='en')
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

if "Library_data" not in st.session_state:
    st.session_state.Library_data = load_data()

st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput input {
        border-radius: 5px;
        padding: 10px;
    }
    .stHeader {
        color: #4CAF50;
    }
    .stDataFrame {
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("📚 Welcome to Our Scholar’s Community")


menu_options = [
    "Add a Book",
    "Remove a Book",
    "Search for a Book",
    "Display All Books",
    "Display Statistics",
    "Export/Import Library",
    "Exit"
]
choice = st.sidebar.selectbox("Menu", menu_options)


if choice == "Add a Book":
    st.header("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        genre = st.text_input("Genre")
        year = st.number_input("Publication Year", min_value=1800, max_value=2100)
        isbn = st.text_input("ISBN")
        read_status = st.selectbox("Have you read this book?", ["Yes", "No"])
        submit = st.form_submit_button("Add Book")

    if submit:
        new_book = pd.DataFrame([[title, author, genre, year, isbn, read_status == "Yes"]], columns=["Title", "Author", "Genre", "Year", "ISBN", "Read Status"])
        st.session_state.Library_data = pd.concat([st.session_state.Library_data, new_book], ignore_index=True)
        save_data(st.session_state.Library_data)
        st.success("Book added successfully!")


elif choice == "Remove a Book":
    st.header("🗑️ Remove a Book")
    book_to_remove = st.selectbox("Select a Book to Remove", st.session_state.Library_data["Title"])
    if st.button("Remove Book"):
        st.session_state.Library_data = st.session_state.Library_data[st.session_state.Library_data["Title"] != book_to_remove]
        save_data(st.session_state.Library_data)
        st.success("Book removed successfully!")


elif choice == "Search for a Book":
    st.header("🔍 Search for a Book")
    search_by = st.radio("Search by:", ["Title", "Author"])
    search_query = st.text_input(f"Enter the {search_by}")
    if search_query:
        if search_by == "Title":
            search_results = st.session_state.Library_data[st.session_state.Library_data["Title"].str.contains(search_query, case=False)]
        else:
            search_results = st.session_state.Library_data[st.session_state.Library_data["Author"].str.contains(search_query, case=False)]
        st.write(search_results)

        if not search_results.empty:
            selected_book = st.selectbox("Select a Book to Listen its Details", search_results["Title"])
            if selected_book:
                book_detail = search_results[search_results["Title"] == selected_book].iloc[0]
                details_text = f"Title: {book_detail['Title']}, Author: {book_detail['Author']}, Genre: {book_detail['Genre']}, Year: {book_detail['Year']}, ISBN: {book_detail['ISBN']}"
                st.write("Book Details:", details_text)

                audio_file = text_to_speech(details_text)
                st.audio(audio_file, format="audio/mp3")
        else:
            st.write("No books found.")
    else:
        st.write(st.session_state.Library_data)

elif choice == "Display All Books":
    st.header("📖 Display All Books")
    if not st.session_state.Library_data.empty:
        st.write(st.session_state.Library_data)
    else:
        st.write("Your library is empty.")

elif choice == "Display Statistics":
    st.header("📊 Display Statistics")
    total_books = len(st.session_state.Library_data)
    read_books = st.session_state.Library_data["Read Status"].sum()
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {percentage_read:.2f}%")

elif choice == "Export/Import Library":
    st.header("📤 Export/Import Library")
    if st.button("Export Library to CSV"):
        st.session_state.Library_data.to_csv("library.csv", index=False)
        st.success("Library Export Successfully")

    uploaded_file = st.file_uploader("Import Library from CSV", type=["csv"])
    if uploaded_file:
        import_data = pd.read_csv(uploaded_file)
        st.session_state.Library_data = pd.concat([st.session_state.Library_data, import_data], ignore_index=True)
        save_data(st.session_state.Library_data)
        st.success("Library Imported Successfully")

elif choice == "Exit":
    st.header("👋 Exit")
    save_data(st.session_state.Library_data)
    st.success("Library saved to file. Goodbye!")
    st.stop()