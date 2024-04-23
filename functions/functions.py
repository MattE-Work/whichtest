#import libraries



#define functions
def recommend_test(data_type, is_normally_distributed, number_of_samples, sample_relationship, hypothesis_type, num_variables=None):
    """
    Recommend appropriate statistical tests based on input parameters.

    Parameters:
    - data_type: 'Nominal', 'Ordinal', 'Interval', 'Ratio'
    - is_normally_distributed: 'Yes' or 'No' indicating whether the data is assumed to be normally distributed
    - number_of_samples: 'One', 'Two', 'More than two' indicating the number of samples to compare
    - sample_relationship: 'Independent' or 'Dependent' indicating the relationship between samples
    - hypothesis_type: 'Differences' or 'Associations' indicating the type of hypothesis being tested

    Returns:
    - List of recommended statistical tests based on the given conditions.
    """
    recommendations = []
    recommendations_keys = []

    # Handle the scenario where there's only one sample
    if number_of_samples == 'One':
        # Recommendations for one sample are based on the number of variables
        if num_variables == 'One variable':  # This block handles the case with one variable
            if data_type == 'Nominal':
                recommendations.append('Chi-square goodness of fit test')
                recommendations_keys.append('chi_square_goodness_of_fit')
            elif data_type == 'Ordinal':
                recommendations.append('One-sample non-parametric test (e.g., Run test for trends)')
                recommendations_keys.append('one_sample_non_parametric_test')
            elif data_type in ['Interval', 'Ratio']:
                if is_normally_distributed == 'Yes':
                    recommendations.append('One-sample t-test')
                    recommendations_keys.append('one_sample_t_test')
                else:
                    recommendations.append('One-sample Wilcoxon signed-rank test')
                    recommendations_keys.append('one_sample_wilcoxon')

        elif num_variables == 'Two variables':  # This block handles the case with two variables
            if data_type == 'Nominal':
                recommendations.append('Chi-square Test for Homogeneity')
                recommendations_keys.append('chi_square_test_for_homogeneity')
            elif data_type == 'Ordinal':
                recommendations.append('Spearman Rank Correlation (for non-normally distributed data)')
                recommendations_keys.append('spearman_rank_correlation')
                #recommendations.append("Kendall's Tau")
                #recommendations_keys.append('kendalls_tau')
            
            elif data_type in ['Interval', 'Ratio']:
                if is_normally_distributed == 'Yes':
                    recommendations.append('Pearson Correlation (for normally distributed data)')
                    recommendations_keys.append('pearson_correlation')
                else:
                    recommendations.append('Spearman Rank Correlation (for non-normally distributed data)')
                    recommendations_keys.append('spearman_rank_correlation')
        # Additional logic for more than two variables can be added here if needed

    elif hypothesis_type == 'Differences':
        if number_of_samples == 'One':
            if data_type in ['Interval', 'Ratio']:
                if is_normally_distributed == 'Yes':
                    recommendations.append('One-sample t-test')
                    recommendations_keys.append('one_sample_t_test')
                
                else:
                    recommendations.append('One-sample Wilcoxon signed-rank test')
                    recommendations_keys.append('one_sample_wilcoxon')
            
            elif data_type == 'Nominal':
                recommendations.append('Chi-square goodness of fit test')
                recommendations_keys.append('chi_square_goodness_of_fit')

            elif data_type == 'Ordinal':
                recommendations.append('One-sample non-parametric test (e.g., Run test for trends)')
                recommendations_keys.append('one_sample_non_parametric_test')

        elif number_of_samples == 'Two':
            if sample_relationship == 'Independent':
                if is_normally_distributed == 'Yes':
                    recommendations.append('Independent t-test (for normally distributed data)')
                    recommendations_keys.append('independent_t_test')

                else:
                    if data_type == 'Ordinal':
                        recommendations.append('Mann-Whitney U test (for non-normally distributed data)')
                        recommendations_keys.append('mann_whitney_u_test')
                    else:
                        recommendations.append('Chi-square test of independence')
                        recommendations_keys.append('chi_square_test_of_independence')
            
            else:
                if is_normally_distributed == 'Yes':
                    recommendations.append('Paired t-test (for normally distributed data)')
                    recommendations_keys.append('paired_t_test')

                else:
                    if data_type == 'Ordinal':
                        recommendations.append('Wilcoxon signed-rank test (for non-normally distributed data)')
                        recommendations_keys.append('wilcoxon_signed_rank')
                    else:
                        recommendations.append("McNemar's Test")
                        recommendations_keys.append('mcnemars_test')

        
        elif number_of_samples == 'More than two':
            if sample_relationship == 'Independent':
                if is_normally_distributed == 'Yes':
                    recommendations.append('ANOVA (for normally distributed data)')
                    recommendations_keys.append('anova')

                else:
                    recommendations.append('Kruskal-Wallis test (for non-normally distributed data)')
                    recommendations_keys.append('kruskal_wallis')

            else:
                if is_normally_distributed == 'Yes':
                    recommendations.append('Repeated measures ANOVA (for normally distributed data)')
                    recommendations_keys.append('repeated_measures_anova')

                else:
                    recommendations.append('Friedman test (for non-normally distributed data)')
                    recommendations_keys.append('friedman_test')

    elif hypothesis_type == 'Associations' and number_of_samples != 'One':
        if data_type in ['Interval', 'Ratio']:
            #if is_normally_distributed == 'Yes':
                #PEARSON INCORRECT HERE
                #recommendations.append('Pearson Correlation (for normally distributed data)')
                #recommendations_keys.append('pearson_correlation')
            
            #else:
                recommendations.append('Spearman Rank Correlation (for non-normally distributed data)')
                recommendations_keys.append('spearman_rank_correlation')

        elif data_type == 'Nominal':
            recommendations.append('Chi-square test of independence')
            recommendations_keys.append('chi_square_test_of_independence')

        elif data_type == 'Ordinal':
            recommendations.append('Spearman Rank Correlation (for non-normally distributed data)')
            recommendations_keys.append('spearman_rank_correlation')

            #recommendations.append("Kendall's Tau")
            #recommendations_keys.append('kendalls_tau')

    return recommendations, recommendations_keys
