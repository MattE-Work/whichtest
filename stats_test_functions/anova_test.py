
import streamlit as st
import scipy.stats as stats


#------------------------------------
# <<< Function to render assumptions >>>
#------------------------------------

def display_anova_assumptions():
    dict_anova_assumptions = {
    "Independence": "Each group's observations are collected independently of the others.",
    "Normality": "The data in each group should follow a normal distribution. This can typically be checked using a Shapiro-Wilk test.",
    "Equal Variances": "The variances of the groups should be similar. This can be checked using Levene's Test for equality of variances.",
    }

    with st.expander("Click for this test's assumptions"):
        for key, value in dict_anova_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")    


#------------------------------------
# <<< Function to select columns >>>
#------------------------------------

def select_columns_for_anova_test(df):
    """
    Renders select boxes for the user to choose columns from a dataframe.

    Args:
    df (DataFrame): The dataframe from which columns will be selected.

    Returns:
    dict: Dictionary with selected column names or None if "---" is selected.
    """
    st.write("Please select the appropriate columns for your analysis:")
    
    # Initialize placeholders
    default_option = "---"
    
    # Get column names and include the placeholder as the first option
    options = [default_option] + list(df.columns)
    
    # Render select boxes for column selection    
    list_df_col_names = list(df.columns)
    list_options = ["---"]
    for item in list_df_col_names:
        list_options.append(item)

    col1, col2 = st.columns(2)
    with col1:
        group_column = st.selectbox(
            "Select the Group Column",
            options=list_options,
            help="Select the column that categorizes the data into different groups for the ANOVA test."
        )
    
    with col2:    
        value_column = st.selectbox(
            "Select the Value Column",
            options=list_options,
            help="Select the column that contains the numerical data on which the ANOVA test will be performed."
        )

    return group_column, value_column

#------------------------------------
# <<< Function to check normality assumption >>>
#------------------------------------

def check_normality(df, group_column, value_column):
    """
    Checks the normality of each group's data using the Shapiro-Wilk test.

    Args:
    df (DataFrame): The dataframe containing the data.
    group_column (str): The column in df that denotes the group.
    value_column (str): The column in df that contains the values to be tested for normality.

    Returns:
    dict: A dictionary of the groups and their Shapiro-Wilk test results (statistic and p-value).
    """
    unique_groups = df[group_column].unique()
    normality_results = {}

    # Explanation of what Normality Test is
    with st.expander("What is a Normality Test?"):
        st.write("""
        **Normality tests** are used to determine if a dataset is well-modeled by a normal distribution. Among these tests, the **Shapiro-Wilk Test** is particularly popular for small to moderately sized samples. It assesses how likely it is for a random variable underlying the data set to be normally distributed.
        """)

    # Guidance on how to interpret the results from the normality test
    with st.expander("How to Interpret Normality Test Results"):
        st.write("""
        **Interpreting the Shapiro-Wilk Test:**
        - **P-value > 0.05**: This suggests that the data can be considered normally distributed under the assumption of normality. There is no indication of significant deviation from normality.
        - **P-value ≤ 0.05**: This indicates that the data do not follow a normal distribution. Depending on the context and the severity of the deviation, transformations or non-parametric methods may be recommended.
        """)

    # Displaying the normality check results
    with st.expander("Normality Check Results"):
        for group in unique_groups:
            group_data = df[df[group_column] == group][value_column]
            stat, p_value = stats.shapiro(group_data)
            normality_results[group] = (stat, p_value)
            st.write(f"**{group}**: Shapiro-Wilk Test Statistic={stat:.4f}, p-value={p_value:.4f}")
    
    return normality_results


#------------------------------------
# <<< Function to check Homogeneity of Variances assumption >>>
#------------------------------------

def check_homogeneity(df, group_column, value_column):
    """
    Checks the homogeneity of variances across different groups using Levene's test.

    Args:
    df (DataFrame): The dataframe containing the data.
    group_column (str): The column in df that denotes the group.
    value_column (str): The column in df that contains the values to be tested for homogeneity.

    Returns:
    tuple: A tuple containing the Levene's test statistic and the p-value.
    """
    group_data = [df[df[group_column] == group][value_column] for group in df[group_column].unique()]

    # Explanation of what Homogeneity of Variances is
    with st.expander("What is Homogeneity of Variances?"):
        st.write("""
        **Homogeneity of variances (Homoscedasticity)** is an assumption for ANOVA that requires the variances within each of the groups being compared to be approximately equal. This assumption is checked because significant differences in variances can affect the validity of the ANOVA results. **Levene's test** is one of the most common methods used to assess this assumption.
        """)

    # Guidance on how to interpret the results from the homogeneity test
    with st.expander("How to Interpret Homogeneity Test Results"):
        st.write("""
        **Interpreting Levene's Test:**
        - **P-value > 0.05**: This suggests that the variances are equal across the groups. The assumption of homogeneity is met, and you can proceed with ANOVA without adjustments.
        - **P-value ≤ 0.05**: This indicates that at least one group's variance significantly differs from the others. In this case, you should consider using alternative methods such as Welch's ANOVA, which does not assume equal variances.
        """)

    # Performing Levene's test and displaying the results
    stat, p_value = stats.levene(*group_data)
    with st.expander("Homogeneity of Variances Check Results"):
        st.write(f"Levene's Test Statistic: {stat:.4f}, P-value: {p_value:.4f}")
    
    return stat, p_value

#------------------------------------
# <<< Main Function to Render Checks >>>
#------------------------------------

def render_anova_checks(df, group_column, value_column):
    display_anova_assumptions()

    #render the assumptions in separate tabs
    tab1, tab2 = st.tabs(['Homogeneity (equal) variance check', 'Normality check'])
    
    with tab1:
        stat, p_value = check_homogeneity(df, group_column, value_column)

    with tab2:
        normality_results = check_normality(df, group_column, value_column)
   
    if all(p > 0.05 for _, p in normality_results.values()) and p_value > 0.05:
        st.success("All assumptions for one-way ANOVA are met. You can proceed with the ANOVA test.")
        return True
    else:
        st.error("One or more assumptions are not met. Consider transforming the data (not in scope in this tool currently), applying corrections (out of scope of this tool currently), or using the **Kruskal-Wallis H Test** non-parametric alternative.")
        return False
