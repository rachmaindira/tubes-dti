import streamlit as st
import streamlit.components.v1 as stc


# for csv file 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Loan Prediction")
    st.write("This app make can help to classify the risk of the loan which is a high risk or low risk Loan.")
    st.write("Make sure the uploaded data is clean without any blank values ​​or noise so the application can predict it accurately")

    st.subheader("Upload Dataset")
    st.write("Please upload a CSV file format!")
    # upload dataset
    data_file = st.file_uploader("Upload File CSV", type=["csv"])
    if data_file is not None:
        df = pd.read_csv(data_file)
        # menampilkan dataset
        st.dataframe(df)
        # pilih atribut kelas
        atribute = list(df.columns)
        class_option = st.selectbox('Choose class column:', df.columns)
        st.write(df[class_option].value_counts())
        st.write(df[class_option].dtypes)

        if df[class_option].dtypes == 'object':
            st.write('change the class to number type')

if __name__ == "__main__":
    main()
