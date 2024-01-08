import streamlit as st

def main():
    st.title("Simple Streamlit App")

    # Text input
    user_input = st.text_input("Enter text:")

    # Button to trigger an action
    if st.button("Submit"):
        # Output the entered text
        st.success(f"You entered: {user_input}")

if __name__ == "__main__":
    main()
