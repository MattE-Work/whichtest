import streamlit as st
import scipy.stats as stats
import pandas as pd
import altair as alt

#import other functions from files
from stats_test_functions import stats_tests as stat_tests
from functions import user_inputs


#--------------------------
# Paired z test
#--------------------------
#functions to check assumptions:
def paired_z_test_assumptions():
    dict_assumptions = {
        'Dependent Samples': "The samples must be paired or matched, which is fundamental for a Paired z-Test. This typically involves before-and-after measurements on the same subjects, or measurements on matched pairs such as siblings or twins.",
        'Known Population Variances': "For the Paired z-Test, it's assumed that the population variances are known. This is less common in practice and often requires a large sample size or historical data to estimate accurately.",
        'Normal Distribution of Differences': "The differences between the paired samples should ideally follow a normal distribution. This is important for the validity of the z-test, especially when sample sizes are large enough to apply the Central Limit Theorem.",
        'No Outliers': "The differences between the paired samples should not contain outliers, as outliers can significantly influence the mean and variance calculations, leading to skewed results.",
        'Random Sampling': "The sample pairs should be randomly drawn from the population. This ensures that the sample pairs accurately represent the population from which they are taken, making the results more generalizable."
    }

    with st.expander("Click for Paired z-Test Assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")

#--------------------------
#functions to check or remind about assumptions (where they cannot be definitively checked)
#--------------------------

#assumption 1:
#Dependent Samples reminder function

def remind_dependent_samples():
    """
    Informs the user about the dependent samples assumption required for the Paired z-Test.

    Returns:
    None: Displays information in Streamlit.
    """
    with st.expander("Check Dependent Samples Assumption"):
        st.write("""
        **Dependent Samples Assumption for Paired z-Test:**\n
        The Paired z-Test requires that the samples are paired or matched in a meaningful way. This means each pair of observations comes from the same unit (e.g., a patient, a geographical location, etc.) measured at two different times or under two different conditions.

        **Explanation:**
        - The test compares two means based on differences within paired observations, assuming that each pair shares common characteristics or conditions that might affect the measurement.

        **Interpretation:**
        - **Samples Are Paired:** If your data consist of matched pairs like before-and-after measurements or comparisons of two different treatments on the same subjects, then this assumption is met.
        - **Samples Are Not Paired:** If the data do not involve such paired measurements, the Paired z-Test is inappropriate. The independence of the pairs is crucial because any correlation between paired observations significantly affects the test outcome.
        
        **Action Required:**
        - Review your data collection and study design to confirm that each data point in one sample directly corresponds to a data point in the other sample, ensuring the pairs are correctly matched.
        - If the pairing is incorrect or not possible, consider using a different test that does not require paired samples.
        """)


#--------------------------
#assumption 2:
#Known Population Variances reminder function
def remind_known_population_variances():
    """
    Informs the user about the known population variances assumption required for the Paired z-Test.

    Returns:
    None: Displays information in Streamlit.
    """
    with st.expander("Explanation"):
        st.write("""
        **Known Population Variances Assumption for Paired z-Test:**\n
        The Paired z-Test requires that the population variances of the differences between paired samples are known. This is typically achieved through previous studies or large sample sizes from which variance can be accurately estimated.

        **Explanation:**
        - Knowing the population variance is crucial as it directly influences the calculation of the z-score, which is used to determine the significance of the observed differences between the paired samples.

        **Interpretation:**
        - **Variances Are Known:** If you have reliable estimates of the population variances from previous data or extensive research, you can proceed with the Paired z-Test.
        - **Variances Are Not Known:** If this information is not available, you might need to reassess whether the Paired z-Test is appropriate. In cases where variance cannot be reliably estimated, considering an alternative test like the Paired t-Test, which does not require known population variances, might be advisable.
        """)



#--------------------------
#functions to check Normal Distribution of Differences

def check_normality_qqplot_altair(df, sample_1, sample_2):
    """
    Displays a Q-Q plot using Altair to check if the differences between two paired samples are normally distributed.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Interpretation:
    - Data points closely following the line suggest normality.
    - Significant deviations from the line indicate departures from normality.
    """
    with st.expander(label='Click for Q-Q plot explanation'):
        st.subheader('Explanation:')
        st.write('The Q-Q (Quantile-Quantile) plot compares the quantiles of the differences against the quantiles of a theoretical normal distribution to assess normality.')
        st.write(":blue[**Blue Points:**] Each point on the Q-Q plot represents a quantile in your data compared to the corresponding quantile of the theoretical normal distribution.")
        st.write(":red[**Red line:**] This line represents what the data points would follow if the sample distribution were perfectly normal.")

    with st.expander(label='Click for Q-Q plot interpretation'):
        st.subheader('Interpretation:')
        st.write("**If the Points Lie on the Red Line:** This suggests the differences are well-modeled by a normal distribution.")
        st.write("**If the Points Deviate from the Red Line:** Significant deviations suggest deviations from normality.")

    with st.expander('Click for Q-Q Plot'):
        # Calculate differences and perform the Q-Q analysis
        differences = df[sample_1] - df[sample_2]
        qq = stats.probplot(differences, dist="norm")

        # Prepare data for plotting
        qq_data = pd.DataFrame({
            'Theoretical Quantiles': [pt[0] for pt in qq[0]],
            'Ordered Values': [pt[1] for pt in qq[0]]
        })

        # Create the Q-Q plot using Altair
        qq_plot = alt.Chart(qq_data).mark_circle(size=60, opacity=0.5).encode(
            x=alt.X('Theoretical Quantiles', title='Theoretical Quantiles'),
            y=alt.Y('Ordered Values', title='Sample Quantiles')
        ).properties(
            title='Q-Q plot for Checking Normality of Differences'
        )

        # Adding a line to represent y=x
        line = alt.Chart(pd.DataFrame({
            'Theoretical Quantiles': qq_data['Theoretical Quantiles'],
            'Ordered Values': qq_data['Theoretical Quantiles']
        })).mark_line(color='red').encode(
            x='Theoretical Quantiles',
            y='Ordered Values'
        )

        st.altair_chart(qq_plot + line, use_container_width=True)



#--------------------------

def perform_shapiro_wilk_test_paired_z_test(df, sample_1, sample_2):
    """
    Performs the Shapiro-Wilk test for normality on the differences between two paired samples and displays the results with explanations.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.
    """
    # Calculate differences
    differences = df[sample_1] - df[sample_2]
    # Perform Shapiro-Wilk test
    w_statistic, p_value = stats.shapiro(differences)

    with st.expander("Click for Shapiro-Wilk test explanation"):
        st.subheader("Explanation of the Shapiro-Wilk Test:")
        st.write("""
        The Shapiro-Wilk test is used to determine whether a dataset is likely to have come from a normal distribution. 
        It is a test of normality that is particularly effective for smaller datasets.
        - **W statistic**: This is the test statistic value that measures the deviation from normality. Closer to 1 indicates more normality.
        - **P-value**: This measures the probability that the observed data could have occurred under the hypothesis of normality. Lower values suggest non-normal data.
        """)

    with st.expander("Click for Shapiro-Wilk test interpretation"):
        st.subheader("Interpretation:")
        st.write("""
        **Interpreting the P-value:**
        - **P-value > 0.05**: Suggests that the differences between the samples do not significantly deviate from a normal distribution, indicating that the data may be considered normal.
        - **P-value ≤ 0.05**: Suggests significant evidence against the normality of the data, indicating that the differences between the samples are likely not normally distributed.
        """)
        st.write(f"Calculated W statistic: {w_statistic:.4f}, P-value: {p_value:.4f}")

    with st.expander('Click for Shapiro-Wilk Test results'):
        # Display the test results and a conclusion based on the p-value
        st.write("**Shapiro-Wilk Test Results:**")
        st.write(f"**W statistic (Test Statistic):** {w_statistic:.4f}")
        st.write(f"**P-value:** {p_value:.4f}")
        conclusion = "Data are normally distributed." if p_value > 0.05 else "Data are not normally distributed. Consider using a non-parametric test."
        st.write(f"**Conclusion:** {conclusion}")
    
    return p_value

#--------------------------
#Function to test assumption of no outliers

def check_for_outliers_paired_z_test(df, sample_1, sample_2):
    """
    Displays a boxplot using Altair to check for outliers in the differences between two paired samples.

    Args:
    df (DataFrame): Source pandas DataFrame containing the paired data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Interpretation:
    - Points outside the whiskers of the boxplot are considered outliers.
    """
    # Explanation of the method
    with st.expander("Click for explanation"):
        st.subheader("Explanation:")
        st.write("""
        This boxplot visualizes the distribution of differences between two paired sets of measurements, highlighting potential outliers. Outliers in paired samples can impact the mean of the differences, which is critical in the paired z test.
        \n**Box and Whiskers:** 
        \n- The central box represents the interquartile range (IQR), the middle 50% of the data. 
        \n- The line inside the box shows the median. 
        \n- Whiskers (vertical lines) extend to the smallest and largest values within 1.5 times the IQR from the quartiles, typically indicating the range for non-outlier data.
        """)

    # Interpretation guide
    with st.expander("Click for interpretation"):
        st.subheader("Interpretation:")
        st.write("""
        \n**Within Whiskers (Typical Values):** 
        \nData points within the whiskers are considered typical and not outliers.
        \n**Outside Whiskers (Potential Outliers):** 
        \n Points that lie beyond the whiskers are considered potential outliers. These outliers may influence the results of a paired z test significantly, especially if the sample size is small.
        """)

    # Visualizing the outliers
    with st.expander('Click for Box Plot'):
        # Calculate differences
        differences = df[sample_1] - df[sample_2]
        diff_df = pd.DataFrame(differences, columns=['Differences'])

        # Create the boxplot using Altair
        box_plot = alt.Chart(diff_df).mark_boxplot(extent='min-max').encode(
            y='Differences:Q'
        ).properties(
            title='Boxplot for Checking Outliers in Differences between Paired Samples'
        )

        # Display the boxplot
        st.altair_chart(box_plot, use_container_width=True)


#--------------------------
#Function to check / confirm random sampling assumption

def check_random_sampling_paired_z_test():
    """
    Informs the user about the random sampling assumption required for the paired samples z-test.

    Returns:
    None: Displays information in Streamlit.
    """
    with st.expander("Click for explanation"):
        st.subheader("Explanation:")
        st.markdown("""
        **Random Sampling Assumption for Paired Samples Z-Test:**
        - Random sampling is crucial to ensure that the pairs are representative of the population from which they are drawn. This assumption supports the generalizability of the test results to the broader population.
        - In the context of paired samples, each pair should be a random, independent sample from the population of all such pairs.

        **Details:**
        - **Randomness**: Each pair included in the study should be selected randomly from the population of interest.
        - **Independence**: The selection of any one pair should not influence the selection of another pair, ensuring that all pairs are independently chosen.
        """)

    with st.expander("Click for interpretation"):
        st.subheader("Interpretation and Action Required:")
        st.markdown("""
        - **Review Study Design:** Carefully review the methodology used to select pairs to ensure that they were chosen randomly and independently.
        - **Potential Biases:** Consider any factors that might have influenced the selection process, such as non-random assignment to treatment and control groups in a clinical trial.
        - **Impact of Non-random Sampling:** Understand that failure to adhere to this assumption could lead to biased results that are not applicable to the general population, potentially invalidating the test outcomes.
        
        **Confirm Sampling Methodology:**
        Ensure that your study's design and data collection methods support the assumption of random sampling. If this assumption is compromised, the conclusions drawn from the z-test may be questioned, and alternative statistical methods or study redesign might be required.
        """)


#--------------------------
#function to combine all assumption checks and reminders logic

def confirm_paired_z_test_assumptions(shapiro_wilk_p_value, alpha=0.05):
    """
    Renders select boxes for the user to manually confirm the assumptions required for the paired samples z-test,
    considering the result from the Shapiro-Wilk normality test for differences.
    
    Args:
    shapiro_wilk_p_value (float): p-value from the Shapiro-Wilk normality test on the differences between the paired samples.
    alpha (float): Significance level, default is 0.05.

    Returns:
    bool: True if all manually checked assumptions are confirmed, False otherwise.
    """
    
    #manual adjustment to confirm error path - testing purposes only
    #shapiro_wilk_p_value = 0.04

    st.subheader("Confirming remaining assumptions for the Paired Samples z-test")
    # Check if the p-value from the normality check is significant
    if shapiro_wilk_p_value <= alpha:
        st.error("Normality assumption is not met based on the Shapiro-Wilk test. Consider using the non-parametric **Wilcoxon Signed-Rank Test** test or transform the data.")
        return False

    # Initialize placeholders
    default_option = "---"
    options = [default_option, "Yes", "No"]

    # User inputs for each assumption
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            dependent_samples_confirmation = st.selectbox(
                "Confirm if the samples are dependent (paired):",
                options=options,
                help="Each observation in one sample should correspond to one observation in the other sample."
            )
        with col1:
            known_variance_confirmation = st.selectbox(
                "Confirm if the population variance is known:",
                options=options,
                help="For the z-test, it is assumed that the population variance is known."
            )
        with col1:
            qq_plot_confirmation = st.selectbox(
                "Having reviewed the Q-Q plot, do the points approximately follow the line?",
                options=options,
                help="A Q-Q plot can show whether the data are normally distributed, which supports the robustness of the z-test."
            )
        with col2:
            no_outliers_confirmation = st.selectbox(
                "Having reviewed the box plot, are there any outliers?",
                options=options,
                help="Outliers can significantly affect the test outcome, especially in tests involving differences."
            )
        with col2:
            random_sampling_confirmation = st.selectbox(
                "Confirm if the data were randomly sampled:",
                options=options,
                help="Ensure that the paired data are randomly sampled from the population."
            )

    # Check if all necessary confirmations are 'Yes'
    if any(x == default_option for x in [dependent_samples_confirmation, known_variance_confirmation, qq_plot_confirmation, no_outliers_confirmation, random_sampling_confirmation]):
        return None  # Wait until all selections are made
    elif all(x == "Yes" for x in [dependent_samples_confirmation, known_variance_confirmation, qq_plot_confirmation, no_outliers_confirmation, random_sampling_confirmation]):
        st.success("All necessary assumptions for the Paired Samples z-test are confirmed.")
        return True
    else:
        issues = []
        if dependent_samples_confirmation == "No":
            issues.append("\n - the samples are not dependent - suggest re-evaluating the experimental design")
        if known_variance_confirmation == "No":
            issues.append("\n - the population variance is unknown - if other assumptions are true, consider **Paired t-Test**")
        if qq_plot_confirmation == "No":
            issues.append("\n - the data may not be normally distributed - suggest using the non-parametric **Wilcoxon Signed-Rank Test**")
        if no_outliers_confirmation == "No":
            issues.append("\n - outliers may affect the test's validity - suggest using the non-parametric **Wilcoxon Signed-Rank Test**")
        if random_sampling_confirmation == "No":
            issues.append("\n - the data may not be randomly sampled - suggest re-evaluating the experimental design")
        
        issues_str = "; ".join(issues)
        recommendation_message = f"""Consider addressing the following issues: {issues_str}. 
        \nAlternative statistical methods may be required."""
        st.error(recommendation_message)
        return False




#-----------------------------------------------
#Function to render all the above functions in the app:
def render_assumption_checks_for_paired_z_test(df):
    
    #display assumptions for the test
    paired_z_test_assumptions()

    #function for user to select samples
    default_option = '---'

    sample_1, sample_2 = user_inputs.select_sample_columns(df)
    
    if sample_1 == default_option or sample_2 == default_option:
        st.write('Please select the column names above.')
        st.stop()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        'Dependent samples',
        'Known population variance',
        'Normal distribution of differences',
        'Box plot (visual outlier check)',
        'Random sampling'
        ])

    #Dependent samples
    with tab1:
        remind_dependent_samples()
    
    #Known population variance
    with tab2:
        remind_known_population_variances()
    
    #Normal distribution of differences (Shapiro Wilk and Q-Q plot)
    with tab3:
        #Q-Q plot
        check_normality_qqplot_altair(df, sample_1, sample_2)
        #Shapiro Wilk test
        p_value = perform_shapiro_wilk_test_paired_z_test(df, sample_1, sample_2)
    
    #Boxplot to check no outliers in the differences between the 2 samples
    with tab4:
        check_for_outliers_paired_z_test(df, sample_1, sample_2)
    
    #random sampling reminder
    with tab5:
        check_random_sampling_paired_z_test()
    

    #user to confirm the assumptions
    test_bool = confirm_paired_z_test_assumptions(p_value)

    # if True means normal dist and if all other assumptions met, can use paired z test
    # if False, means 1+ assumptions not True, give guidance for alternative test(s). 
    return test_bool

