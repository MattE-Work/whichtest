from scipy.stats import ttest_ind, levene, shapiro
import numpy as np
import altair as alt
import streamlit as st
import pandas as pd
import scipy.stats as stats


#import other functions from files
#from stats_test_functions import stats_tests as stat_tests
from functions import user_inputs


#--------------------------------------------------
#<<< Render assumptions for the independent z test >>>
#--------------------------------------------------
#functions to check assumptions:
def independent_z_test_assumptions():
    dict_assumptions = {
        'Independence of Samples': "The two groups are independent, meaning the observations in one group are not related to the observations in the other group.",
        'Known Population Variances': "The population variances (\u03C3\u00B2) of the two groups must be known. If not known exactly, they should be estimated from large sample sizes.",
        'Normality': "The data in both groups should be approximately normally distributed. This assumption can be relaxed somewhat when sample sizes are large enough to rely on the Central Limit Theorem."
    }

    with st.expander("Click for Independent Z-Test Assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")



#--------------------------------------------------
#<<< function to check assumptions or remind user to be assured where these cannot be checked >>>
#--------------------------------------------------
#Independence of Samples

def explain_independence_assumption():
    """
    Asks the user to confirm the independence of samples for the independent z-test.

    Returns:
    None: Provides explanations and interpretations for the user to confirm independence of samples.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Independence of Samples:**
        \nThe independent z-test requires that the two groups being compared are independent of each other. This means that the selection or outcome in one group should not influence the selection or outcome in the other group.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Independence:**
        - **Data Are Independent:** Suitable for the independent z-test. This setup is crucial because the test assumes no relationship between the members of different groups.
        - **Data Are Not Independent:** The independent z-test may not be appropriate if there is any linkage or pairing between the groups’ members. In such cases, other tests designed for paired or matched data should be considered.
        """)

#--------------------------------------------------
#<<< function to check assumptions or remind user to be assured where these cannot be checked >>>
#--------------------------------------------------
#Known Population Variances:

def explain_known_population_variances():
    """
    Asks the user to confirm that the population variances are known for conducting the independent z-test.

    Returns:
    bool: True if the user confirms that population variances are known, False otherwise.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Known Population Variances:**
        \nThe independent z-test requires that the population variances of the groups being compared are known. This is because the standard deviation of the groups, used in calculating the z-score, relies on this information to accurately assess the significance of the difference between group means.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Known Population Variances:**
        - **Variances Are Known:** Suitable for the independent z-test. Having precise variance values ensures that the z-score calculation and the consequent p-values are accurate.
        - **Variances Are Not Known:** The independent z-test may not be suitable. Without known population variances, estimations would introduce uncertainty that could lead to incorrect conclusions. In such cases, an independent t-test, which estimates variances from the sample data, may be more appropriate.
        """)



# -------------------------------
# Function to check for normality 
def check_normality_z_test(df, sample_1, sample_2):
    """
    Checks for normality in each of two independent samples for the independent z-test.
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
                st.write("Data appears to be normally distributed. While normality is less critical for the z-test due to large sample sizes, this finding supports the robustness of the analysis.")
            else:
                st.write("Data does not appear to be normally distributed. With smaller sample sizes, this might affect the reliability of the z-test.")

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



# -------------------------------
# Function to interpret assumption results
def confirm_independent_z_test_assumptions(normality_p_values):
    """
    Renders select boxes for the user to manually confirm the assumptions required for the independent z-test,
    considering the results from the normality checks.
    
    Args:
    normality_p_values (list): List of p-values from the normality check functions for each sample.

    Returns:
    bool: True if all manually checked assumptions are confirmed, False otherwise.
    """
    st.subheader("Confirming remaining assumptions for the Independent z-test")

    # Check if any p-values from normality checks are significant, suggesting non-normal distributions
    if any(p <= 0.05 for p in normality_p_values):
        st.error("Normality assumption is not met based on the Shapiro-Wilk test. Consider using a non-parametric test (such as the **Mann-Whitney U test**) or transform the data.")
        return False

    # Initialize placeholders
    default_option = "---"
    options = [default_option, "Yes", "No"]

    col1, col2, col3 = st.columns(3)

    with col1:
        independence_confirmation = st.selectbox(
            "Confirm if the samples are independent:",
            options=options,
            help="The two groups being compared must be independent of each other."
        )

    with col2:
        known_variance_confirmation = st.selectbox(
            "Confirm if the population variances are known:",
            options=options,
            help="For the z-test, it is assumed that the population variances are known."
        )

    with col3:
        qq_plot_confirmation = st.selectbox(
            "Confirm if the points in the Q-Q plot closely follow the line:",
            options=options,
            help="A Q-Q plot can show whether the data are normally distributed, which supports the robustness of the z-test."
        )

    # Check if all necessary confirmations are 'Yes'
    if independence_confirmation == default_option or known_variance_confirmation == default_option or qq_plot_confirmation == default_option:
        return None  # Wait until all selections are made
    else:
        issues = []
        if independence_confirmation == "No":
            issues.append("\n- independence of samples (consider a **paired t-test** if the samples are paired)")
        if known_variance_confirmation == "No":
            issues.append("\n- known population variances (consider using **Welch's t-test** if variances are unequal)")
        if qq_plot_confirmation == "No":
            issues.append("\n- normal distribution of data (consider using the **Mann-Whitney U** Test for non-normal data)")
        
        if issues:
            issues_str = "; ".join(issues)
            recommendation_message = f"The follow assumptions were  not met: {issues_str}. Consider using the suggested alternatives."
            st.error(recommendation_message)
            return False
        else:
            st.success("All necessary assumptions for the independent z-test are confirmed.")
            return True

    # Check if all necessary confirmations are 'Yes'
    #if independence_confirmation == default_option or known_variance_confirmation == default_option or qq_plot_confirmation == default_option:
    #    return None
    #elif independence_confirmation == "Yes" and known_variance_confirmation == "Yes" and qq_plot_confirmation == "Yes":
    #    st.success("All necessary assumptions for the Independent z-test are confirmed.")
    #    return True
    #else:
    #    st.error("One or more critical assumptions are not met. Consider revising the data or using a different statistical method.")
    #    return False


#--------------------------------
#function to render all checks (bring all above together)
# Main function to render all checks
def render_assumption_checks_for_independent_z_test(df):
    independent_z_test_assumptions()

    #function for user to select samples
    sample_1_col, sample_2_col = user_inputs.select_sample_columns(df)
    #if sample_1_col == None or sample_2_col == None:
    #    st.write('Select the columns for sample 1 and sample 2 above.')
    #    st.stop()

    tab1, tab2, tab3 = st.tabs(['Indpendence of samples', 'Known Population Variances', 'Normal dist check'])
    
    with tab1:
        #Independence of Samples:
        explain_independence_assumption() #remind user
    
    with tab2:
        #Known Population Variances
        explain_known_population_variances() #remind user
    
    with tab3:
        #Normality
        try:
            normality_check_p_values = check_normality_z_test(df, sample_1_col, sample_2_col)
        except KeyError:
            st.write('Select sample names above for the check to proceed.')
            st.stop()
    #add function to interpret user input (if applicable) and output bools from prior assumptions checks
    test_bool_result = confirm_independent_z_test_assumptions(normality_check_p_values)
    #return a single bool if all checks are True from this render_assumption_checks_for_independent_z_test function

    return test_bool_result

    #return the shapiro bool value
    # if True means normal dist and if all other assumptions met, can use paired t test
    # if False, means not normal dist, recommend using Wilcoxon Signed-Rank Test
    