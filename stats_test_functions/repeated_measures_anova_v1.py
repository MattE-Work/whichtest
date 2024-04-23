import streamlit as st
import pandas as pd
import pingouin as pg

# Import other necessary tools or references for user interactions
# from utils import user_inputs  # Assuming some utilities for user interactions

#------------------------------------
# <<< Function to render assumptions >>>
#------------------------------------

def repeated_measures_anova_assumptions():
    dict_assumptions_rm_anova = {
        'Sphericity': "Equal variances of the differences between all combinations of groups (conditions). This can be tested using Mauchly’s test.",
        'Normality of Residuals': "Residuals from the model should be normally distributed, which can be checked with a Q-Q plot or Shapiro-Wilk test for each group.",
        'Independence': "Observations within each subject/group combination should be independent, which is generally a given in experimental designs."
    }

    with st.expander("Click for this test's assumptions"):
        for key, value in dict_assumptions_rm_anova.items():
            st.write(f":red[**{key}**:]\n{value}")    

#------------------------------------
# <<< Function to select columns >>>
#------------------------------------

def select_columns_for_wide_format_anova(df):
    """
    Renders a user interface to select the subject column and multiple condition columns from a wide-format dataframe.

    Args:
    df (DataFrame): The dataframe from which columns will be selected.

    Returns:
    dict: A dictionary with the selected subject_column and a list of condition_columns.
    """
    st.write("Please select the appropriate columns from your dataset for the analysis:")

    #col1, col2 = st.columns(2)
    #with col1:
    #    # Select subject column
    #    subject_column = st.selectbox(
    #        "Select the Subject Column",
    #        options=df.columns,
    #        help="This should be the column that uniquely identifies each subject or participant in the study."
    #    )

    #with col2:
    # Allow the user to select multiple columns for the within-subject factors
    #st.write("Select the columns that represent different conditions or time points:")
    condition_columns = st.multiselect(
        #"Select Condition Columns",
        "Select the columns that represent different conditions or time points (**:red[Caution: select these in order]**, e.g. baseline, then follow_up_1, etc.):",
        options=[col for col in df.columns],
        help="These columns should represent different measurement conditions or time points for the within-subjects factors."
    )

    #return {'subject_column': subject_column, 'condition_columns': condition_columns}
    return condition_columns

    # Example usage in a Streamlit app
    # df = pd.DataFrame({
    #     'SubjectID': [1, 1, 2, 2],
    #     'Baseline': [20, 20, 21, 21],
    #     'Follow_Up_1': [22, 22, 23, 23],
    #     'Follow_Up_2': [24, 24, 25, 25]
    # })
    # selections = select_columns_for_wide_format_anova(df)
    # print(selections)


#------------------------------------
# <<< Function to check sphericity assumption >>>
#------------------------------------

def check_sphericity(df_wide):
    """
    Performs the sphericity test using Pingouin on the wide-format data.
    
    Args:
    df_wide (DataFrame): DataFrame in wide format where each column represents a different condition 
                         and each row represents a subject.
                         
    Returns:
    bool: True if sphericity is assumed (p > 0.05), False otherwise.
    """
    # Explanation of what Sphericity is
    with st.expander("What is Sphericity?"):
        st.write("""
        **Sphericity** is an assumption underlying certain statistical tests, including Repeated Measures ANOVA. It requires that the variances of the differences between all combinations of related group (condition) means are equal. This assumption is crucial because violations can inflate Type I error rates, leading to incorrect conclusions about the effects being tested.
        """)
    
    # Guidance on how to interpret the results from the sphericity test
    with st.expander("How to Interpret Sphericity Test Results"):
        st.write("""
        **Mauchly's Test** is commonly used to assess sphericity. The test provides a p-value:
        - **P-value > 0.05**: This suggests that the sphericity assumption holds. No corrections are necessary for further ANOVA tests.
        - **P-value ≤ 0.05**: This indicates a violation of the sphericity assumption. Corrections like Greenhouse-Geisser or Huynh-Feldt should be considered to adjust the degrees of freedom for the F-tests, which can help control Type I error rates.
        """)

    try:
        # Calculate the sphericity test
        spher, W, chisq, dof, p_value = pg.sphericity(df_wide)
        
        # Display results in Streamlit
        with st.expander("Sphericity Test Results"):
            st.write(f"Sphericity test result (Mauchly's W): {W:.4f}, Chi-square: {chisq:.4f}, Degrees of freedom: {dof}, P-value: {p_value:.4f}")
            if p_value > 0.05:
                st.write("Sphericity is assumed (p > 0.05). No corrections needed.")
                return True
            else:
                st.write("Sphericity is not assumed (p ≤ 0.05). Consider using corrections such as Greenhouse-Geisser or Huynh-Feldt.")
                return False
    except Exception as e:
        st.error(f"Error in calculating sphericity: {str(e)}")
        return False

#------------------------------------
# <<< Function to check normality of residuals assumption >>>
#------------------------------------

def check_normality_of_residuals(df_wide):
    """
    Checks the normality of residuals for each condition in a repeated measures setup using the Shapiro-Wilk test.

    Args:
    df_wide (DataFrame): DataFrame in wide format where each column represents a different condition and each row represents a subject.

    Returns:
    dict: A dictionary with condition names as keys and a tuple of (Shapiro-Wilk statistic, p-value, normality assumption boolean) as values.
    """
    # Explanation of what the test is and why it's important
    with st.expander("What is the Normality of Residuals?"):
        st.write("""
        **Normality of Residuals** refers to the assumption that the residuals (differences between observed values and group means) 
        from an analysis should be normally distributed. This assumption is crucial for the validity of parametric tests, 
        including Repeated Measures ANOVA, because these tests assume the data follow a normal distribution to correctly 
        calculate significance and confidence intervals.
        """)

    # Guidance on how to interpret the results of the Shapiro-Wilk test
    with st.expander("How to Interpret the Results"):
        st.write("""
        The Shapiro-Wilk test assesses the normality of the residuals:
        - **W statistic**: A value close to 1 indicates that the data are well modeled by a normal distribution.
        - **P-value**: Determines whether we reject the assumption of normality.
          - A **p-value greater than 0.05** suggests that the residuals can be considered normally distributed, and the normality assumption holds.
          - A **p-value less than or equal to 0.05** suggests that the residuals are not normally distributed, which might invalidate some conclusions drawn from parametric tests that assume normality.
        """)

    normality_results = {}
    with st.expander("Normality Check for Residuals"):
        for condition in df_wide.columns:
            st.subheader(f"***{condition}***")
            # Calculate the residuals for each condition
            residuals = df_wide[condition] - df_wide[condition].mean()
            # Perform the Shapiro-Wilk test on the residuals
            shapiro_results = pg.normality(residuals)
            W = shapiro_results['W'][0]
            p_value = shapiro_results['pval'][0]
            normality_assumed = p_value > 0.05

            # Store the results
            normality_results[condition] = (W, p_value, normality_assumed)

            # Output the results to Streamlit
            st.write(f"**{condition}** - Shapiro-Wilk Test: W = {W:.4f}, p-value = {p_value:.4f}")
            if normality_assumed:
                st.write(f"The residuals for **{condition}** are normally distributed (p > 0.05).")
            else:
                st.write(f"The residuals for **{condition}** are not normally distributed (p ≤ 0.05). Consider using non-parametric methods or transforming the data.")

    return normality_results



#------------------------------------
# <<< Main function to render all assumption checks >>>
#------------------------------------

# Main function to render all checks
def render_assumption_checks_for_repeated_measures_anova(df):
    """
    Function to render assumption checks and t-test for the repeated measures anova test in a Streamlit app.
    """

    #render assumptions to user:
    repeated_measures_anova_assumptions()

    #select the measurement columns
    col_labels_containing_measurements = select_columns_for_wide_format_anova(df)

    #render the assumptions in separate tabs
    tab1, tab2 = st.tabs(['Sphericity check', 'Normality of residuals check'])
    
    with tab1:
        assumption_check_sphericity = check_sphericity(df)

    with tab2:
        normality_results = check_normality_of_residuals(df)

    #interpret_test_results(normality_check_p_values[0], normality_check_p_values[1], equality_of_variances_check_p_value[0], alpha=0.05)

    #return assumption_check_sphericity, normality_results
    # Interpret results and provide recommendations
    if assumption_check_sphericity and all(normality_results.values()):
        st.success("All assumptions for Repeated Measures ANOVA are met. You can proceed with the analysis using Repeated Measures ANOVA.")
        return True

    else:
        issues = []
        if not assumption_check_sphericity:
            issues.append("sphericity is not assumed; consider using Greenhouse-Geisser or Huynh-Feldt corrections (**not current included in this tool**).")
        if not all(normality_results.values()):
            issues.append("not all residuals are normally distributed; consider transforming the data **(not current included in this tool)** or using non-parametric methods.")

        st.error("One or more assumptions are not met: " + " and ".join(issues))
        st.write("It is recommended to address these issues or consider alternative methods such as the non-parametric **:red[Friedman test]** if appropriate corrections cannot be applied.")

        return False

    

