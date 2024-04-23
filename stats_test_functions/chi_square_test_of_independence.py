import pandas as pd
import numpy as np
import streamlit as st
from scipy.stats import chi2_contingency

#--------------------------------------------

def chi_square_test_of_independence_assumptions():
    """
    Displays the assumptions required for conducting a Chi-square test of independence.
    """
    dict_assumptions = {
        "Independence within Samples": "Each observation must be independent of the others. For survey data, this means each respondent or subject contributes only one response to each category.",
        "Large Sample Size": "Expected frequencies in each cell of the contingency table should be at least 5. This is necessary for the Chi-square approximation to the distribution of the test statistic to be valid.",
        "Independent Samples": "The observations in one sample must not influence the observations in another. Each sample or group must be sampled independently.",
        "Fixed Marginals": "In the analysis of a contingency table, the row and column totals are considered fixed. This assumption underpins the computation of expected frequencies which are based on these totals.",
        "Categorical Data": "Data must be categorical (nominal or ordinal), not numerical. The Chi-square test assesses frequency data categorized into distinct categories."
    }

    with st.expander("Click for this test's assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")

#--------------------------------------------

def select_sample_columns(df):
    """
    Renders Streamlit select boxes for choosing columns for the two columns to group by from a provided DataFrame.

    Args:
    df (DataFrame): A pandas DataFrame from which to select column names to use in the chi square test of independence.

    Returns:
    column names for col1 and col2
    """

    list_df_col_names = list(df.columns)
    list_options = ["---"]
    for item in list_df_col_names:
        list_options.append(item)

    if df is not None:
        col1, col2 = st.columns(2)
        with col1:
            groupby_col = st.selectbox(
                "Select the first column name to group by (e.g. Gender)", 
                options=list_options, 
                index=0)
        with col2:
            target_col = st.selectbox(
                "Select the second column name to group by (e.g. preference)", 
                options=list_options, 
                index=0)
        return groupby_col, target_col
    else:
        st.error("No DataFrame provided. Please upload data and retry.")
        return None, None

#--------------------------------------------

def convert_long_form_df_to_aggregate_format(df_long_format, group_variable_col, preference_column):
    """
    group_variable_col e.g. gender
    preference_column e.g. preferred appointment time
    """
    # Convert to aggregated form for chi-square test
    df_aggregated = df_long_format.groupby([group_variable_col, preference_column]).size().reset_index(name='Count')
    # Display the aggregated DataFrame
    return df_aggregated


#--------------------------------------------
def check_expected_frequencies(df, groupby_col, target_col):
    """
    Checks if all expected frequencies in a contingency table are at least 5.

    Args:
    df (DataFrame): The dataframe containing the data.
    groupby_col (str): The column in df that denotes the groups.
    target_col (str): The column in df that contains the target categories.

    Returns:
    bool: True if all expected frequencies are at least 5, False otherwise.
    """
    # Creating a contingency table
    contingency_table = pd.crosstab(df[groupby_col], df[target_col])
    
    # Calculate expected frequencies
    chi2, p, dof, expected = chi2_contingency(contingency_table, correction=False)
    
    # Explanation of Expected Frequencies
    with st.expander("What are Expected Frequencies?"):
        st.write("""
        **Expected frequencies** are calculated under the hypothesis of independence between the categories. These frequencies represent the expected counts that would be observed in each cell of the contingency table if there were no association between the variables.
        """)
    
    # Guidance on how to interpret the check
    with st.expander("How to Interpret Expected Frequencies"):
        st.write("""
        **Interpreting Expected Frequencies for the Chi-square Test:**
        - **Frequencies ≥ 5**: Satisfies the assumption for using the Chi-square test. This is required to ensure the validity of the Chi-square approximation to the chi-square distribution.
        - **Frequencies < 5**: Indicates that the expected frequencies are too low, which can invalidate the results of a Chi-square test due to the approximation to the chi-square distribution becoming unreliable.
        """)

    # Display expected frequencies
    expected_df = pd.DataFrame(expected, columns=contingency_table.columns, index=contingency_table.index)

    with st.expander("Expected Frequencies for Chi-square Test"):
        st.dataframe(expected_df.style.format("{:.2f}"))
    
        # Check if all expected frequencies are at least 5
        if (expected >= 5).all():
            st.write("All expected frequencies are at least 5. Assumption satisfied.")
            return True
        else:
            st.error("Some expected frequencies are less than 5. This may affect the validity of the Chi-square test results.")
            return False

#------------------------------------
# <<< Main Function to Render Checks >>>
#------------------------------------

def render_chi_square_test_of_independence_checks(df):
    
    #render assumptions
    chi_square_test_of_independence_assumptions()

    groupby_col, target_col = select_sample_columns(df)

    #df_aggregated = chi_toi.convert_long_form_df_to_aggregate_format(df, groupby_col, target_col)

    #render the assumptions in separate tabs
    tab1, tab2 = st.tabs(['Expected frequencies check', 'Other assumptions'])
    
    with tab1:
        expected_all_above_five_count = check_expected_frequencies(df, groupby_col, target_col)

    with tab2:
        st.write("You must assure yourself the other assumptions are true for your data set as these are dependent on your awareness of local context / data set.")

    if expected_all_above_five_count:
        st.success("Expected frequencies assumption met. If you are assured of the other assumptions (see drop down above), you can proceed with the Chi Square test of independence.")
        return True
    else:
        st.error("The assumption is not met. Consider using the **Fischer's Exact Test** non-parametric alternative.")
        return False