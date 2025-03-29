import streamlit as st
import pandas as pd

st.title("Sample App")
# st.header("Sample App")
# st.subheader("Sample App")
# st.text("Sample App")
# st.write("Sample App")
# st.markdown("""
#     **This is markdown of streamlit**
# """)

# if st.button("Button"):
#     st.success("Button Clicked!")

# checked = st.checkbox("Check me!") # True or False
# if checked:
#     st.write("Checkbox is checked!")


# name = st.text_input("Enter your name", value="")
# # st.write(f"Hello, {name}!")
# age = st.slider("Select your age ", min_value=0, max_value=100, value=25)
# # st.write("Your age is: ", age)
# fav_num = st.text_input("Enter a number")

# if st.button("Submit"):
#     st.write(f"Hello, {name}, Your age is {age}, Your favorite number is {fav_num}")

# data = {"Name": ["Arsalan", "Ahhmed", "Ali", "Sara"], "Age": [23,20,24,21], "City": ["New York", "Paris", "Berlin", "London"]}
# df = pd.DataFrame(data)
# st.dataframe(df) ## Scrollable
# st.table(df) ## Non-Scrollable

# json_data = {
#     "name": "John Doe",
#     "age": 30,
#     "address": {
#         "street" : "123 new york",
#         "city" : "New York"
#     }
# }

# st.json(json_data) ## JSON data

data = {
    "Name": ["Arsalan", "Ahmed", "Ali", "Sara"], 
    "Age": [23,20,24,21], 
    "City": ["New York", "Paris", "Berlin", "London"],
    "Score": [88, 92, 78, 90]
}
df = pd.DataFrame(data)

# city = st.selectbox("Choose a city to filter", df["City"].unique())
# filter_data = df[df["City"] == city]

# st.write(f"Data for city: {city}")
# st.dataframe(filter_data)
value_of_styled = st.number_input("Enter the minumin number to display in yellow: ", value=80)
if st.button("Submit"):
    styled_df = df.style.applymap(lambda x: "background-color: yellow" if isinstance(x, int) and x > value_of_styled else "")
    st.dataframe(styled_df)