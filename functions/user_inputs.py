import pandas as pd
import streamlit as st




def select_sample_columns(df):
    """
    Renders Streamlit select boxes for choosing columns for two samples from a provided DataFrame.

    Args:
    df (DataFrame): A pandas DataFrame from which to select column names for samples.

    Returns:
    tuple: A tuple containing the selected column names for Sample 1 and Sample 2.
    """

    list_df_col_names = list(df.columns)
    list_options = ["---"]
    for item in list_df_col_names:
        list_options.append(item)


    if df is not None:
        col1, col2 = st.columns(2)
        with col1:
            sample_1_col = st.selectbox(
                "Select the column for Sample 1", 
                options=list_options, 
                index=0)
        with col2:
            sample_2_col = st.selectbox(
                "Select the column for Sample 2", 
                options=list_options, 
                index=0)
        return sample_1_col, sample_2_col
    else:
        st.error("No DataFrame provided. Please upload data and retry.")
        return None, None



#-----------------------------------------------------

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------