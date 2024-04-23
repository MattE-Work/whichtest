#imports
import streamlit as st
import numpy as np
import pandas as pd

#functions

#--------------------------
#chi square goodness of fit

#functions to check assumptions:

def chi_square_goodness_of_fit_assumptions():
    """
    Displays the assumptions required for conducting a Chi-square goodness of fit test.
    """
    dict_assumptions = {
        "Sufficient Sample Size": "Each category or class should have an expected frequency of at least 5. This is necessary to ensure the validity of the test results, as the Chi-square test may not perform well with smaller expected frequencies.",
        "Independent Observations": "Each observation must be independent of others. This means the selection of one observation should not influence or affect the selection of another.",
        "One-Dimensional Categories": "Data must be categorized into mutually exclusive classes. This means each observation can belong to one and only one category.",
        "Fixed Categories": "The number of categories into which data are classified should be fixed prior to the study. This prevents categories from being tailored based on the observed data.",
        "Sample data": "The test is applied to sample data and assumes that the data points are drawn from a larger population."
    }

    with st.expander("Click for this test's assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")


#--------------------------------

def derive_expected_frequencies(df):
    """
    Allows the user to specify how to derive expected frequencies for a Chi-square goodness of fit test.

    Args:
    df (DataFrame): The dataframe containing observed counts.

    Returns:
    dict: Dictionary of expected frequencies if derivable, otherwise None.
    """
    
    col1, col2 = st.columns(2)

    list_df_col_names = list(df.columns)
    list_options = ["---"]
    for item in list_df_col_names:
        list_options.append(item)

    with col1:
        category_column = st.selectbox(
            "Select column name containing category labels",
            options=list_options)
    
    with col2:
        observed_column = st.selectbox(
            "Select column name containing observed counts for each category label",
            options=list_options)

    method = st.selectbox(
        "Select a method to calculate expected frequencies",
        [
            "---", 
            "Theoretical distribution", # - not yet incorporated", 
            "Proportional allocation", #- not yet incorporated", 
            "Uniform distribution"
            ],
        help="""Select:
        \n'**Theoretical distribution**' to manually specify expected counts, 
        \n'**Proportional allocation**' to assign a percentage to each category, or 
        \n'**Uniform distribution**' to assume equal frequencies across categories."""
    )
    
    current_total = 0
    total_sum = df[observed_column].sum()
    total_count = df[category_column].count()
    if method == "---":
        st.write("Please select a method to calculate expected frequencies.")
        #return None
    
    elif method == "Uniform distribution":
        # Uniform distribution, every category has the same expected frequency
        total_sum = df[observed_column].sum()

        #st.write(total_count)
        unique_categories = df[category_column].nunique()
        expected_frequency = total_sum / unique_categories
        expected_frequencies = {cat: expected_frequency for cat in df[category_column].unique()}
    
    elif method == "Theoretical distribution":
        st.write("Enter the expected frequency for each category:")
        
        #total_sum = df[observed_column].sum()
        #total_count = df[category_column].count()

        expected_frequencies = {}
        for category in df[category_column].unique():
            freq = st.number_input(f"Expected frequency for {category}", min_value=0, value=0, step=1)
            expected_frequencies[category] = freq
            current_total += freq


    elif method == "Proportional allocation":
        st.write("Enter the proportion (as a percentage) for each category:")
        
        #total_sum = df[observed_column].sum()
        #total_count = df[category_column].count()
        
        expected_frequencies = {}
        
        if current_total > total_sum:
            st.write(f":red[Total expected count ({current_total}) is greater than total observed count ({current_total}) - adjust so these match]")
        elif current_total < total_sum:
            st.write(f":red[Total expected count ({current_total}) is less than total observed count ({current_total}) - adjust so these match]")

        for category in df[category_column].unique():
            percent = st.slider(f"Percentage for {category}", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
            expected_frequency = round((percent / 100) * total_sum, 0)
            expected_frequencies[category] = expected_frequency
            current_total += expected_frequency
            st.write(f"Equating to expected frequency: {expected_frequency}")
    
    #st.write(current_total)
    if method != 'Uniform distribution':
        if current_total > total_sum:
            st.write(f":red[Total expected count ({current_total}) is greater than total observed count ({total_sum}) - adjust so these match. You have to reduce by {current_total - total_sum}.]")
        elif current_total < total_sum: 
            st.write(f":red[Total expected count ({current_total}) is less than total observed count ({total_sum}) - adjust so these match. You have {total_sum - current_total} remaining.]")

    #st.write(expected_frequencies)
    # Validate that all expected frequencies are at least 5
    if any(freq < 5 for freq in expected_frequencies.values()):
        st.error("All expected frequencies must be 5 or more to meet Chi-square test requirements.")
        return None

    df['Expected'] = df[category_column].map(expected_frequencies)
    
    return df, observed_column, category_column

#--------------------------------

def check_expected_frequencies(df, observed_column, category_column):
    """
    Checks if the expected frequencies for each category in a Chi-square goodness of fit test are at least 5.
    
    Args:
    data (pd.Series): A pandas Series containing the observed categorical data.
    expected_frequencies (dict): A dictionary with categories as keys and their expected frequencies as values.
    
    Returns:
    bool: True if all expected frequencies are >= 5, False otherwise.
    """
    # Calculate the actual frequencies
    actual_frequencies = df[observed_column]
    
    #extract observed frequencies
    expected_frequencies = df['Expected']
    
    #extract categories
    category_labels = df[category_column]

    
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

    # Display frequencies and their check results
    with st.expander("Expected Frequencies Check"):
        st.write("### Frequency Check for Each Category:")
        expected_all_above_five_count = True

        for i in range(len(actual_frequencies)):
            
            if expected_frequencies[i] < 5:
                st.write(f"Category '{category_labels[i]}': Expected Frequency = {expected_frequencies[i]}, **Not sufficient** (less than 5)")
                expected_all_above_five_count = False
            else:
                st.write(f"Category '{category_labels[i]}': Expected Frequency = {expected_frequencies[i]}, Sufficient")


        # Conclusion based on the checks
        #if expected_all_above_five_count:
        #    st.success("All categories have sufficient expected frequencies. You can proceed with the Chi-square goodness of fit test.")
        #else:
        #    st.error("One or more categories do not have sufficient expected frequencies. Consider combining some categories or using a different statistical test.")

    return expected_all_above_five_count

#------------------------------------
# <<< Main Function to Render Checks >>>
#------------------------------------

def render_chi_square_goodness_of_fit_test_checks(df):
    #render assumptions
    chi_square_goodness_of_fit_assumptions()

    df_location, observed_column, category_column = derive_expected_frequencies(df)

    #render the assumptions in separate tabs
    tab1, tab2 = st.tabs(['Expected frequencies check', 'Other assumptions'])
    
    with tab1:
        expected_all_above_five_count = check_expected_frequencies(df, observed_column, category_column)

    with tab2:
        st.write("You must assure yourself the other assumptions are true for your data set as these are dependent on your awareness of local context / data set.")

    if expected_all_above_five_count:
        st.success("Expected frequencies assumption met. If you are assured of the other assumptions (see drop down above), you can proceed with the Chi Square Goodness of Fit test.")
        return True
    else:
        st.error("The assumption is not met. Consider using the **Wilcoxon Signed-Rank Test** non-parametric alternative.")
        return False