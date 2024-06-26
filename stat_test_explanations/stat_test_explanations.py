

def explain_one_sample_t_test():
    explanation = """
    The one-sample t-test is used to determine if the mean of a single sample is significantly different from a known or hypothesized population mean. This test assumes that the sample data is normally distributed. It is most commonly used when you want to test if the average measurement from a single group differs from a specific value.
    """
    requirements = """
    Requirements for the One-sample T-test include:
    - A single set of continuous data.
    - Data must be approximately normally distributed.
    - A known population mean with which to compare the sample mean.
    """
    example_context = """
    Healthcare Example:
    Testing the effectiveness of a new drug on blood pressure levels, a research team might use the one-sample t-test to determine if the average decrease in blood pressure in their sample of patients significantly differs from the hypothesized decrease expected from the drug's use.
    """
    test_type = "Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------
#explain one sample z test
def explain_one_sample_z_test():
    explanation = """
    The one-sample z-test is used to test whether the mean of a population is significantly different from a known or hypothesized value. Unlike the t-test, which assumes an unknown population standard deviation, the z-test assumes that the population standard deviation is known.
    """
    requirements = """
    Requirements for the One-sample Z-test include:
    - A single set of continuous data.
    - Data must be approximately normally distributed.
    - A known population mean with which to compare the sample mean.
    """
    example_context = """
    Example:
    Suppose we want to test whether a new medication affects IQ levels. We have a sample of 20 patients, and their IQ levels at the end of the month are as follows:
    - Sample size (n): 20
    - Sample mean IQ (x): 103.05
    - Population mean IQ (μ₀): 100
    - Population standard deviation (σ): 15
    """
    test_type = "Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

def explain_repeated_measures_anova():
    explanation = """
    Repeated Measures ANOVA is used to analyze the differences between groups when the same participants are subjected to different conditions or measurements over time. This method is particularly useful for studies where participants are measured multiple times under varying conditions. It assumes that the data are normally distributed and the measurements are related.
    """
    requirements = """
    Requirements for Repeated Measures ANOVA include:
    - More than two sets of related sample data, typically time-series or repeated measures from the same subjects.
    - Data must be normally distributed within each group across the repeated measures.
    - Sphericity, which assumes equal variances of the differences between all possible pairs of groups.
    """
    example_context = """
    Healthcare Example:
    In a study examining the effects of different physiotherapy regimens on knee surgery recovery, Repeated Measures ANOVA could be used to compare patient mobility scores at multiple time points across several treatment groups.
    """
    test_type = "Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}


#-----------------------------------------------------------------------

def explain_chi_square_test_of_independence():
    explanation = """
    The Chi-square Test of Independence is used to determine if there is a significant relationship between two categorical variables. This non-parametric test assesses whether observed frequencies in a contingency table deviate from expected frequencies, which would suggest independence between the variables.
    """
    requirements = """
    Requirements for the Chi-square Test of Independence include:
    - Two categorical variables organized into a contingency table.
    - Expected frequency count of at least 5 in each cell of the table is recommended to meet the test assumptions.
    """
    example_context = """
    Healthcare Example:
    A public health study might use this test to analyze if there is an association between demographic factors (like age groups or gender) and the incidence of a certain disease, based on data collected from various clinics.
    """
    test_type = "Non-Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}


#-----------------------------------------------------------------------

#-----------------------------------------------------------------------


#One-sample Wilcoxon Signed-Rank Test
def explain_one_sample_wilcoxon():
    explanation = """
    The One-sample Wilcoxon signed-rank test is a non-parametric alternative to the one-sample t-test, used to compare the median of a single sample to a hypothesized median, typically when data are not normally distributed.
    """
    requirements = """
    Requirements include:
    - A single sample of ordinal or continuous data.
    - The data should not assume normal distribution.
    - Used when comparing the sample median against a hypothesized median.
    """
    example_context = """
    Healthcare Example:
    Testing the effect of a new diet on cholesterol levels, with cholesterol reductions recorded for a sample of patients. The test determines if the median reduction is significantly different from the expected median reduction hypothesized.
    """

    test_type = "Non-Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

#Chi-square Goodness of Fit Test
def explain_chi_square_goodness_of_fit():
    explanation = """
    The Chi-square goodness of fit test determines if a sample data matches a population with a specific distribution. It's typically used for nominal data.
    """
    requirements = """
    Requirements include:
    - One sample of nominal data.
    - Expected frequencies of categories known a priori.
    """
    example_context = """
    Healthcare Example:
    Evaluating whether the number of patients diagnosed with four different types of diseases follows an expected distribution across those diseases.
    """
    
    test_type = "Non-Parametric"
    
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

#One-sample Non-parametric Test (e.g., Run Test for Trends)
def explain_one_sample_non_parametric_test():
    explanation = """
    The Run test for trends is a non-parametric test used to identify non-randomness in data, such as trends over time, within a single sample.
    """
    requirements = """
    Requirements include:
    - A single sample of ordinal or continuous data.
    - No assumption of underlying distribution for the data.
    """
    example_context = """
    Healthcare Example:
    Analyzing patient recovery times recorded over consecutive days to detect any trend indicating improvement or deterioration.
    """
    
    test_type = "Non-Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

#Wilcoxon Signed-Rank Test for Two Samples
def explain_wilcoxon_signed_rank():
    explanation = """
    The Wilcoxon signed-rank test is used to compare two related samples, matched samples, or repeated measurements on a single sample to assess whether their population mean ranks differ. It's a non-parametric alternative to the paired t-test.
    """
    requirements = """
    Requirements include:
    - Two related samples or paired measurements.
    - The data should not assume normal distribution.
    """
    example_context = """
    Healthcare Example:
    Comparing pain scores before and after treatment within the same group of patients using a non-normally distributed scale.
    """

    test_type = "Non-Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

#Kruskal-Wallis Test
def explain_kruskal_wallis():
    explanation = """
    The Kruskal-Wallis test is a non-parametric alternative to ANOVA. It's used to determine if there are statistically significant differences between three or more groups of an independent variable on a continuous or ordinal dependent variable without assuming a normal distribution.
    """
    requirements = """
    Requirements include:
    - Three or more independent samples.
    - The data should not assume normal distribution.
    """
    example_context = """
    Healthcare Example:
    Assessing pain relief effectiveness across three different treatment groups where pain relief levels are recorded on an ordinal scale.
    """

    test_type = "Non-Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

#Friedman Test
def explain_friedman_test():
    explanation = """
    The Friedman test is a non-parametric alternative to repeated measures ANOVA. It's used to detect differences in treatments across multiple test attempts where the respondents are the same or related.
    """
    requirements = """
    Requirements include:
    - Three or more related samples.
    - No assumption of normal distribution for the data.
    """
    example_context = """
    Healthcare Example:
    Comparing the effectiveness of three physiotherapy treatments on the same group of patients over different time points.
    """

    test_type = "Non-Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

# Independent t-test
def explain_independent_t_test():
    explanation = """
    The independent t-test compares the means of two unrelated groups to determine if there is a statistically significant difference between them. It assumes that the data are normally distributed.
    """
    requirements = """
    Requirements for the independent t-test include:
    - Two samples of continuous data that are independent of each other.
    - The data should be approximately normally distributed.
    - Homogeneity of variance should ideally be met (similar variances between groups).
    """
    example_context = """
    Healthcare Example:
    Imagine comparing the average recovery times of two different surgical techniques. Patients who underwent Technique A and Technique B are independent groups. The independent t-test can be used to determine if there is a significant difference in recovery times between these two techniques.
    """

    test_type = "Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------
# Independent samples z-test
# Independent z-test
def explain_independent_z_test():
    explanation = """
    The independent z-test compares the means of two unrelated groups to determine if there is a statistically significant difference between them. This test is typically used when sample sizes are large and population variances are known.
    """
    requirements = """
    Requirements for the independent z-test include:
    - Two samples of continuous data that are independent of each other.
    - Large sample sizes (often each group should have more than 30 observations).
    - Known population variances, or the variances can be assumed based on large sample sizes.
    - The data should be approximately normally distributed, especially as sample size decreases.
    """
    example_context = """
    Healthcare Example:
    Consider comparing the average blood pressure levels between patients treated with two different medications. Patients who received Medication A and those who received Medication B are independent groups. The independent z-test can be used to determine if there is a significant difference in average blood pressure levels between these two medications.
    """

    test_type = "Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}



#-----------------------------------------------------------------------

# Mann-Whitney U test
def explain_mann_whitney_u_test():
    explanation = """
    The Mann-Whitney U test is a non-parametric test used to compare differences between two independent groups when the data are not normally distributed.
    """
    requirements = """
    Requirements for the Mann-Whitney U test include:
    - Two samples of ordinal or continuous data that are independent of each other.
    - The test does not assume normality of data, making it suitable for distributions that are skewed.
    """
    example_context = """
    Healthcare Example:
    Consider two groups of patients treated with different pain management therapies. If the pain relief scores (on an ordinal scale) are not normally distributed, the Mann-Whitney U test can be used to determine if there is a statistically significant difference in pain relief between the two therapies.
    """

    test_type = "Non-Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------


# Paired t-test
def explain_paired_t_test():
    explanation = """
    The paired t-test is used to compare the means of two related groups or matched samples to determine if there is a statistically significant difference between them under the assumption of normality.
    """
    requirements = """
    Requirements for the paired t-test include:
    - Two sets of continuous data that are paired or matched, such as pre-test and post-test scores in a medical study.
    - The data should be approximately normally distributed.
    """
    example_context = """
    Healthcare Example:
    A study might compare the blood pressure levels of patients before and after a specific treatment using the same group of patients. The paired t-test can assess whether the treatment had a significant effect on lowering blood pressure.
    """

    test_type = "Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

def explain_paired_z_test():
    explanation = """
    The paired z-test is used to compare the means of two related groups or matched samples to determine if there is a statistically significant difference between them. It is similar to the paired t-test but is used when the population standard deviation is known and the sample size is large enough for the z-distribution to be appropriate.
    """
    requirements = """
    Requirements for the paired z-test include:
    - Two sets of continuous data that are paired or matched, such as measurements before and after a specific intervention.
    - The population standard deviations (variances) should be known, which is less common in practice.
    - The sample size should be large, typically over 30 pairs, to satisfy the central limit theorem, which justifies the use of the z-distribution.
    """
    example_context = """
    Healthcare Example:
    Imagine a clinical trial where the effectiveness of a new drug is assessed by measuring cholesterol levels in patients before and after the drug administration using the same group of patients. The paired z-test can be used to analyze whether there is a significant difference in cholesterol levels due to the drug.
    """

    test_type = "Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}



#-----------------------------------------------------------------------

# ANOVA
def explain_anova():
    explanation = """
    ANOVA is used to compare the means of three or more groups to see if at least one group mean is significantly different from the others. It assumes that the data are normally distributed.
    """
    requirements = """
    Requirements for ANOVA include:
    - Three or more independent samples of continuous data.
    - The data should be approximately normally distributed.
    - Homogeneity of variances across the groups.
    """
    example_context = """
    Healthcare Example:
    A study might compare the effectiveness of three different medications for treating high blood pressure. ANOVA can be used to assess whether the mean reduction in blood pressure differs significantly among the three medications.
    """

    test_type = "Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

# Pearson Correlation
def explain_pearson_correlation():
    explanation = """
    Pearson correlation measures the linear relationship between two continuous variables. It assumes that the data are normally distributed.
    """
    requirements = """
    Requirements for Pearson correlation include:
    - Two sets of continuous data.
    - Both datasets should be approximately normally distributed.
    - The relationship being tested should be linear.
    """
    example_context = """
    Healthcare Example:
    Researchers might be interested in the relationship between age and cholesterol levels in adults. Pearson correlation can be used to assess whether there is a linear relationship between these two variables.
    """

    test_type = "Parametric"

    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------


# Spearman Rank Correlation
def explain_spearman_rank_correlation():
    #Use Spearman's Rank Correlation when dealing with larger datasets and where 
    # computational simplicity and robustness against outliers are key considerations. 
    # It provides a quick and intuitive understanding of the monotonic 
    # relationships in the data.

    explanation = """
    Spearman Rank Correlation is a non-parametric test that measures the strength and direction of association between two ranked variables. It assesses how well the relationship between two variables can be described using a monotonic function. Preferred to Kendalls Tau for larger data sets, or data sets with outliers as it is less sensitive to outliers. Provides a clear indication of both the strength and direction of any present relationship between two variables.
    """
    requirements = """
    Requirements for Spearman Rank Correlation include:
    - Two sets of data, each ranked or ordinal. The test can also be applied to continuous data that is not normally distributed by converting it into ranks.
    - It is ideal for data with outliers or non-linear relationships.
    """
    example_context = """
    Healthcare Example:
    Researchers are interested in the relationship between the rank order of age and the rank order of response times to a reflex test among older adults. The data includes ordinal rankings (e.g., age groups ranked by decade and response times ranked from fastest to slowest).
    """
    test_type = "Non-Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------


# Kendalls Tau
def explain_kendalls_tau():
    #Use Kendall's Tau for smaller datasets or when the data includes many ties. 
    # It's especially suitable for more detailed analyses where a conservative 
    # approach to determining association is preferred.

    explanation = """
    Kendall's Tau is a non-parametric measure that uses a rank correlation coefficient to assess the strength of the relationship between two variables. This test evaluates the association by measuring the correspondence between the ordering of the data points. Kendall's Tau is particularly useful for small datasets or datasets with a large number of ties. It handles ties more rigorously by adjusting for tied ranks in its calculation. Often more conservative than Spearman's correlation, which means it tends to give a lower correlation value. This characteristic can be particularly useful when stringent criteria for determining correlation are desired.
    """
    requirements = """
    Requirements for Kendall's Tau include:
    - Two sets of data that are ordinal (ranked) or continuous data converted to ranks.
    - Suitable for small data sets or data sets with a large number of tied ranks.
    """
    example_context = """
    Healthcare Example:
    A study might examine the correlation between patient satisfaction levels and the number of days spent in the hospital. Patient satisfaction is ranked on a scale from very unsatisfied to very satisfied, and hospital days are ranked from fewer to more days.
    """
    test_type = "Non-Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}

#-----------------------------------------------------------------------

def explain_chi_square_test_for_homogeneity():
    explanation = """
    The Chi-square Test for Homogeneity is used to compare the distribution of categorical variables across different independent groups. This test is ideal for determining whether different populations or groups exhibit similar or different preferences or characteristics in one categorical dimension.
    """
    requirements = """
    Requirements for the Chi-square Test for Homogeneity include:
    - Two or more independent samples.
    - Data must be categorical (nominal).
    - Observations should be independently drawn from the population.
    - The expected frequency count for each category should ideally be 5 or more to satisfy the test assumptions.
    """
    example_context = """
    Healthcare Example:
    Suppose a health department wants to compare the vaccination rates for different vaccines (Pfizer, Moderna, Johnson & Johnson) across various regions (North, South, East, West). The Chi-square Test for Homogeneity can be applied to see if there is a significant difference in vaccine preferences or acceptance rates across these regions.
    """
    test_type = "Non-Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}


#-----------------------------------------------------------------------

def explain_mcnemars_test():
    explanation = """
    McNemar's Test is used to determine if there are significant changes in the proportions of categorical outcomes between two related groups on the same subjects. This test is applicable when the data are nominal and the two samples are related, such as in before-and-after studies.
    """
    requirements = """
    Requirements for McNemar's Test include:
    - Two related samples of nominal data.
    - Data collected from the same subjects under two different conditions or at two different times.
    - The data format should ideally be a 2x2 contingency table representing the paired observations.
    """
    example_context = """
    Healthcare Example:
    Consider a clinical study testing the efficacy of a new treatment for a skin condition, where each patient's condition (improved or not improved) is recorded before and after the treatment. McNemar's Test can be used to analyze whether the treatment led to a significant change in the proportion of patients showing improvement.
    """
    test_type = "Non-Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}



#-----------------------------------------------------------------------

def explain_fishers_exact_test():
    explanation = """
    Fisher's Exact Test is used to determine if there are non-random associations between two categorical variables in a 2x2 contingency table. Unlike the chi-square test, which approximates probabilities with a chi-square distribution, Fisher's test calculates the exact probability of observing the data as extreme as, or more extreme than, what is observed, assuming the null hypothesis is true.
    """
    requirements = """
    Requirements for Fisher's Exact Test include:
    - Data must be in a 2x2 contingency table format.
    - The test is used for categorical data.
    - Ideally suited for small sample sizes where the chi-square test assumptions might not hold, especially when expected frequencies in the contingency table are below 5.
    """
    example_context = """
    Healthcare Example:
    Evaluating the effectiveness of a new drug versus a placebo, where patients are categorized as either 'improved' or 'not improved'. Fisher's Exact Test can be used to analyze whether the proportions of improved patients differ significantly between the drug and placebo groups, particularly useful in studies with small sample sizes.
    """
    test_type = "Non-Parametric"
    return {'Explanation': explanation, 'Requirements': requirements, 'Example Context': example_context, 'Test Type': test_type}




#-----------------------------------------------------------------------

def get_dict_test_explanation(test_name):

    placeholder_text = 'Functionality not yet built'

    dict_tests_and_recommendations = {
    'Chi-square goodness of fit': explain_chi_square_goodness_of_fit(),
    'Chi-square test of independence': explain_chi_square_test_of_independence(),
    "Cramer's V": placeholder_text,
    'Exact test of Goodness of Fit (multinomial model)': placeholder_text,
    'Exact test of Goodness of Fit': placeholder_text,
    'Factorial ANOVA': placeholder_text,
    'Fischers Exact test': explain_fishers_exact_test(),
    'G-test of Goodness of Fit': placeholder_text,
    'G-test': placeholder_text,
    'Independent samples T-test': explain_independent_t_test(),
    'Independent samples Z-test': explain_independent_z_test(),
    "Kendall's Tau": explain_kendalls_tau(),
    'Kruskal-Wallis': explain_kruskal_wallis(),
    'Log-linear analysis': placeholder_text,
    'Mann-Whitney U Test': explain_mann_whitney_u_test(),
    'McNemars test': explain_mcnemars_test(),
    'One-proportion z-test': placeholder_text,
    'One-way ANCOVA': placeholder_text,
    'One-way ANOVA': explain_anova(),
    'Paired samples T-test': explain_paired_t_test(),
    'Paired samples Z-test': explain_paired_z_test(),
    'Partial correlation': placeholder_text,
    'Pearson correlation': explain_pearson_correlation(),
    'Phi co-efficient': placeholder_text,
    "Point biserial correlation": placeholder_text,
    'Single sample T-test': explain_one_sample_t_test(),
    'Single sample wilcoxon signed-rank test': explain_one_sample_wilcoxon(),
    'Single sample Z-test': explain_one_sample_z_test(),
    "Spearman's Rho": placeholder_text,
    'Two proportion z-test': placeholder_text,
    'Wilcoxon signed-rank test': explain_wilcoxon_signed_rank(),
    }

    dict_for_selected_test = dict_tests_and_recommendations[test_name]
    dict_for_selected_test['video'] = get_test_explanation_video(test_name)

    return dict_for_selected_test

'''
def get_dict_test_explanation():
    dict_tests_and_recommendations = {
        'one_sample_t_test': explain_one_sample_t_test(),
        'repeated_measures_anova': explain_repeated_measures_anova(),
        'chi_square_test_of_independence': explain_chi_square_test_of_independence(),
        'one_sample_wilcoxon': explain_one_sample_wilcoxon(),
        'chi_square_goodness_of_fit': explain_chi_square_goodness_of_fit(),
        'one_sample_non_parametric_test': explain_one_sample_non_parametric_test(),
        'wilcoxon_signed_rank': explain_wilcoxon_signed_rank(),
        'kruskal_wallis': explain_kruskal_wallis(),
        'friedman_test': explain_friedman_test(),
        'independent_t_test': explain_independent_t_test(),
        'mann_whitney_u_test': explain_mann_whitney_u_test(),
        'paired_t_test': explain_paired_t_test(),
        'anova': explain_anova(),
        'pearson_correlation': explain_pearson_correlation(),
        'spearman_rank_correlation': explain_spearman_rank_correlation(),
        'kendalls_tau': explain_kendalls_tau(),
        'chi_square_test_for_homogeneity': explain_chi_square_test_for_homogeneity(),
        'mcnemars_test': explain_mcnemars_test(),
    }

    return dict_tests_and_recommendations
'''

#-----------------------------------------------------------------------
def get_test_explanation_video(test_name):

    placeholder_text = 'Video link not yet included'


    dict_tests_and_recommendations = {
    'Chi-square goodness of fit': 'https://youtu.be/y24q6BhRiDc?si=hfiGfJK0GUwQ32d5',
    'Chi-square test of independence': 'https://youtu.be/NTHA9Qa81R8?si=bsnhuJkPWpPEiOsC',
    "Cramer's V": placeholder_text,
    'Exact test of Goodness of Fit (multinomial model)': placeholder_text,
    'Exact test of Goodness of Fit': placeholder_text,
    'Factorial ANOVA': placeholder_text,
    'Fischers Exact test': 'https://www.youtube.com/watch?v=jwkP_ERw9Ak',
    'G-test of Goodness of Fit': placeholder_text,
    'G-test': placeholder_text,
    'Independent samples T-test': 'https://youtu.be/ujLHJKrgx1A?si=AaR8Afe8GIUiJZLw',
    'Independent samples Z-test': 'https://www.youtube.com/watch?v=5ABpqVSx33I',
    "Kendall's Tau": 'https://youtu.be/Pm8KV5f3JM0?si=v0xnR_poOFzikKGh',
    'Kruskal-Wallis': 'https://youtu.be/l86wEhUzkY4?si=9NUInmGQURglCp3z',
    'Log-linear analysis': placeholder_text,
    'Mann-Whitney U Test': 'https://youtu.be/LcxB56PzylA?si=jLywahNmxFjEQuwh',
    'McNemars test': 'https://youtu.be/p338YiJVi18?si=q3thjHuE7XexzExW',
    'One-proportion z-test': placeholder_text,
    'One-way ANCOVA': placeholder_text,
    'One-way ANOVA': 'https://youtu.be/0NwA9xxxtHw?si=9v6gx6prN6tKmEIC',
    'Paired samples T-test': 'https://youtu.be/_7IW2PUqe64?si=34J7xDSPI07f7NFX',
    'Paired samples Z-test': 'https://www.statstest.com/paired-samples-z-test/',
    'Partial correlation': placeholder_text,
    'Pearson correlation': 'https://youtu.be/k7IctLRiZmo?si=auIioQ9hPPNis_Xv',
    'Phi co-efficient': placeholder_text,
    "Point biserial correlation": placeholder_text,
    'Single sample T-test': 'https://youtu.be/pXuFeRCMTAo?si=bponMzjdrDQFtwx9',
    'Single sample wilcoxon signed-rank test': 'https://youtu.be/EvpqzUN56sA?si=LQTLl2e2TUMTO458',
    'Single sample Z-test': 'https://www.youtube.com/watch?v=BWJRsY-G8u0',
    "Spearman's Rho": placeholder_text,
    'Two proportion z-test': placeholder_text,
    'Wilcoxon signed-rank test': 'https://youtu.be/EvpqzUN56sA?si=LQTLl2e2TUMTO458',
    }

    video_url = dict_tests_and_recommendations[test_name]

    return video_url


#-----------------------------------------------------------------------
'''
def get_test_explanation_video():
    dict_tests_and_recommendations = {
    'one_sample_t_test': 'https://youtu.be/pXuFeRCMTAo?si=bponMzjdrDQFtwx9',
    'repeated_measures_anova': 'https://youtu.be/FIxzP4fmi3w?si=ln-E3pQje9MDCPE9',
    'chi_square_test_of_independence': 'https://youtu.be/NTHA9Qa81R8?si=bsnhuJkPWpPEiOsC',
    'one_sample_wilcoxon': 'https://youtu.be/EvpqzUN56sA?si=LQTLl2e2TUMTO458',
    'chi_square_goodness_of_fit': 'https://youtu.be/y24q6BhRiDc?si=hfiGfJK0GUwQ32d5',
    'one_sample_non_parametric_test': 'https://youtu.be/wIwqsXMa1cY?si=l9m9WtagiGDhI5Fe',
    'wilcoxon_signed_rank': 'https://youtu.be/EvpqzUN56sA?si=LQTLl2e2TUMTO458',
    'kruskal_wallis': 'https://youtu.be/l86wEhUzkY4?si=9NUInmGQURglCp3z',
    'friedman_test': 'https://youtu.be/2moNzzkkZwU?si=3qBC8y3N9h3uadhG',
    'independent_t_test': 'https://youtu.be/ujLHJKrgx1A?si=AaR8Afe8GIUiJZLw',
    'mann_whitney_u_test': 'https://youtu.be/LcxB56PzylA?si=jLywahNmxFjEQuwh',
    'paired_t_test': 'https://youtu.be/_7IW2PUqe64?si=34J7xDSPI07f7NFX',
    'anova': 'https://youtu.be/0NwA9xxxtHw?si=9v6gx6prN6tKmEIC',
    'pearson_correlation': 'https://youtu.be/k7IctLRiZmo?si=auIioQ9hPPNis_Xv',
    'spearman_rank_correlation': 'https://youtu.be/XV_W1w4Nwoc?si=E_fOAUtRRM6J8zhv',
    'kendalls_tau': 'https://youtu.be/Pm8KV5f3JM0?si=v0xnR_poOFzikKGh',
    'chi_square_test_for_homogeneity': 'https://youtu.be/t_jfTOE44YQ?si=PRu48vYIPWJX3TDF',
    'mcnemars_test': 'https://youtu.be/p338YiJVi18?si=q3thjHuE7XexzExW',
        }
    
    return dict_tests_and_recommendations
'''