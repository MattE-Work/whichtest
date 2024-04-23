import scipy.stats as stats
import streamlit as st


#------------------------------------
# <<< Function to render assumptions >>>
#------------------------------------
def display_one_sample_t_test_assumptions():
    """
    Displays the assumptions required for conducting a one-sample t-test.
    """
    dict_assumptions = {
        "Normality": "The data should be normally distributed. This assumption can be checked using a Shapiro-Wilk test.",
        "Independence": "The observations must be independent of each other. This means the data collected from one subject should not influence the data from another.",
        "Scale of Measurement": "The data should be interval or ratio scale, which allows for meaningful comparisons of differences."
    }

    with st.expander("Click for this test's assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")


#------------------------------------
# <<< Function to select columns >>>
#------------------------------------

def select_column_for_one_sample_t_test(df):
    """
    Renders a select box for the user to choose the column from a dataframe for the one-sample t-test.

    Args:
    df (DataFrame): The dataframe from which a column will be selected.

    Returns:
    str: The selected column name or None if "---" is selected.
    """
    st.write("Please select the column for your analysis:")
    
    # Initialize placeholders
    default_option = "---"
    
    # Get column names and include the placeholder as the first option
    options = [default_option] + list(df.columns)
    
    # Render select box for column selection    
    selected_column = st.selectbox(
        "Select the Data Column",
        options=options,
        help="Select the column that contains the numerical data for the one-sample t-test."
    )

    if selected_column == default_option:
        return None
    return selected_column

#------------------------------------
# <<< Function to check normality assumption >>>
#------------------------------------

def check_normality_one_sample_t_test(df, value_column):
    """
    Checks the normality of the data using the Shapiro-Wilk test for a one-sample t-test.

    Args:
    df (DataFrame): The dataframe containing the data.
    value_column (str): The column in df that contains the values to be tested for normality.

    Returns:
    tuple: The Shapiro-Wilk test statistic and the p-value, indicating normality.
    """
    # Extract the data from the specified column
    
    data = df[value_column]

    # Explanation of what a Normality Test is
    with st.expander("What is a Normality Test?"):
        st.write("""
        **Normality tests** such as the **Shapiro-Wilk Test** are used to determine if a dataset is well-modeled by a normal distribution. This test is crucial for methods that assume normality, such as the one-sample t-test, as the conclusions drawn from these tests can be heavily influenced by this assumption.
        """)

    # Guidance on how to interpret the results from the normality test
    with st.expander("How to Interpret Normality Test Results"):
        st.write("""
        **Interpreting the Shapiro-Wilk Test:**
        - **P-value > 0.05**: This suggests that the data can be considered normally distributed under the assumption of normality. This means you can proceed with statistical tests that assume normality.
        - **P-value ≤ 0.05**: This indicates that the data do not follow a normal distribution. You might need to consider using non-parametric alternatives if normality is a crucial assumption for your analysis.
        """)

    # Performing the Shapiro-Wilk test
    stat, p_value = stats.shapiro(data)

    # Displaying the normality check results
    with st.expander("Normality Check Results"):
        st.write(f"Shapiro-Wilk Test Statistic: {stat:.4f}, P-value: {p_value:.4f}")

    return stat, p_value

#------------------------------------
# <<< Main Function to Render Checks >>>
#------------------------------------

def render_one_sample_t_test_checks(df, selected_column):
    display_one_sample_t_test_assumptions()

    #render the assumptions in separate tabs
    tab1, tab2 = st.tabs(['Normality check', 'Other assumptions'])
    
    with tab1:
        stat, p_value = check_normality_one_sample_t_test(df, selected_column)

    with tab2:
        st.write("You must assure yourself the other assumptions are true for your data set as these are dependent on your awareness of local context / data set.")

    if p_value > 0.05:
        st.success("Assumption met. You can proceed with the  for one sample t-test.")
        return True
    else:
        st.error("The assumption is not met. Consider using the **Wilcoxon Signed-Rank Test** non-parametric alternative.")
        return False

