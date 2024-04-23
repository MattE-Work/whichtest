
#--------------------------
#<< Parametric Test >>
#--------------------------
#one sample t-test
from scipy.stats import ttest_1samp

#independent t-test
from scipy.stats import ttest_ind
from scipy.stats import levene #to test for equal variances assumption
from scipy.stats import shapiro #to test for normal distribution assumption
from math import e #to test for normal distribution assumption


#paired t test
from scipy.stats import ttest_rel
import scipy.stats as stats

#--------------------------
#<< Non-Parametric Test >>
#--------------------------
#one sample wilcoxon
from scipy.stats import wilcoxon

#chi square test for homogeneity
from scipy.stats import chi2_contingency

#--------------------------
#<< Standard Libraries >>
#--------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

#--------------------------
# Import modules
#--------------------------
from stats_test_functions import dummy_data_creator as dummy_data

#--------------------------
#List of tests in scope
#--------------------------

# << Parametric Tests >>
#One-Sample t-Test - assumptions check for this test done
#Independent t-Test - assumptions check for this test done
#Paired t-Test - assumptions checking section done
#Repeated Measures ANOVA - assumptions checking section done
#ANOVA (Analysis of Variance) - assumptions checking section done
#Pearson Correlation - assumptions checking section done

# << Non-Parametric Tests >>
#One-Sample Wilcoxon - NEXT TO DO
#Chi-Square Test of Independence
#Chi-Square Goodness of Fit
#One-Sample Non-Parametric Test
#Wilcoxon Signed-Rank
#Kruskal Wallis
#Friedman Test
#Mann-Whitney U Test
#Spearman Rank Correlation
#Kendall’s Tau





#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Functions for parametric tests
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# One sample t test
def one_sample_t_test(data, population_mean, p_value_threshold=0.05):
    """
    Perform a one-sample t-test to determine if the mean of a single sample is significantly different from the population mean.

    Args:
    data (array_like): The sample data, which should be continuous.
    population_mean (float): The mean value of the population to which the sample mean is compared.
    p_value_threshold (float, optional): The threshold for determining statistical significance. Defaults to 0.05.

    Returns:
    tuple: The test statistic, the p-value of the test, and a plain English interpretation of the result.

    Example:
    >>> one_sample_t_test([1.2, 1.5, 1.8, 2.0, 1.9], 1.5)
    """
    # Convert the data into a numpy array for compatibility with scipy functions
    data = np.array(data)
    # Perform the one-sample t-test
    stat, p_value = ttest_1samp(data, population_mean)
    # Interpret the result
    if p_value < p_value_threshold:
        result = "There is significant evidence to reject the null hypothesis. This suggests the mean of the sample is different from the population mean."
    else:
        result = "There is not enough evidence to reject the null hypothesis. This suggests the mean of the sample may not be different from the population mean."
    return stat, p_value, result

#--------------------------
# Independent t-Test

#functions to check assumptions:

#test for equal variance in both samples
def test_equal_variance(sample1, sample2):
    """
    Test if two samples have equal variances using Levene's Test.

    Args:
    sample1 (array_like): First sample dataset.
    sample2 (array_like): Second sample dataset.

    Returns:
    bool: True if the test suggests equal variances, False otherwise.

    Example:
    >>> test_equal_variance([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    """
    stat, p_value = levene(sample1, sample2)
    return p_value > 0.05  # Common threshold for statistical significance


#function to check samples are normally distributed
def test_normality(sample1, sample2):
    """
    Test if both samples are normally distributed using the Shapiro-Wilk Test.

    Args:
    sample1 (array_like): First sample dataset.
    sample2 (array_like): Second sample dataset.

    Returns:
    bool: True if both samples are normally distributed, False otherwise.

    Example:
    >>> test_normality([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    """
    stat1, p_value1 = shapiro(sample1)
    stat2, p_value2 = shapiro(sample2)

    bool_normal = p_value1 > 0.05 and p_value2 > 0.05  # Common threshold for statistical significance

    if bool_normal == True:
      recommended_test = 'independent t test can be used if samples have equal variance'
    else:
      recommended_test = 'normal distribution assumption not met. Use Mann Whitney U test instead.'

    return bool_normal, recommended_test


def check_independent_t_test_assumptions(normal_dist, equal_var):
    #code to check assumptions have both been met and advise on appropriate test
    if normal_dist and equal_var:
        return('run independent t test using independent t test function as assumptions are met')
    elif normal_dist and not equal_var:
        return('run welches t test using independent t test function, by passing in equal_var this will default to using welches t test variant')
    elif not normal_dist and equal_var:
        return('run mann whitney U test instead as the non parametric alternative to the independent t test. Mann whitney does not assume normality.')
    elif not normal_dist and not equal_var:
        return('run mann whitney U test instead as the non parametric alternative to the independent t test. Mann whitney does not assume normality.')
    else:
        return('error in logic')


#test function:
def independent_t_test(data1, data2, p_value_threshold=0.05, equal_var=True):
    """
    Perform an Independent t-Test (two-sample t-Test) to determine if there is a significant difference
    between the means of two independent samples. Can use Welch's t-test for unequal variances.

    Args:
    data1 (array_like): The first sample dataset.
    data2 (array_like): The second sample dataset.
    p_value_threshold (float, optional): The threshold for determining statistical significance. Defaults to 0.05.
    equal_var (bool, optional): Assumption of equal variance. True assumes equal variance (standard t-test),
                                False uses Welch's t-test, which does not assume equal variance. Defaults to True.

    Returns:
    tuple: The test statistic, the p-value of the test, and a plain English interpretation of the result.

    Example:
    >>> independent_t_test([1.2, 1.5, 1.8, 2.0, 1.9], [1.1, 1.3, 1.4, 1.8, 1.6])
    """
    # Convert data to numpy arrays for compatibility with scipy functions
    data1 = np.array(data1)
    data2 = np.array(data2)
    # Perform the independent t-test
    stat, p_value = ttest_ind(data1, data2, equal_var=equal_var)
    # Interpret the result
    if p_value < p_value_threshold:
        result = "There is significant evidence to reject the null hypothesis. This suggests a statistically significant difference between the means of the two groups."
    else:
        result = "There is not enough evidence to reject the null hypothesis. This suggests no statistically significant difference between the means of the two groups."
    return stat, p_value, result

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

#Function to Check Normality using Q-Q Plot
def check_normality_qqplot(df, sample_1, sample_2):
    """
    Displays a Q-Q plot to check if the differences between two samples are normally distributed.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Interpretation:
    - Data points closely following the diagonal line suggest normality.
    - Significant deviations from the line indicate departures from normality.
    """
    differences = df[sample_1] - df[sample_2]
    stats.probplot(differences, dist="norm", plot=plt)
    plt.title('Q-Q plot for checking normality of differences')
    plt.xlabel('Theoretical quantiles')
    plt.ylabel('Sample quantiles')
    plt.show()

#Function to Check for Outliers using Boxplot
def check_for_outliers(df, sample_1, sample_2):
    """
    Displays a boxplot to check for outliers in the differences between two samples.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    sample_1 (str): Column name for the first sample.
    sample_2 (str): Column name for the second sample.

    Interpretation:
    - Points outside the whiskers of the boxplot are considered outliers.
    """
    differences = df[sample_1] - df[sample_2]
    plt.boxplot(differences)
    plt.title('Boxplot for checking outliers in differences')
    plt.ylabel('Differences')
    plt.show()


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
    st.header("Assumption Checks for Paired t-Test")
    col1, col2 = st.columns(2)

    with col1:
        qq_plot_confirmation = st.selectbox(
            "Having reviewed the Q-Q plot, confirm whether the points approximately follow the line:",
            options=["Yes", "No"],
            index=0  # Default to 'Yes'
        )

    with col2:
        box_plot_confirmation = st.selectbox(
            "Having reviewed the box-plot, confirm whether there are any outliers beyond the outer whiskers:",
            options=["No", "Yes"],
            index=0  # Default to 'No'
        )

    # Apply logic based on responses and the boolean value
    if qq_plot_confirmation == "Yes" and box_plot_confirmation == "No" and normal_dist_can_use_paired_t:
        return "All assumptions for the Paired t-Test are met. You can proceed with the Paired t-Test."
    else:
        issues = []
        if qq_plot_confirmation == "No":
            issues.append("the points do not follow the line in the Q-Q plot")
        if box_plot_confirmation == "Yes":
            issues.append("there are outliers beyond the outer whiskers in the box plot")
        if not normal_dist_can_use_paired_t:
            issues.append("the differences are not normally distributed (Shapiro-Wilk test)")

        issues_str = ", ".join(issues)
        return f"Assumptions not met because {issues_str}. Recommend using the Wilcoxon Signed-Rank Test as a non-parametric alternative."



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

#--------------------------
#Repeated Measures ANOVA



#--------------------------
#ANOVA (Analysis of Variance)


#--------------------------
#Pearson Correlation



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# << Non Parametric Tests >>
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#one sample wilcoxon
def one_sample_wilcoxon(data, hypothesized_median=0, p_value_threshold=0.05):
    """
    Perform a one-sample Wilcoxon signed-rank test and provide an interpretation of the result.

    Args:
    data (array_like): The sample data, which should be ordinal or continuous.
    hypothesized_median (float or int, optional): The hypothesized median value to which the sample median is compared. Defaults to 0.
    p_value_threshold (float, optional): The threshold for determining statistical significance. Defaults to 0.05.

    Returns:
    tuple: The test statistic, the p-value of the test, and a plain English interpretation of the result.

    Example:
    >>> one_sample_wilcoxon([120, 130, 140, 145, 150, 132, 136, 144], 135)
    """
    # Calculate differences from the hypothesized median
    differences = np.array(data) - hypothesized_median
    # Remove zero differences as Wilcoxon test cannot handle zero differences
    differences = differences[differences != 0]
    # Perform the Wilcoxon signed-rank test
    stat, p_value = wilcoxon(differences)
    # Interpret the result
    if p_value < p_value_threshold:
        result = "There is significant evidence to reject the null hypothesis. This suggests the median of the sample is different from the hypothesized median."
    else:
        result = "There is not enough evidence to reject the null hypothesis. This suggests the median of the sample may not be different from the hypothesized median."
    return stat, p_value, result



#--------------------------
#Chi square test of independence


#--------------------------
#Chi square Goodness of Fit




#--------------------------
#One-Sample Non-Parametric Test



#--------------------------
#Wilcoxon Signed-Rank



#--------------------------
#Kruskal Wallis




#--------------------------
#Friedman Test



#--------------------------
#Mann-Whitney U Test




#--------------------------
#Spearman Rank Correlation




#--------------------------
#Kendall’s Tau




#--------------------------
#Chi square test for homogeneity

def chi_square_homogeneity(data, p_value_threshold=0.05):
    """
    Perform a Chi-square test for homogeneity to compare category distributions across different groups and interpret the result.

    Args:
    data (2D array_like): A contingency table where rows are categories and columns are groups. Each cell is the count of occurrences.
    p_value_threshold (float, optional): The threshold for determining statistical significance. Defaults to 0.05.

    Returns:
    tuple: Chi-square statistic, p-value, degrees of freedom, expected frequencies table, and a plain English interpretation of the result.

    Example:
    >>> chi_square_homogeneity([[10, 20, 30], [20, 15, 5]])
    """
    # Perform the chi-square test for homogeneity
    chi2_stat, p_value, dof, expected = chi2_contingency(data)
    # Interpret the result
    if p_value < p_value_threshold:
        result = "There is significant evidence to reject the null hypothesis. This suggests the distributions across the groups are not the same."
    else:
        result = "There is not enough evidence to reject the null hypothesis. This suggests the distributions across the groups may be the same."
    return chi2_stat, p_value, dof, expected, result


#--------------------------

#--------------------------

#--------------------------

#--------------------------


