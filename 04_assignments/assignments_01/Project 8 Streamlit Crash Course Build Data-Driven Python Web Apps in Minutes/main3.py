import streamlit as st

# col1,col2 = st.columns(2)

# with col1:
#     st.header("Column 1")
#     st.write("This is first column")
#     st.button("Column 1 ")

# with col2:
#     st.header("Column 2")
#     st.write("This is second column")
#     st.button("Column 2 ")

# with st.expander("See more details"):
#     st.write("Here are some additional details")
#     st.line_chart([1,2,5,4,3])

# st.sidebar.title("Navigation")
# options = st.sidebar.selectbox("Choose a page: ", ["Home", "About", "Contact"])

# if options == "Home":
#     st.write("Welcome to home page")
# elif options == "About":
#     st.write("Welcome to about page")
# elif options == "Contact":
#     st.write("Welcome to contact page")

st.set_page_config(page_title="Themed App", layout="wide", initial_sidebar_state="expanded")
st.title("Themed Streamlit App")
st.write("This app has customized theme!")