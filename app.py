import streamlit as st
import streamlit.components.v1 as stc


# for csv file 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Loan Prediction")

    st.subheader("Dataset")
    data_file = st.file_uploader("Upload File CSV", type=["csv"])
    if data_file is not None:
        df = pd.read_csv(data_file)
        st.dataframe(df)

        atribute = list(df.columns)

        class_option = st.selectbox('Choose class column:', df.columns)
        
        st.write(df[class_option].value_counts())

if __name__ == "__main__":
    main()
