import streamlit as st

# Hardcoded credentials for demonstration
admin_username = "admin"
admin_password = "adminpass"
user_username = "user"
user_password = "userpass"

# Function to verify login
def login(username, password):
    if username == admin_username and password == admin_password:
        return "admin"
    elif username == user_username and password == user_password:
        return "user"
    else:
        return None

# Streamlit app
def main():
    st.title("Login Page")

    # Create a login form
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        role = login(username, password)
        
        if role == "admin":
            st.success("Welcome, Admin!")
            # Admin page content
            st.write("This is the admin dashboard.")
        elif role == "user":
            st.success("Welcome, User!")
            # User page content
            st.write("This is the user dashboard.")
        else:
            st.error("Invalid username or password.")

if __name__ == "__main__":
    main()
