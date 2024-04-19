

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

#-----------------------------------------------------------------------

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