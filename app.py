

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard ")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df.columns = df.columns.str.strip()

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Data Visualization")

    st.write("Columns in the file:", df.columns.tolist())

    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column for visualization", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value for visualization", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write("Filtered columns:", filtered_df.columns.tolist())

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    st.write(f"X-axis column: {x_column}, Y-axis column: {y_column}")

    if st.button("Generate Plot"):
        try:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        except KeyError as e:
            st.error(f"KeyError: {e}. Please check the column names.")    
    else:
      st.write("Waiting on file upload....")

