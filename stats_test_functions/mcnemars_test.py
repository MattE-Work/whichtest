#import libraries
import streamlit as st
import pandas as pd
#--------------------------
#McNemars Test
#--------------------------

#--------------------------

def display_mcnemars_test_assumptions():
    """
    Displays the assumptions required for conducting McNemar's Test.
    """
    dict_assumptions = {
        "Binary Data": "McNemar's test requires data that can be classified into a binary outcome for each subject under two conditions or at two time points.",
        "Paired Design": "The data must consist of paired observations, which means the observations are collected in pairs, such as before-and-after measurements from the same subjects.",
        "Independence of Pairs": "Each pair of observations must be independent of other pairs. This means the selection of one pair should not influence the selection or outcome of another.",
        "Marginal Homogeneity": "This assumption implies that the marginal totals of each category (success or failure) should be the same across the two conditions. It is often assumed rather than tested."
    }

    with st.expander("Click for McNemar's Test Assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")
            
            if key == "Binary Data":
                # Display an example 2x2 matrix
                example_data = {
                    'Before': [10, 5],  # Example data: 10 passed before and failed after, 5 failed before and passed after
                    'After': [5, 10]   # 5 passed before and after, 10 failed before and after
                }
                example_df = pd.DataFrame(example_data, index=['Pass to Fail', 'Fail to Pass'])
                st.write("Example of the required 2x2 contingency table for this test:")
                st.dataframe(example_df)

#--------------------------
#user selects the columns in their df containing the data labels to use with this test

def select_two_columns_for_mcnemars_test(df):
    """
    Renders 2x select boxes for the user to choose columns from a dataframe for McNemar's Test.

    Args:
    df (DataFrame): The dataframe from which columns will be selected.

    Returns:
    tuple: A tuple containing the selected column names or None if "---" is selected for either.
    """
    st.write("Please select the column names for the paired categories you want to compare in your analysis:")
    
    # Initialize placeholders
    default_option = "---"
    
    # Get column names and include the placeholder as the first option
    options = [default_option] + list(df.columns)
    
    col1, col2 = st.columns(2)

    with col1:
        # Render select box for column selection    
        selected_column_1 = st.selectbox(
            "Select the First Condition Column",
            options=options,
            help="Select the column that contains the categorical data for the first condition (e.g., before treatment)"
        )
  
    with col2:
        # Render select box for column selection    
        selected_column_2 = st.selectbox(
            "Select the Second Condition Column",
            options=options,
            help="Select the column that contains the categorical data for the second condition (e.g., after treatment)"
        )

    # Return the selected columns if both are valid selections
    if selected_column_1 != "---" and selected_column_2 != "---":
        return selected_column_1, selected_column_2
    else:
        return None, None

# Example function call to select columns in your app
#selected_columns = select_two_columns_for_mcnemars_test(df)
#if selected_columns[0] and selected_columns[1]:
#    st.write(f"Selected columns for McNemar's Test: {selected_columns}")
#else:
#    st.error("Please select valid columns for the test.")


#------------------------------------
# <<< function to check binary data assumption holds true >>>
#------------------------------------

def check_binary_data_mcnemars_test(df, column1, column2):
    """
    Checks if the selected columns for McNemar's Test contain exactly two unique values.

    Args:
    df (DataFrame): The dataframe containing the data.
    column1 (str): The first column name.
    column2 (str): The second column name.

    Returns:
    bool: True if both columns are binary, False otherwise.
    """
    # Explanation of what Binary Data means for McNemar's Test
    with st.expander("Click for explanation"):
        st.write("""
        **Binary Data Assumption for McNemar's Test:**
        \nEach variable used in McNemar's Test should have exactly two levels (binary data), such as 'Positive/Negative' or 'Present/Absent'. 
        This requirement is crucial because McNemar's test calculations are specifically designed for 2x2 contingency tables comparing two paired samples.
        """)

    # Guidance on how to interpret the data check
    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Binary Data Check:**
        - **Exactly Two Unique Values:** If each of the selected columns contains exactly two unique values, the data structure is appropriate for McNemar's Test.
        - **More or Less than Two Unique Values:** If any column contains more or fewer than two unique values, McNemar's Test may not be suitable without modifying the data or choosing a different statistical method.
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
# <<< function to remind user of paired observations data assumption requirement >>>
#------------------------------------

def remind_about_paired_data_requirement():
    """
    Asks the user to confirm if the data used for McNemar's Test are paired, as required by the test assumptions.

    Returns:
    bool: True if the user confirms the data are paired, False otherwise.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Paired Data Assumption for McNemar's Test:**
        \nMcNemar's Test requires the data to be paired. This means the two categories being compared should come from the same subjects under different conditions or at different times.
        \nFor example, pre-treatment and post-treatment observations from the same patients, or responses on two related questions from the same survey respondents.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Paired Data Requirement:**
        - **Data Are Paired:** Suitable for McNemar's Test. This setup is crucial because McNemar's test is designed to analyze changes in responses within the same subjects.
        - **Data Are Not Paired:** McNemar's Test is not appropriate. You may need to consider alternative methods that do not require paired data.
        """)

#------------------------------------
# <<< function to remind user of independence of pairs data assumption requirement >>>
#------------------------------------
def remind_about_independence_of_pairs():
    """
    Asks the user to confirm if the pairs used for McNemar's Test are independent.

    Returns:
    bool: User's confirmation of the independence of pairs.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Independence of Pairs Assumption for McNemar's Test:**
        \nThis assumption requires that each pair is independent of others. This condition is crucial to ensure that the analysis does not include biased or correlated results.
        \nFor example, if you are studying a medical treatment's effect, each patient pair (e.g., before and after treatment measures) should not influence or be influenced by other pairs in the study.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Independence of Pairs:**
        - **Pairs Are Independent:** This is suitable for McNemar's Test. Independence here ensures that the statistical conclusions drawn are valid and generalizable.
        - **Pairs Are Not Independent:** McNemar's Test may not be suitable. Dependencies between pairs can lead to erroneous conclusions. Alternative statistical methods considering such dependencies might be required.
        """)

#------------------------------------
# <<< function to remind user of Marginal Homogeneity assumption requirement >>>
#------------------------------------

def explain_marginal_homogeneity():
    """
    Provides information about the Marginal Homogeneity assumption in McNemar's Test.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Marginal Homogeneity Assumption for McNemar's Test:**
        \nMcNemar's Test does not require the marginal totals (the sum of rows and columns in the 2x2 table) to be the same. This feature makes McNemar's Test particularly suitable for 'before-and-after' studies or any scenario where two related measures are compared on the same subjects.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Understanding Marginal Homogeneity:**
        - **Marginal Homogeneity Not Required:** This means McNemar's Test can be used even if the total number of successes or failures is different between the two conditions. The test focuses on the change from one condition to the other, particularly looking at how many observations changed from the first state to the second and vice versa.
        - **Why It Matters:** In studies where the same subjects are measured under two different conditions, it's common to see shifts in response due to the treatment or intervention, resulting in unequal margins. McNemar's Test accommodates this by comparing the discordant pairs.
        """)

    st.write("No action required. Proceed with McNemar's Test if other assumptions are met.")

#--------------------------
#user confirms their study design has accounted for the assumptions that can't be definitively checked
def check_assumptions_and_recommend_mcnemars(binary_data_check):
    """
    Asks the user to confirm assumptions based on the binary data check and context knowledge
    to determine if McNemar's Test can be used.

    Args:
    binary_data_check (bool): Result from the previous function indicating if the binary data assumption is met.

    Returns:
    bool: True if all user-confirmed assumptions are met and McNemar's Test can proceed.
    """
    st.subheader("Confirming interpretation of assumption checks")

    # If the binary data assumption is already violated, skip further checks
    if not binary_data_check:
        st.error("Binary data assumption is violated. McNemar's Test cannot proceed.")
        return False

    # Ask the user to confirm the paired data and independence of pairs assumptions
    col1, col2 = st.columns(2)
    with col1:
        paired_data_confirmation = st.selectbox(
            "Confirm if the data are paired:",
            options=["---", "Yes", "No"],
            index=0,  # Default to 'Yes'
            help="Data should be paired, meaning the same subjects are measured under two conditions."
        )

    with col2:
        independence_pairs_confirmation = st.selectbox(
            "Confirm if pairs are independent:",
            options=["---", "Yes", "No"],
            index=0,  # Default to 'Yes'
            help="Each pair's measurement must be independent of other pairs."
        )

    # Logic to determine if McNemar's Test can proceed
    if paired_data_confirmation == "Yes" and independence_pairs_confirmation == "Yes":
        st.success("All checked assumptions for McNemar's Test are met. You can proceed with the McNemar's Test.")
        return True
    elif paired_data_confirmation == "No" or independence_pairs_confirmation == "No":
        issues = []
        if paired_data_confirmation != "Yes":
            issues.append("data are not appropriately paired")
        if independence_pairs_confirmation != "Yes":
            issues.append("pairs are not independent")
        
        issues_str = " and ".join(issues)
        st.error(f"Assumptions not met because {issues_str}. Consider using another appropriate statistical test.")
        return False
    

#-----------------------------------------------
#Function to render all the above functions in the app:
def render_assumption_checks_for_mcnemars_test(df):
    #render the assumptions of the test
    display_mcnemars_test_assumptions()

    #function for user to select the categorical columns
    col1, col2 = select_two_columns_for_mcnemars_test(df)
    
    tab1, tab2, tab3, tab4 = st.tabs(['Binary data', 'Paired Data', 'Independence of Pairs', 'Marginal Homogeneity'])
    #Binary data
    with tab1:
        #Remind user to be assured of binary data
        binary_data_bool = check_binary_data_mcnemars_test(df, col1, col2)
    
    #Paired data tab
    with tab2:
        #Remind about paired data requirement
        remind_about_paired_data_requirement()
    
    #Independence of Pairs
    with tab3:
        remind_about_independence_of_pairs()
    
    #Marginal Homogeneity
    with tab4:
        #explain this concept to user
        explain_marginal_homogeneity()

    test_can_be_used_bool = check_assumptions_and_recommend_mcnemars(binary_data_bool)
    
    #return the shapiro bool value
    # if True means normal dist and if all other assumptions met, can use paired t test
    # if False, means not normal dist, recommend using Wilcoxon Signed-Rank Test
    return test_can_be_used_bool



#--------------------------
#--------------------------
#--------------------------
