#import libraries
import streamlit as st
import pandas as pd
import altair as alt
from scipy.stats import chi2_contingency

#------------------------------------
# <<< Function to render assumptions >>>
#------------------------------------

def display_fishers_exact_test_assumptions():
    """
    Displays the assumptions required for conducting Fisher's Exact Test.
    """
    dict_assumptions = {
        "Independence": "The samples must be independent. Each observation is classified into exactly one category, and the sampling or assignment to categories must be independent.",
        "Fixed Margins": "The row and column totals (margins) must be fixed, or 'conditioned'. Fisher's Exact Test is appropriate when the structure of the experiment gives fixed row or column totals.",
        "Binary Data": "The test is applicable for 2x2 contingency tables. Each variable used in the test should have exactly two levels (binary data), e.g., male/female, pass/fail, etc.",
        "Small Sample Size": "Fisher's Exact Test is particularly suited for datasets where sample sizes are small, as it calculates the exact probability of observing the data as extreme, or more, given the null hypothesis."
    }

    with st.expander("Click for Fisher's Exact Test Assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")
            
            if key == "Binary Data":
                # Display an example 2x2 matrix
                example_data = {
                    'Pass': [10, 5],
                    'Fail': [15, 20]
                }
                example_df = pd.DataFrame(example_data, index=['Group 1', 'Group 2'])
                st.write("Example of the required 2x2 contingency table for this test:")
                st.dataframe(example_df)


#------------------------------------
# <<< Function to select columns >>>
#------------------------------------

def select_two_columns_for_fishers_exact_test(df):
    """
    Renders 2x select boxes for the user to choose columns from a dataframe for Fisher's Exact Test.

    Args:
    df (DataFrame): The dataframe from which a column will be selected.

    Returns:
    tuple: A tuple containing the selected column names or None if "---" is selected for either.
    """
    st.write("Please select the column names for the categorical variables you want to include in your analysis:")
    
    # Initialize placeholders
    default_option = "---"
    
    # Get column names and include the placeholder as the first option
    options = [default_option] + list(df.columns)
    
    col1, col2 = st.columns(2)

    with col1:
        # Render select box for column selection    
        selected_column_1 = st.selectbox(
            "Select the First Category Column",
            options=options,
            help="Select the column that contains the categorical data for the first group"
        )
  
    with col2:
        # Render select box for column selection    
        selected_column_2 = st.selectbox(
            "Select the Second Category Column",
            options=options,
            help="Select the column that contains the categorical data for the second group"
        )

    # Return the selected columns if both are valid selections
    if selected_column_1 != "---" and selected_column_2 != "---":
        return selected_column_1, selected_column_2
    else:
        return None, None

#------------------------------------
# <<< Remind user to be assured that each observation is independent >>>
#------------------------------------

def check_independence():
    """
    Informs the user about the independence assumption required for Fisher's Exact Test.

    Returns:
    None: Displays information in Streamlit.
    """
    with st.expander("Check Independence Assumption"):
        st.write("""
        **Independence Assumption for Fisher's Exact Test:**
        Each sample or observation must be collected independently of the others. This is crucial for the validity of the test results. Ensure that:
        - Each subject or experimental unit contributes only one data point to the table.
        - The sampling or allocation to categories (e.g., treatment/control) does not influence other samples or their allocation.
        - There is no clustering or relatedness in the data that might violate independence (e.g., multiple measurements from the same individual should not be treated as independent observations unless appropriate design adjustments are made).
        
        **Action Required:**
        - Review the design of your study or experiment to confirm that these criteria are met.
        - If multiple observations from the same subject are included, consider modifying the analysis to account for this clustering or use another statistical test that handles dependent samples.
        """)

#------------------------------------
# <<< Remind user to ensure fixed margins assumption holds true >>>
#------------------------------------

def check_fixed_margins():
    """
    Informs the user about the fixed margins assumption required for Fisher's Exact Test and suggests methods to ensure this condition is met.

    Returns:
    None: Displays information in Streamlit.
    """
    with st.expander("Check Fixed Margins Assumption"):
        st.write("""
        **Fixed Margins Assumption for Fisher's Exact Test:**
        The totals for each row and column in the contingency table must be fixed prior to the study. This often occurs by design in experiments where the number of samples in each group is predetermined.

        **Why This Matters:**
        Fisher's Exact Test calculates the probability of obtaining the observed distribution of data under the null hypothesis that there are no differences between the groups, given these fixed margins. Deviations from this assumption may require a different statistical approach.

        **Study Design Methods to Ensure Fixed Margins:**
        - **Randomized Controlled Trials (RCTs):** Random assignment of participants to treatment or control groups.
        - **Block Randomization:** Ensures equal numbers of participants across treatments in each block.
        - **Quota Sampling:** Predetermined quotas based on specific characteristics ensure fixed sample sizes.
        - **Stratified Sampling:** Population is divided into strata, and samples are taken from each stratum to meet predefined size targets.

        **Action Required:**
        - Review the design of your study to ensure that the number of observations in each category was predetermined and not influenced by any experimental outcomes.
        - If your study design does not fix these margins, consider consulting with a statistician or using another appropriate test.
        """)

#------------------------------------
# <<< function to check binary data assumption holds true >>>
#------------------------------------

def check_binary_data(df, column1, column2):
    """
    Checks if the selected columns for Fisher's Exact Test contain exactly two unique values.

    Args:
    df (DataFrame): The dataframe containing the data.
    column1 (str): The first column name.
    column2 (str): The second column name.

    Returns:
    bool: True if both columns are binary, False otherwise.
    """
    # Explanation of what Binary Data means
    with st.expander("Click for explanation"):
        st.write("""
        **Binary Data Assumption for Fisher's Exact Test:**
        \nEach variable used in Fisher's Exact Test should have exactly two levels (binary data), such as 'Yes/No' or 'Male/Female'. 
        This requirement is crucial because Fisher's test calculations are specifically designed for 2x2 contingency tables.
        """)

    # Guidance on how to interpret the data check
    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Binary Data Check:**
        - **Exactly Two Unique Values:** If each of the selected columns contains exactly two unique values, the data structure is appropriate for Fisher's Exact Test.
        - **More or Less than Two Unique Values:** If any column contains more or fewer than two unique values, Fisher's Exact Test may not be suitable without modifying the data or choosing a different statistical method.
        """)
    
    # Perform the binary data check and display results
    with st.expander("Binary Data Check Results"):
        unique_values_column1 = df[column1].nunique()
        unique_values_column2 = df[column2].nunique()
        
        if unique_values_column1 == 2 and unique_values_column2 == 2:
            st.write(f"Both {column1} and {column2} are binary. Assumption satisfied.")
            return True
        else:
            st.error(f"Check failed: {column1} and {column2} must each have exactly two unique values.")
            return False

#------------------------------------
# <<< function to check sample size and expected cell count assumption holds true >>>
#------------------------------------

def check_sample_size_for_fishers_exact_test(df, column1, column2):
    """
    Checks if the sample size and expected counts are adequate for conducting Fisher's Exact Test.

    Args:
    df (DataFrame): The dataframe containing the data.
    column1 (str): The first column name used in the test, representing one categorical variable.
    column2 (str): The second column name used in the test, representing another categorical variable.

    Returns:
    bool: True if the conditions for Fisher's Exact Test are met, False otherwise.
    """
    # Create a contingency table
    contingency_table = pd.crosstab(df[column1], df[column2])

    # Total entries in the contingency table
    total_entries = contingency_table.sum().sum()
    
    # Calculate expected frequencies
    chi2, p, dof, expected = chi2_contingency(contingency_table, correction=False)
    
    # Create a DataFrame from the expected frequencies
    expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)


    # Check the conditions on expected frequencies
    # Count of expected frequencies >= 5
    count_at_least_5 = (expected >= 5).sum()

    # Total number of cells in the expected frequencies table
    total_cells = expected.size

    # Checking if all expected frequencies are at least 5
    all_cells_not_5_or_more = count_at_least_5 != total_cells

    # Explanation of sample size and expected count considerations
    with st.expander("Click for explanation"):
        st.write("""
        **Sample Size and Expected Count Considerations for Fisher's Exact Test:**
        \nFisher's Exact Test calculates the exact probability of observing the given data under the null hypothesis, which is especially useful when sample sizes are small or expected frequencies in any cell of a 2x2 contingency table are low.
        """)

    # Guidance on interpreting sample size and expected count adequacy
    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Sample Size and Expected Count Adequacy:**
        - **Total patients < 20 OR Total > 20 but not all cells have expected count ≥ 5:** Fisher's Exact Test is appropriate.
        - **Total patients > 20 and all cells have expected count ≥ 5:** The use of Chi-square test might be more appropriate.
        """)

    # Display results
    with st.expander("Sample Size and Expected Counts Check Results"):
        st.write(f"""The total sample size is: {total_entries}.
        \nSeparate tables showing the actual and expected frequencies are displayed belwow.""")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Actual counts')
            st.write(contingency_table)
        with col2:
            st.subheader('Expected counts')
            st.write(expected_df)

        if total_entries < 20 or (total_entries > 20 and all_cells_not_5_or_more):
            st.write(f"Total sample size is {total_entries}. Conditions are suitable for Fisher's Exact Test.")
            return True
        else:
            st.error(f"Total sample size is {total_entries}, and expected counts are too high in all cells for Fisher's Exact Test.")
            return False


#-----------------------------------------------

def check_assumptions_and_recommend_fishers_exact(binary_data_check, sample_size_check):
    """
    Asks the user to confirm assumptions based on the previous checks and context knowledge
    to determine if Fisher's Exact Test can be used.

    Args:
    sample_size_check (bool): Result from the previous function indicating if the sample size assumption is met.

    Returns:
    str: Recommendation on which statistical test to use based on the assumptions checks.
    """
    st.subheader("Confirming interpretation of assumption checks")

    # If the sample size assumption is already violated, skip asking further and recommend an alternative
    # Initialize the list to collect issues
    issues = []
    
    # Check the binary data assumption
    if not binary_data_check:
        issues.append("binary data assumption is violated (data should be in a 2x2 contingency table format)")
    
    # Check the sample size assumption
    if not sample_size_check:
        issues.append("sample size assumption is violated (all expected frequencies cannot be 5 or more)")
    
    # If any key assumptions are violated, display the error and suggest alternatives
    if issues:
        issues_str = " and ".join(issues) + ". Cannot proceed with Fisher's Exact Test."
        st.error(f"The {issues_str} Consider using an alternative test.")
        return False


    col1, col2 = st.columns(2)
    with col1:
        # If the sample size assumption is met, ask for confirmation on other assumptions
        independence_confirmation = st.selectbox(
            "Confirm if the samples are independent:",
            options=["---", "Yes", "No"],
            index=0,  # Default to 'Yes'
            help="Each observation should be independent of others. This means the selection of one observation does not influence or affect the selection of another."
        )

    with col2:
        fixed_margins_confirmation = st.selectbox(
            "Confirm if the margins are fixed:",
            options=["---", "Yes", "No"],
            index=0,  # Default to 'Yes'
            help="The row and column totals (margins) must be fixed, or 'conditioned'. This ensures the totals are not influenced by the observed data."
        )

    # Logic based on user confirmations
    if independence_confirmation == "Yes" and fixed_margins_confirmation == "Yes":
        recommendation_string = "All checked assumptions for Fisher's Exact Test are met. You can :green[**proceed with the Fisher's Exact Test**]."
        test_can_be_used = True
        st.write(recommendation_string)
        return test_can_be_used

    elif independence_confirmation == "No" or fixed_margins_confirmation == "No":
        issues = []
        if independence_confirmation == "No":
            issues.append("samples are not independent")
        if fixed_margins_confirmation == "No":
            issues.append("margins are not fixed")
        
        issues_str = ", ".join(issues)
        recommendation_string = f":red[Assumptions not met because **{issues_str}**. Consider using another appropriate statistical test.]"
        test_can_be_used = False
        st.write(recommendation_string)
        return test_can_be_used
    
    elif independence_confirmation == "---" or fixed_margins_confirmation == "---":
        return '' 


#-----------------------------------------------
#Function to render all the above functions in the app:
def render_assumption_checks_for_fishers_exact_test(df):
    #render the assumptions of the test
    display_fishers_exact_test_assumptions()

    #function for user to select the categorical columns
    col1, col2 = select_two_columns_for_fishers_exact_test(df)

    
    tab1, tab2, tab3, tab4 = st.tabs(['Independence', 'Fixed margins', 'Binary data', 'sample size'])
    #Independence
    with tab1:
        #Remind user to be assured of independence (not checked in app)
        check_independence()
    
    #Fixed margins tab
    with tab2:
        check_fixed_margins()
    
    #Binary data 
    with tab3:
        binary_data_assumption_met = check_binary_data(df, col1, col2)
    
    #sample size
    with tab4:
        sample_size_assumption_met = check_sample_size_for_fishers_exact_test(df, col1, col2)

    test_can_be_used_bool = check_assumptions_and_recommend_fishers_exact(binary_data_assumption_met, sample_size_assumption_met )
    
    #return the shapiro bool value
    # if True means normal dist and if all other assumptions met, can use paired t test
    # if False, means not normal dist, recommend using Wilcoxon Signed-Rank Test
    return test_can_be_used_bool