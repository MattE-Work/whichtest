#paired t test
from scipy.stats import ttest_rel
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import streamlit as st
import pandas as pd

#import other functions from files
from stats_test_functions import stats_tests as stat_tests
from functions import user_inputs


#--------------------------
# Paired t test

#functions to check assumptions:
def paired_t_test_assumptions():
    dict_assumptions = {
        'Dependent samples': "The samples must be paired or matched. This is the fundamental requirement for a Paired t-Test, meaning that each subject in one sample corresponds to a subject in the other sample. Common scenarios include before-and-after measurements on the same subjects (e.g., pre-test and post-test scores) or measurements on matched pairs (e.g., siblings or twins).",
        'Scale of measurement': "The data must be measured at least at the interval level, which allows for the use of addition and subtraction operations. Common types of data suitable for a Paired t-Test include continuous data such as weights, scores, or times.",
        'Normal Distribution of Differences': "The differences between the paired samples should follow a normal distribution. This assumption is crucial for the validity of the test. If the sample size is small and the distribution of differences is not normal, the test might not be the appropriate choice.",
        'No Outliers': "The paired differences should not have outliers. Outliers can significantly affect the mean and standard deviation, which are critical for the t-test, potentially leading to misleading results.",
        'Random Sampling': "The sample pairs should be drawn randomly from the population. This ensures that the samples accurately represent the population from which they are taken, allowing for generalizations of the test results to the broader population.",
    }
    return dict_assumptions


#Function to Check Normality using Q-Q Plot using Altair
def check_normality_qqplot_altair(df, sample_1, sample_2):
    """
    Displays a Q-Q plot using Altair to check if the differences between two samples are normally distributed.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Interpretation:
    - Data points closely following the line suggest normality.
    - Significant deviations from the line indicate departures from normality.
    """
    with st.expander(label='Click for explanation'):
            st.subheader('Explanation:')
            st.write('The plot shows the distribution of a dataset relative to a theoretical distribution—in this case, the normal distribution')
            st.write(":blue[**Blue Points:**] Each point on the Q-Q plot represents a quantile in your sample data compared to the corresponding quantile of the theoretical normal distribution. If your dataset has many observations, you will see a scatter of points instead of just one or two.")
            st.write(":red[**Red line:**] This line represents what the data points would follow if the sample distribution were perfectly normal. It's a reference line where the x-values (theoretical quantiles) and y-values (sample quantiles) are equal.")

    with st.expander(label='Click for interpretation'):
        st.subheader('Interpretation:')
        st.write("**If the Points Lie on the Red Line:** This indicates that the sample data are well-modeled by a normal distribution. The closer the points conform to the line, the more normal the data.")
        st.write("**If the Points Deviate from the Red Line:** Deviations from this line suggest deviations from normality:")
        st.write("1. Points forming a curve above or below the line suggest a distribution that has heavier tails or lighter tails than a normal distribution.")
        st.write("2. Points spread far apart from the line, especially in the tails, indicate outliers or extreme values that the normal distribution does not adequately model.")
    
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

        # Combine the points and the line
        st.altair_chart(qq_plot + line, use_container_width=True)


def check_for_outliers_altair(df, sample_1, sample_2):
    """
    Displays a boxplot using Altair to check for outliers in the differences between two samples.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Interpretation:
    - Points outside the whiskers of the boxplot are considered outliers.
    """
    # Explanation and interpretation
    with st.expander("Click for explanation"):
        st.subheader("Explanation:")
        st.write("This boxplot visualizes the distribution of differences between two sets of measurements, highlighting potential outliers.")
        st.write("**Box and Whiskers:** The central box represents the interquartile range (IQR), the middle 50% of the data. The line inside the box shows the median. Whiskers (vertical black lines) extend to the smallest and largest values within 1.5 times the IQR from the quartiles.")

    with st.expander("Click for interpretation"):
        st.subheader("Interpretation:")
        st.write("**Within Whiskers (Typical Values):** Data points within the whiskers are considered typical and not outliers.")
        st.write("**Outside Whiskers (Potential Outliers):** Points that lie beyond the whiskers are potential outliers and may warrant further investigation or exclusion from analysis depending on the context.")
    
    with st.expander('Click for Box Plot'):
        # Calculate differences
        differences = df[sample_1] - df[sample_2]
        diff_df = pd.DataFrame(differences, columns=['Differences'])

        # Create the boxplot using Altair
        box_plot = alt.Chart(diff_df).mark_boxplot(extent='min-max').encode(
            y='Differences:Q'
        ).properties(
            title='Boxplot for Checking Outliers in Differences'
        )

        # Display the boxplot
        st.altair_chart(box_plot, use_container_width=True)

    

'''
# Function to Perform Shapiro-Wilk Test for Normality
def perform_shapiro_wilk_test_paired_t_test_check(df, sample_1, sample_2):
    """
    Performs the Shapiro-Wilk test for normality on the differences between two samples.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Returns:
    tuple: Test statistic (W statistic) and the p-value.

    Interpretation:
    - A p-value greater than 0.05 suggests normality.
    - A p-value less than or equal to 0.05 suggests non-normality.
    """
    differences = df[sample_1] - df[sample_2]
    w_statistic, p_value = shapiro(differences)

    normal_dist_can_use_paired_t = p_value > 0.05

    return w_statistic, p_value, normal_dist_can_use_paired_t

'''

def perform_shapiro_wilk_test_paired_t_test_check_with_explainers(df, sample_1, sample_2):
    """
    Performs the Shapiro-Wilk test for normality on the differences between two samples and displays the results with explanations.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.
    """
    # Calculate differences
    differences = df[sample_1] - df[sample_2]
    # Perform Shapiro-Wilk test
    w_statistic, p_value = stats.shapiro(differences)
    # Determine if the data can be considered normal
    normal_dist_can_use_paired_t = p_value > 0.05

    # Explanation and interpretation
    with st.expander("Click for explanation"):
        st.subheader("Explanation of the Shapiro-Wilk Test:")
        st.write("""
        The Shapiro-Wilk test is used to determine whether a dataset is likely to have come from a normal distribution. 
        It is a test of normality that is particularly effective for smaller datasets.
        - **W statistic**: This is the test statistic value that measures the deviation from normality. Closer to 1 indicates more normality.
        - **P-value**: This measures the probability that the observed data could have occurred under the hypothesis of normality. Lower values suggest non-normal data.
        """)

    with st.expander("Click for interpretation"):
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
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**W statistic (Test Statistic):** {w_statistic:.4f}")
        with col2:
            st.write(f"**P-value:** {p_value:.4f}")
        conclusion = "Data are normally distributed." if normal_dist_can_use_paired_t else "Data are not normally distributed. Consider using a non-parametric test."
        st.write(f"**Conclusion:** {conclusion}")
    return(normal_dist_can_use_paired_t)




#function to render inputs for user to confirm whether assumptions are met, and based on these inputs and bool param, recommend appropriate test
def check_assumptions_and_recommend_test(normal_dist_can_use_paired_t):
    """
    Asks the user to confirm assumptions based on the Q-Q plot and box-plot results and uses the Shapiro-Wilk test result
    to determine if the Paired t-Test or Wilcoxon Signed-Rank Test should be used.

    Args:
    normal_dist_can_use_paired_t (bool): Result from the Shapiro-Wilk test indicating if differences are normally distributed.

    Returns:
    str: Recommendation on which statistical test to use based on the assumptions checks.
    """
    st.subheader("Confirming interpretation of assumption checks")
    col1, col2 = st.columns(2)

    with col1:
        qq_plot_confirmation = st.selectbox(
            "Having reviewed the Q-Q plot, do the points approximately follow the line?",
            options=["Yes", "No"],
            index=0  # Default to 'Yes'
        )

    with col2:
        box_plot_confirmation = st.selectbox(
            "Having reviewed the box-plot, are there any outliers beyond the outer whiskers?",
            options=["No", "Yes"],
            index=0  # Default to 'No'
        )

    # Apply logic based on responses and the boolean value
    if qq_plot_confirmation == "Yes" and box_plot_confirmation == "No" and normal_dist_can_use_paired_t:
        paired_t_test_confirmation_string = "The assumptions that can be checked have been met. If you are happy the other assumptions are met (outlined in the expander at the top of this section) then you can **:green[proceed with the Paired t-Test]**."
        test_bool_result = True
    else:
        issues = []
        if qq_plot_confirmation == "No":
            issues.append("the points do not follow the line in the Q-Q plot")
        if box_plot_confirmation == "Yes":
            issues.append("there are outliers beyond the outer whiskers in the box plot")
        if not normal_dist_can_use_paired_t:
            issues.append("the differences are not normally distributed (Shapiro-Wilk test)")
        
        test_bool_result = False
        issues_str = ", ".join(issues)
        paired_t_test_confirmation_string = f"Assumptions not met because {issues_str}. Non-parametric alternative required."
    return paired_t_test_confirmation_string, test_bool_result


#test function for paired t test:
def paired_t_test(data1, data2, p_value_threshold=0.05):
    """
    Perform a Paired t-Test to determine if there is a significant difference between the means of two related samples.

    Args:
    data1 (array_like): The first set of paired sample data (e.g., pre-treatment scores).
    data2 (array_like): The second set of paired sample data (e.g., post-treatment scores).
    p_value_threshold (float, optional): The threshold for determining statistical significance. Defaults to 0.05.

    Returns:
    tuple: The test statistic, the p-value of the test, and a plain English interpretation of the result.

    Example:
    >>> paired_t_test([1.2, 1.5, 1.8, 2.0, 1.9], [1.1, 1.3, 1.4, 1.8, 1.6])
    """
    # Convert data to numpy arrays for compatibility with scipy functions
    data1 = np.array(data1)
    data2 = np.array(data2)
    # Perform the paired t-test
    stat, p_value = ttest_rel(data1, data2)
    # Interpret the result
    if p_value < p_value_threshold:
        result = "There is significant evidence to reject the null hypothesis. This suggests a statistically significant difference between the means of the paired groups."
    else:
        result = "There is not enough evidence to reject the null hypothesis. This suggests no statistically significant difference between the means of the paired groups."
    return stat, p_value, result


#-----------------------------------------------
#Function to render all the above functions in the app:
def render_assumption_checks_for_paired_t_test(df):
    dict_paired_t_assumptions = stat_tests.paired_t_test_assumptions()

    st.subheader('...for the paired t test')
    with st.expander(label='Click to review required assumptions for this test'):
        for assumption, value in dict_paired_t_assumptions.items():
            st.write(f":red[**{assumption}**:]\n{value}")

    #function for user to select samples
    sample_1_col, sample_2_col = user_inputs.select_sample_columns(df)
    
    tab1, tab2, tab3 = st.tabs(['Q-Q plot (visual normal dist. check)', 'Box plot (visual outlier check)', 'Normal dist check'])
    #Q-Q plot tab
    with tab1:
        #visual check for normality using Q-Q plot
        check_normality_qqplot_altair(df, sample_1_col, sample_2_col)
    
    #boxplot tab
    with tab2:
        check_for_outliers_altair(df, sample_1_col, sample_2_col)
    
    with tab3:
        normal_dist_can_use_paired_t = perform_shapiro_wilk_test_paired_t_test_check_with_explainers(df, sample_1_col, sample_2_col)
    
    paired_t_test_confirmation_string, test_bool_result = check_assumptions_and_recommend_test(normal_dist_can_use_paired_t)
    
    st.write(paired_t_test_confirmation_string)
    #return the shapiro bool value
    # if True means normal dist and if all other assumptions met, can use paired t test
    # if False, means not normal dist, recommend using Wilcoxon Signed-Rank Test
    return test_bool_result