from scipy.stats import ttest_ind, levene, shapiro
import numpy as np
import altair as alt
import streamlit as st
import pandas as pd
import scipy.stats as stats


#import other functions from files
#from stats_test_functions import stats_tests as stat_tests
from functions import user_inputs



#functions to check assumptions:
def independent_t_test_assumptions():
    dict_assumptions = {
        'Independence of Samples': "The two groups are independent, meaning the observations in one group are not related to the observations in the other group.",
        'Equal Variances': "The variances of the two groups should be approximately equal. This assumption can be tested using Levene’s test or an F-test for equal variances.",
        'Normality': "The data in both groups should be approximately normally distributed. This is particularly important when sample sizes are small.",
    }
    return dict_assumptions


# Function to perform Levene's Test for equality of variances
def check_homoscedasticity(df, sample_1, sample_2):
    """
    Performs Levene's test for equality of variances between two samples.
    """
    equality_of_variances_check_p_value = []

    data1 = df[sample_1]
    data2 = df[sample_2]
    stat, p_value = levene(data1, data2)
    
    equality_of_variances_check_p_value.append(p_value) #store p_value for later decision making

    with st.expander("Click for explanation of Levene's Test"):
        st.write("""
        **Levene's Test** checks if two or more groups have equal variances. Equal variances across groups is an assumption of the independent t-test when comparing means.
        - **Statistic**: The test statistic value.
        - **P-value**: If the p-value is less than 0.05, we reject the hypothesis of equal variances.
        """)

    with st.expander("Click for interpretation of Levene's Test results"):
        st.write(f"Levene's test statistic: {stat:.4f}, P-value: {p_value:.4f}")
        if p_value > 0.05:
            st.write("The variances are equal. Assumption satisfied for the independent t-test.")
        else:
            st.write("The variances are not equal. Consider using a test that does not assume equal variances, such as Welch's t-test.")
    
    return equality_of_variances_check_p_value



# Function to check for normality using Q-Q plots and Shapiro-Wilk Test
def check_normality(df, sample_1, sample_2):
    """
    Checks for normality in each of two independent samples.
    """
    normality_check_p_values = []

    for sample in [sample_1, sample_2]:
        data = df[sample]
        st.write(f"***Normality Check for {sample}:***")
        # Shapiro-Wilk Test
        stat, p_value = shapiro(data)
        normality_check_p_values.append(p_value)  # Store the p-value for later decision making

        with st.expander(f"Click for Shapiro-Wilk Test results for {sample}"):
            st.write(f"Shapiro-Wilk test statistic: {stat:.4f}, P-value: {p_value:.4f}")
            if p_value > 0.05:
                st.write("Data appears to be normally distributed. Assumption satisfied for the independent t-test.")
            else:
                st.write("Data does not appear to be normally distributed. Consider using a non-parametric test if this is the case for both samples.")

        # Q-Q Plot
        with st.expander(f"Click for Q-Q Plot for {sample}"):
            qq = stats.probplot(data, dist="norm")
            qq_data = pd.DataFrame({
                'Theoretical Quantiles': [pt[0] for pt in qq[0]],
                'Ordered Values': [pt[1] for pt in qq[0]]
            })
            qq_plot = alt.Chart(qq_data).mark_circle(size=60, opacity=0.5).encode(
                x=alt.X('Theoretical Quantiles', title='Theoretical Quantiles'),
                y=alt.Y('Ordered Values', title=f'Sample Quantiles for {sample}')
            ).properties(
                title=f'Q-Q plot for {sample}'
            )
            line = alt.Chart(pd.DataFrame({
                'Theoretical Quantiles': qq_data['Theoretical Quantiles'],
                'Ordered Values': qq_data['Theoretical Quantiles']
            })).mark_line(color='red').encode(
                x='Theoretical Quantiles',
                y='Ordered Values'
            )
            st.altair_chart(qq_plot + line, use_container_width=True)
    return normality_check_p_values


def interpret_test_results(p_value_normality1, p_value_normality2, p_value_homoscedasticity, alpha=0.05):
    """
    Interprets the results of normality and homoscedasticity tests to determine the appropriateness of using the independent t-test.

    Args:
    p_value_normality1 (float): P-value from the Shapiro-Wilk test for the first sample.
    p_value_normality2 (float): P-value from the Shapiro-Wilk test for the second sample.
    p_value_homoscedasticity (float): P-value from Levene's test for equal variances.
    alpha (float): Significance level, default is 0.05.

    Returns:
    tuple: A boolean indicating if the independent t-test assumptions are met and a string with the recommendation.
    """
    test_can_be_run = True
    messages = []

    # Check normality results
    if p_value_normality1 < alpha or p_value_normality2 < alpha:
        messages.append("normality is not assumed as one or both samples do not follow a normal distribution.")
        test_can_be_run = False

    # Check homoscedasticity results
    if p_value_homoscedasticity < alpha:
        messages.append("equal variances are not assumed as the variances between groups are significantly different.")
        test_can_be_run = False

    # Build the recommendation message
    if test_can_be_run:
        recommendation = "All assumptions for the independent t-test are met. You can **proceed with the Independent t-Test**."
    else:
        alternative_tests = []
        if messages:
            joined_message = " and ".join(messages)
            recommendation = f"Assumptions for the independent t-test are not met because {joined_message}."
            if "normality" in joined_message:
                alternative_tests.append("**Mann-Whitney U test**")
            if "equal variances" in joined_message:
                alternative_tests.append("**Welch's t-test**")
            alternative_tests_str = " or ".join(alternative_tests)
            recommendation += f" Consider using {alternative_tests_str} as alternative tests."
        else:
            recommendation = "Check the data and assumptions carefully before proceeding."

    # Display recommendation in Streamlit
    st.write(recommendation)
    return test_can_be_run, recommendation


# Function to perform the independent t-test
def independent_t_test(df, sample_1, sample_2):
    """
    Performs the independent t-test between two samples.
    """
    data1 = df[sample_1]
    data2 = df[sample_2]
    stat, p_value = ttest_ind(data1, data2, equal_var=True)

    st.write(f"Independent t-Test Results:")
    st.write(f"Test Statistic: {stat:.4f}, P-value: {p_value:.4f}")
    if p_value < 0.05:
        st.write("There is a statistically significant difference between the two groups.")
    else:
        st.write("There is no statistically significant difference between the two groups.")


# Main function to render all checks
def render_assumption_checks_for_independent_t_test(df):
    """
    Function to render assumption checks and t-test for the independent t-test in a Streamlit app.
    """

    dict_independent_t_assumptions = independent_t_test_assumptions()

    st.subheader('...for the independent t test')
    with st.expander(label='Click to review required assumptions for this test'):
        for assumption, value in dict_independent_t_assumptions.items():
            st.write(f":red[**{assumption}**:]\n{value}")

    sample_1_col, sample_2_col = user_inputs.select_sample_columns(df)  # Assuming user_inputs.select_sample_columns is defined elsewhere
    tab1, tab2 = st.tabs(['Normality Checks', 'Homoscedasticity Check'])
    
    with tab1:
        normality_check_p_values = check_normality(df, sample_1_col, sample_2_col)
    
    with tab2:
        equality_of_variances_check_p_value = check_homoscedasticity(df, sample_1_col, sample_2_col)
    
    test_can_be_run, recommendation = interpret_test_results(normality_check_p_values[0], normality_check_p_values[1], equality_of_variances_check_p_value[0], alpha=0.05)
    
    #with tab3:
    #    independent_t_test(df, sample_1_col, sample_2_col)
    return test_can_be_run
