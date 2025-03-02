import streamlit as st
import pandas as pd
import os
from io import BytesIO
import time

# Set up App
st.set_page_config(page_title="📂 Data Sweeper", layout="wide")
st.title("📂 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with the built-in data cleaning and visualization!")


# Input Name
name = st.text_input("📝 Enter Your Name: ")
if(st.button('Submit')):
    st.success(f"Hello, {name}!")


# Upload Files (CSV or Excel)
uploaded_files = st.file_uploader("📂 Upload your file (CSV or Excel): ", type=["csv", "xlsx"], accept_multiple_files = True)



if uploaded_files:
   for file in uploaded_files:
      file_ext = os.path.splitext(file.name)[-1].lower()

      if file_ext == ".csv":
         df = pd.read_csv(file)
      elif file_ext == ".xlsx":
         df = pd.read_excel(file)
      else:
         st.error(f"Unsopported file type: {file_ext}")
         continue

      # Display info about the file
      st.write(f"**File Name:** {file.name}")
      st.write(f"**File Size:** {file.size/1024}")

      # Show 5 rows of our df
      st.write("👀 Preview the head of the Dataframe")
      st.dataframe(df.head())

      # Options for data cleaning
      st.subheader("🧹 Date Cleaning Options")
      if st.checkbox(f"Clean Data for {file.name}"):
         col1, col2 = st.columns(2)

         with col1:
            if st.button(f"🗑️Remove Duplicates from {file.name}"):
               df.drop_duplicates(inplace=True)
               st.write("Duplicates Removed!")

         with col2:
            if st.button(f"🔧Fill Missing Values for {file.name}"):
               numeric_cols = df.select_dtypes(include=['number']).columns
               df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
               st.write("Missing Values Have Been Filled!")

      # Choose Specific Colums to Keep or Convert
      st.subheader("📌Select Colums to Convert")
      columns = st.multiselect(f"Choose Columns for {file.name}", options=df.columns.tolist(), default=df.columns.tolist())
      df = df[columns]


      # Create some Visualizations
      st.subheader("📊 Data Visualization")
      if st.checkbox(f"Show Visualizations for {file.name}"):
         st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

      
      # Convert the File -> CSV or EXCEL 
      st.subheader("🔄 Conversion Options")
      conversion_type = st.radio(f"Convert {file.name} to: ", ["CSV", "Excel"], key=file.name)
      if st.button(f"Convert {file.name}"):
         buffer = BytesIO()
         if conversion_type == "CSV":
            df.to_csv(buffer, index=False)
            file_name = file.name.replace(file_ext, ".csv")
            mime_type = "text/csv"

         elif conversion_type == "Excel":
            with pd.ExcelWriter(buffer) as writer:
               df.to_excel(writer, index=False)
               file_name = file.name.replace(file_ext, "xlsx")
               mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
         buffer.seek(0)

         # Downlaod Button
         st.download_button(
            label=f"⬇️ Download {file.name} as {conversion_type}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
         )
      st.success("🎉 Good job you did it!")

st.markdown(
   """
    ### 👨‍💻 Curious Who Made This??
    - Check out my Profile:  [Github Arsalan4work](http://github.com/Arsalan4work)
"""
)

