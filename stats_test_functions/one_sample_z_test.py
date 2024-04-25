
import streamlit as st 
from scipy.stats import shapiro
import scipy.stats as stats
import pandas as pd 
import altair as alt
#--------------------------------------------------
#<<< Render assumptions for the one sample z test >>>
#--------------------------------------------------
def one_sample_z_test_assumptions():
    """
    Renders the assumptions for the one-sample z-test.

    Returns:
        None
    """
    dict_assumptions = {
        'Independence of Samples': "The sample data is independent, meaning the observations are not related to each other.",
        'Known Population Variance': "The population variance (σ²) is known. If not known exactly, it should be estimated from a large sample size.",
        'Normality': """The data in the sample should be approximately normally distributed. This assumption can be relaxed somewhat when sample sizes are large enough to rely on the [Central Limit Theorem](https://www.youtube.com/watch?v=YAlJCEDH2uY)"""
    }

    with st.expander("Click for One-Sample Z-Test Assumptions"):
        for key, value in dict_assumptions.items():
            st.markdown(f":red[**{key}**]:\n{value}", unsafe_allow_html=True)


#--------------------------------------------------
#<<< check assumptions for the one sample z test >>>
#--------------------------------------------------
def explain_independence_assumption_one_sample():
    """
    Provides explanations and interpretations regarding the independence of observations for the one-sample z-test.

    Returns:
    None: Displays information to help the user confirm the independence of observations.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Independence of Observations:**
        \nThe one-sample z-test requires that the observations within the sample are independent of each other. This means that the outcome of one observation should not influence the outcome of another observation within the same sample.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Independence:**
        - **Data Are Independent:** Suitable for the one-sample z-test. This setup is crucial because the test assumes no relationship between the observations within the sample.
        - **Data Are Not Independent:** The one-sample z-test may not be appropriate if there is any linkage or dependency between observations. In such cases, other statistical methods that account for dependent data should be considered.
        """)


#--------------------------------------------------
#<<< function to check assumptions or remind user to be assured where these cannot be checked >>>
#--------------------------------------------------
#Known Population Variances:

def explain_known_population_variance():
    """
    Provides explanations and interpretations regarding the assumption of known population variance for the one-sample z-test.

    Returns:
    None: Displays information to help the user confirm the known population variance.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Known Population Variance:**
        \nThe one-sample z-test requires that the population variance is known. This assumption is crucial because the standard deviation of the population, used in calculating the z-score, relies on this information to assess the significance of the observed sample mean relative to the population mean.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Known Population Variance:**
        - **Variance Is Known:** Suitable for the one-sample z-test. Having a precise variance value ensures that the z-score calculation and the consequent p-values are accurate.
        - **Variance Is Not Known:** The one-sample z-test may not be suitable. Without a known population variance, estimation introduces uncertainty that could lead to incorrect conclusions. In such cases, a one-sample t-test, which does not require the population variance to be known and instead uses the sample variance, may be more appropriate.
        """)

#--------------------------------------------------
#<<< check normality assumption for the one sample z test >>>
#--------------------------------------------------
def check_normality_one_sample_z_test(df, sample_column):
    """
    Checks for normality in a single sample for the one-sample z-test.
    """
    
    with st.expander('Click for explanation'):
        st.subheader('Explanation:')
        st.write('The Q-Q (Quantile-Quantile) plot compares the quantiles of the variable data against the quantiles of a theoretical normal distribution to assess normality. This is crucial for determining if the one-sample z-test is appropriate, as it typically assumes that the sample distribution approximates normality, especially as sample sizes increase.')
        st.write(":blue[**Blue Points:**] Each point represents a quantile in your data compared to the corresponding quantile of the theoretical normal distribution.")
        st.write(":red[**Red line:**] This line represents what the data points would follow if the sample distribution were perfectly normal.")

    with st.expander('Click for interpretation'):
        st.subheader('Interpretation:')
        st.write("**If the Points Lie on the Red Line:** This suggests the data are well-modeled by a normal distribution, affirming the suitability of the z-test.")
        st.write("**If the Points Deviate from the Red Line:** Significant deviations indicate that the data may not be normally distributed, which could undermine the assumptions of the z-test.")

    
    data = df[sample_column]
    st.write(f"***Normality Check for {sample_column}:***")
    # Shapiro-Wilk Test
    stat, p_value = shapiro(data)

    with st.expander(f"Click for Shapiro-Wilk Test results for {sample_column}"):
        st.write(f"Shapiro-Wilk test statistic: {stat:.4f}, P-value: {p_value:.4f}")
        if p_value > 0.05:
            st.write("Data appears to be normally distributed. While normality is less critical for the z-test due to the Central Limit Theorem, this finding supports the robustness of the analysis.")
        else:
            st.write("Data does not appear to be normally distributed. For smaller sample sizes, this might affect the reliability of the z-test.")

    # Q-Q Plot
    with st.expander(f"Click for Q-Q Plot for {sample_column}"):
        qq = stats.probplot(data, dist="norm")
        qq_data = pd.DataFrame({
            'Theoretical Quantiles': [pt[0] for pt in qq[0]],
            'Ordered Values': [pt[1] for pt in qq[0]]
        })
        qq_plot = alt.Chart(qq_data).mark_circle(size=60, opacity=0.5).encode(
            x=alt.X('Theoretical Quantiles', title='Theoretical Quantiles'),
            y=alt.Y('Ordered Values', title='Sample Quantiles')
        ).properties(
            title=f'Q-Q plot for {sample_column}'
        )
        line = alt.Chart(pd.DataFrame({
            'Theoretical Quantiles': qq_data['Theoretical Quantiles'],
            'Ordered Values': qq_data['Theoretical Quantiles']
        })).mark_line(color='red').encode(
            x='Theoretical Quantiles',
            y='Ordered Values'
        )
        st.altair_chart(qq_plot + line, use_container_width=True)
    
    return p_value

# -------------------------------
# Function to interpret assumption results

def confirm_one_sample_z_test_assumptions(normality_p_value):
    """
    Renders select boxes for the user to manually confirm the assumptions required for the one-sample z-test,
    considering the result from the normality check.
    
    Args:
    normality_p_value (float): p-value from the normality check function for the sample.

    Returns:
    bool: True if all manually checked assumptions are confirmed, False otherwise.
    """
    st.subheader("Confirming remaining assumptions for the One-Sample z-test")

    # Check if the p-value from normality checks is significant, suggesting non-normal distribution
    if normality_p_value <= 0.05:
        st.error("Normality assumption is not met based on the Shapiro-Wilk test. Consider using a non-parametric test or transform the data.")
        return False

    # Initialize placeholders
    default_option = "---"
    options = [default_option, "Yes", "No"]

    col1, col2, col3 = st.columns(3)

    with col1:
        independence_confirmation = st.selectbox(
            "Confirm if the observations within the sample are independent:",
            options=options,
            help="Observations within the sample should be independent of each other."
        )

    with col2:
        known_variance_confirmation = st.selectbox(
            "Confirm if the population variance is known:",
            options=options,
            help="For the one-sample z-test, it is assumed that the population variance is known."
        )

    with col3:
        qq_plot_confirmation = st.selectbox(
            "Having reviewed the Q-Q plot, do the points approximately follow the line?",
            options=["---", "Yes", "No"],
            index=0,  # Default to '---'
            help = "Review the Q-Q plot displayed: If the data points closely follow the theoretical line (usually displayed in red), it suggests that the sample distribution closely approximates a normal distribution, which supports the validity of the z-test under the assumption of normality. If the points deviate significantly from the line, especially in the tails, the data may not be normally distributed, which could affect the reliability of the z-test results."
        )

    # Check if all necessary confirmations are 'Yes'
    if independence_confirmation == default_option or known_variance_confirmation == default_option or qq_plot_confirmation == default_option:
        return None  # Wait until all selections are made
    elif independence_confirmation == "Yes" and known_variance_confirmation == "Yes" and qq_plot_confirmation == "Yes":
        st.success("All necessary assumptions for the One-Sample z-test are confirmed.")
        return True
    else:
        issues = []
        if independence_confirmation == "No":
            issues.append("\n - the observations within the sample are not independent")
        if known_variance_confirmation == "No":
            issues.append("\n - the population variance is not known")
        if qq_plot_confirmation == "No":
            issues.append("\n - the distribution does not appear Normal from the Q-Q plot")

        issues_str = ", ".join(issues)
        recommendation_message = f"""Assumptions not met because: {issues_str}.
        \n Consider using another statistical test such as the t-test if variance is unknown or non-parametric tests (such as the **Single sample wilcoxon signed-rank test**) for non-normal distributions."""

        st.error(recommendation_message)
        return False

#-----------------------------------

def render_assumption_checks_for_independent_z_test(df):
    one_sample_z_test_assumptions()

    #function for user to select samples
    sample_column = st.selectbox(
        label='Select the column containing the sample data',
        options=list(df.columns)
    )
    #if sample_1_col == None or sample_2_col == None:
    #    st.write('Select the columns for sample 1 and sample 2 above.')
    #    st.stop()

    tab1, tab2, tab3 = st.tabs(['Indpendence of sample observations', 'Known Population Variances', 'Normal dist check'])
    
    with tab1:
        #Independence of Samples:
        explain_independence_assumption_one_sample() #remind user
    
    with tab2:
        #Known Population Variances
        explain_known_population_variance() #remind user
    
    with tab3:
        #Normality
        try:
            normality_check_p_values = check_normality_one_sample_z_test(df, sample_column)
        except KeyError:
            st.write('Select sample names above for the check to proceed.')
            st.stop()
    #add function to interpret user input (if applicable) and output bools from prior assumptions checks
    test_bool_result = confirm_one_sample_z_test_assumptions(normality_check_p_values)
    #return a single bool if all checks are True from this render_assumption_checks_for_independent_z_test function

    return test_bool_result
