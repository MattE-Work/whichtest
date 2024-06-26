import streamlit as st

#very useful site explaining tests with a decision logic in the menu bar
#https://www.statstest.com/

#other sources:
#https://www.statstest.com/

#source: https://webspace.ship.edu/pgmarr/Geo441/Statistical%20Test%20Flow%20Chart.pdf
"""
def recommend_test(data_type, is_normally_distributed, number_of_samples, sample_relationship, hypothesis_type, paired_data = None, num_variables=None, variance_known = None, number_of_levels = None):
    if data_type in ['Interval', 'Ratio']:
        
        #Normal branch
        if is_normally_distributed == True: 
            
            #one group
            if number_of_samples == 'One':
                
                #known variance
                if variance_known == True:
                    recommendation = 'One sample z test'
                #unknown variance
                else:
                    recommendation = 'One sample t test'
            
            #Two groups
            elif number_of_samples == 'Two':
                #non-paired data
                if paired_data == False:
                    recommendation = 'F test'
                    
                    st.write('''Note: depending on the result, then run either
                    \n1. 2 sample independent t test for **equal** variances
                    \n2. 2 sample independent t test for **unequal** variances''')

                #paired data
                else:
                    recommendation = 'Paired sample t test'
            
            #More than two groups
            elif number_of_samples == 'More than two':
                
                #One level
                if number_of_levels == 'One level':
                    recommendation = 'Hartley test'
                    st.write('If the Hartley test **is not** significant, run one way ANOVA, then run a Multiple Comaprison (post hoc) Test')
                    st.write('If the Hartley test **is** significant, run Kruskal Wallis H Test')

                #More than one level
                elif number_of_levels == 'More than one level':
                    recommendation = 'Hartley test'
                    st.write('If the Hartley test **is not** significant, run two way ANOVA, then run a Multiple Comaprison (post hoc) Test')
                    st.write('If the Hartley test **is** significant, stop, no further tests')

                #Hierachical levels
                elif number_of_levels == 'Hierachical levels':
                    recommendation = 'Hartley test'
                    st.write('If the Hartley test **is not** significant, run nested ANOVA, then run a Multiple Comaprison (post hoc) Test')
                    st.write('If the Hartley test **is** significant, stop, no further tests')
                else:
                    pass
            
            #Association between two groups
            elif hypothesis_type == 'Associations':
                recommendation = "Pearson's correlation"
            else:
                pass
        
        #Not Normal branch
        elif is_normally_distributed == False:
            
            #one group
            if number_of_samples == 'One':
                recommendation = "Wilcoxon one-sample median test"

            #two groups
            elif number_of_samples == 'Two':
                
                #non-paired data
                if paired_data == False:
                    recommendation = 'Mann-Whitney U test'

                #paired data
                elif paired_data == True:
                    recommendation = 'Wilcoxon paired-sample test'
            
            #More than two groups
            elif number_of_samples == 'More than two':
                recommendation = 'Kruskal-Wallis H test'
                st.write('Then run a Multiple Comaprison (post hoc) Test')

            #Association between two groups
            elif hypothesis_type == 'Associations':
                recommendation = "Spearman's ranked correlation"
            else:
                pass

    elif data_type in ['Nominal', 'Ordinal']:
        #Normal branch
        if is_normally_distributed == True:
            
            #one group
            if number_of_samples == 'One':
                #known variance
                if variance_known == True:
                    recommendation = 'One sample z test'
                #unknown variance
                else:
                    recommendation = 'One sample t test'
            
            #two groups
            elif number_of_samples == 'Two':
                #non-paired data
                if paired_data == False:
                    recommendation = 'F test'
                    
                    st.write('''Note: depending on the result, then run either
                    \n1. 2 sample independent t test for **equal** variances
                    \n2. 2 sample independent t test for **unequal** variances''')

                #paired data
                else:
                    recommendation = 'Paired sample t test'

            #More than two groups
            elif number_of_samples == 'More than two':
                #One level
                if number_of_levels == 'One level':
                    recommendation = 'One-way ANOVA'
                    st.write('Then run a Multiple Comaprison (post hoc) test')

                #More than one level
                elif number_of_levels == 'More than one level':
                    recommendation = 'Two-way ANOVA'
                    st.write('Then run a Multiple Comaprison (post hoc) test')

                #Hierachical levels
                elif number_of_levels == 'Hierachical levels':
                    recommendation = 'Nested ANOVA'
                    st.write('Then run a Multiple Comaprison (post hoc) test')
                else:
                    pass
            
            #Association between two groups
            elif hypothesis_type == 'Associations':
                recommendation = "Pearson's correlation"
            else:
                pass
        
        #Not Normal branch
        if is_normally_distributed == False:
            #one group
            if number_of_samples == 'One':
                recommendation = 'Wilcoxon 1-Sample Median test'
                
            #two groups
            elif number_of_samples == 'Two':
                recommendation = 'Mann-Whitney U test'

            #More than two groups
            elif number_of_samples == 'More than two':
                recommendation = 'Kruskal-Wallis H test'
        
        #Association between two groups
            elif hypothesis_type == 'Associations':
                recommendation = "Spearman's ranked correlation"
            else:
                pass
    else:
        pass

    return recommendation
"""


#----------------------------------
#<<< SECOND ATTEMPT! >>>>
#----------------------------------

"""
def recommend_test(dict_inputs):
    
    list_recommendations = []

    #Differences or Goodness of fit
    if dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit':

        #categorical or proportion data
        if dict_inputs['data_type'] in ['Nominal', 'Ordinal']:
            
            #one sample or group
            #if dict_inputs['number_of_samples'] == 'One':
               
            #One group variable
            if dict_inputs['num_group_variables'] == 'One':

                #Two levels / options
                if dict_inputs['number_of_levels'] == 'Two':
                    
                    #sample size
                    if dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':
                        list_recommendations.append('Exact test of Goodness of Fit')
                    elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
                        list_recommendations.append('One-proportion z-test')
                    elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':
                        list_recommendations.append('G-test of Goodness of Fit')
                    else:
                        pass
            
                #More than two levels / options
                elif dict_inputs['number_of_levels'] == 'More than two':
                    
                    #sample size
                    if dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':
                        list_recommendations.append('Exact test of Goodness of Fit (multinomial model)')
                    elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
                        list_recommendations.append('Chi-square goodness of fit')
                    elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':
                        list_recommendations.append('G-test of Goodness of Fit')
                    else:
                        pass
                    
            #Two samples or groups
            #elif dict_inputs['number_of_samples'] == 'Two':

            #Two group variables
            elif dict_inputs['num_group_variables'] == 'Two':

                #Two levels / options
                if dict_inputs['number_of_levels'] == 'Two':

                    #independent samples
                    if dict_inputs['sample_relationship'] == 'Independent':

                        #sample size
                        if dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':
                            list_recommendations.append('Fischers Exact test')
                        elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
                            list_recommendations.append('Two proportion z-test')
                        elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':
                            list_recommendations.append('G-test')
                        else:
                            pass
                    
                    #paired samples
                    elif dict_inputs['sample_relationship'] == 'Paired':
                        list_recommendations.append('McNemars test')
                
                #More than two levels / options
                elif dict_inputs['number_of_levels'] == 'More than two':

                    #independent samples
                    if dict_inputs['sample_relationship'] == 'Independent':
                        
                        #sample size
                        if dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':
                            list_recommendations.append('Fischers Exact test')
                        elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
                            list_recommendations.append('Chi-square test of independence')
                        elif dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':
                            list_recommendations.append('G-test')
                        else:
                            pass

                    #paired samples
                    elif dict_inputs['sample_relationship'] == 'Paired':
                        list_recommendations.append('McNemars test')

            elif dict_inputs['num_group_variables'] == 'Three':
                list_recommendations.append('Log-linear analysis')

            else:
                pass
        
        #continuous (interval or ratio)
        elif dict_inputs['data_type'] in ['Interval', 'Ratio']:
            
            #one sample or group
            if dict_inputs['number_of_samples'] == 'One':

                #Normally distributed
                if dict_inputs['normal_dist'] == 'Yes':
                    
                    #known pop variance
                    if dict_inputs['population_variance_known'] == 'Yes':
                       list_recommendations.append('Single sample Z-test')
                    #unknown pop variance
                    else:
                        list_recommendations.append('Single sample T-test')

                #Not normally distributed
                else:
                    list_recommendations.append('Single sample wilcoxon signed-rank test')
            
            #Two sample or group
            elif dict_inputs['number_of_samples'] == 'Two':

                #Independent samples
                if dict_inputs['sample_relationship'] == 'Independent':

                    #Normally distributed
                    if dict_inputs['normal_dist'] == 'Yes':
                        
                        #known pop variance
                        if dict_inputs['population_variance_known'] == 'Yes':
                            list_recommendations.append('Independent samples Z-test')
                        #unknown pop variance
                        else:
                            list_recommendations.append('Independent samples T-test')

                    #Not normally distributed
                    else:
                        list_recommendations.append('Mann-Whitney U Test')
                
                #Paired samples
                elif dict_inputs['sample_relationship'] == 'Paired':
                    
                    #Normally distributed
                    if dict_inputs['normal_dist'] == 'Yes':
                        
                        #known pop variance
                        if dict_inputs['population_variance_known'] == 'Yes':
                            list_recommendations.append('Paired samples Z-test')
                        #unknown pop variance
                        else:
                            list_recommendations.append('Paired samples T-test')

                    #Not normally distributed
                    else:
                        list_recommendations.append('Wilcoxon signed-rank test')
            
            #Two sample or group
            elif dict_inputs['number_of_samples'] == 'More than two':
                
                #Independent samples
                if dict_inputs['sample_relationship'] == 'Independent':
                    
                    #Normally distributed
                    if dict_inputs['normal_dist'] == 'Yes':

                        #How many independent variables
                        #Single independent variable
                        if dict_inputs['num_variables'] == 'One':
                            list_recommendations.append('One-way ANOVA')
                        elif dict_inputs['num_variables'] == 'One with a covariate':
                            list_recommendations.append('One-way ANCOVA')
                        elif dict_inputs['num_variables'] == 'Multiple independent variables':
                            list_recommendations.append('Factorial ANOVA')
                    
                    #Not normally distributed
                    else:
                        list_recommendations.append('Kruskal-Wallis')
                        list_recommendations.append('One-way ANOVA')

    #Relationship
    elif dict_inputs['hypothesis_type'] == 'Relationship':
        
        #two continuous variables
        if dict_inputs['nature_of_variables_of_interest'] == 'Two continuous':

            #covariates present
            if dict_inputs['covariates_present'] == 'Yes':
                list_recommendations.append('Partial correlation')
            
            #covariates not present
            else:
                list_recommendations.append('Pearson correlation')
        
        #two categorical variables
        elif dict_inputs['nature_of_variables_of_interest'] == 'Two categorical':

            #2 unique values per variable
            if dict_inputs['number_of_levels'] == 'Two':
                list_recommendations.append('Phi co-efficient')
            
            #more than 2 unique values
            if dict_inputs['number_of_levels'] == 'More than two':
                list_recommendations.append("Cramer's V")
        
        #at least one ordinal
        elif dict_inputs['nature_of_variables_of_interest'] == 'At least one ordinal':
            list_recommendations.append("Kendall's Tau")
            list_recommendations.append("Spearman's Rho")

        #one binary and one continuous
        elif dict_inputs['nature_of_variables_of_interest'] == 'One binary and one continuous':
            list_recommendations.append("Point biserial correlation")
        else:
            pass
    else:
        pass
    
    return list_recommendations
"""

#----------------------------------
#<<< CURRENT WORKING ON >>>
#----------------------------------
#----------------------------------
#<<< SECOND ATTEMPT! >>>>
#----------------------------------

def recommend_test(dict_inputs):
    """
    still to do with this function:
    Need to check the naming conventions of the user inputs both in terms of 
    how they are displayed to the user, as well as their variable naming
    also check the input strings in the inputs function align with the logic in this function.
    if not, amend input strings to align. 
    check this against the logic flow chart to ensure aligns semantically
    then check all logic for recommendations is as required with the correct
    test(s) being suggested in each circumstance.
    """
    list_recommendations = []

    #Differences or Goodness of fit
    #proportion or categorical variable of interest path
    if dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':
        list_recommendations.append('Exact test of Goodness of Fit')

    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
        list_recommendations.append('One-proportion z-test')

    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':
        list_recommendations.append('G-test of Goodness of Fit')

    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':
        list_recommendations.append('Exact test of Goodness of Fit (multinomial model)')

    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
        list_recommendations.append('Chi-square goodness of fit')

    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':
        list_recommendations.append('G-test of Goodness of Fit')

    #two group variables path | two levels/options
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':    
        list_recommendations.append('Fischers Exact test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':    
        list_recommendations.append('Two proportion z-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell and more than 1000 in total':    
        list_recommendations.append('G-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'Two' and dict_inputs['sample_relationship'] == 'Paired':    
        list_recommendations.append('McNemars test')

    #two group variables path | more than two levels/options
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['sample_size_per_cell'] == 'Less than 10 in a cell':    
        list_recommendations.append('Fischers Exact test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['sample_size_per_cell'] == 'More than 10 in every cell':
        list_recommendations.append('Chi-square test of independence')
    
#!!  #TODO: Need to add logic to input function to ensure the option of "More than 1000 total" comes up when applicable to filter to this test option
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['sample_size_per_cell'] == 'More than 1000 in total':
        list_recommendations.append('G-test')

    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['number_of_levels'] == 'More than two' and dict_inputs['sample_relationship'] == 'Paired':    
        list_recommendations.append('McNemars test')
    
    #More than two group variables path
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Nominal', 'Ordinal'] and dict_inputs['number_of_samples'] == 'More than two':
        list_recommendations.append('Log-linear analysis')
    
    #continuous variable of interest path
    #One sample/group
#!! #TODO: change dict_inputs['normal_dist'] options to be "Yes and population variance known", "Yes but population variance not known", "No"
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['population_variance_known'] == 'Yes':
        list_recommendations.append('Single sample Z-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['population_variance_known'] == 'No':
        list_recommendations.append('Single sample T-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'One' and dict_inputs['normal_dist'] == 'No':
        list_recommendations.append('Single sample wilcoxon signed-rank test')

    #Two samples/groups
    #independent
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['population_variance_known'] == 'Yes':
        list_recommendations.append('Independent samples Z-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['population_variance_known'] == 'No':
        list_recommendations.append('Independent samples T-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'No':
        list_recommendations.append('Mann-Whitney U Test')

    #Paired
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['sample_relationship'] == 'Paired' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['population_variance_known'] == 'Yes':
        list_recommendations.append('Paired samples Z-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['sample_relationship'] == 'Paired' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['population_variance_known'] == 'No':
        list_recommendations.append('Paired samples T-test')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'Two' and dict_inputs['sample_relationship'] == 'Paired' and dict_inputs['normal_dist'] == 'No':
        list_recommendations.append('Wilcoxon signed-rank test')

    #Three or more samples/groups
    #INDEPENDENT
    #normal dist
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['numer_group_variables'] == 'One':
        list_recommendations.append('One-way ANOVA')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['numer_group_variables'] == 'One with a covariate':
        list_recommendations.append('One-way ANCOVA')

#!! #TODO: Change "multiple independent variables" option to "Two or more"
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['numer_group_variables'] == 'Two or more':
        list_recommendations.append('Factorial ANOVA')

    #not normal dist
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Independent' and dict_inputs['normal_dist'] == 'No':
        list_recommendations.append('Kruskal-Wallis')
        list_recommendations.append('One-way ANOVA')


    #PAIRED
    #Normal
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Paired' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['numer_group_variables'] == 'One':
        list_recommendations.append('One-way Repeated Measures ANOVA')
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Paired' and dict_inputs['normal_dist'] == 'Yes' and dict_inputs['numer_group_variables'] == 'Two or more':
        list_recommendations.append('Split plot ANOVA')
    #Not normal
    elif dict_inputs['hypothesis_type'] == 'Differences or Goodness of fit' and dict_inputs['data_type'] in ['Interval', 'Ratio'] and dict_inputs['number_of_samples'] == 'More than two' and dict_inputs['sample_relationship'] == 'Paired' and dict_inputs['normal_dist'] == 'No':
        list_recommendations.append('Friedman test')
    
    
    #RELATIONSHIP BRANCH
    #Two continuous
    elif dict_inputs['nature_of_variables_of_interest'] == 'Two continuous variables' and dict_inputs['covariates_present'] == 'Yes':
        list_recommendations.append('Partial correlation')
    elif dict_inputs['nature_of_variables_of_interest'] == 'Two continuous variables' and dict_inputs['covariates_present'] == 'No':
        list_recommendations.append('Pearson correlation')
    
    #Two categorical
    elif dict_inputs['nature_of_variables_of_interest'] == 'Two categorical variables' and dict_inputs['number_of_levels'] == 'Two':
        list_recommendations.append('Phi co-efficient')
    elif dict_inputs['nature_of_variables_of_interest'] == 'Two categorical variables' and dict_inputs['number_of_levels'] == 'More than two':
        list_recommendations.append("Cramer's V")
    
    #at least one ordinal
    elif dict_inputs['nature_of_variables_of_interest'] == 'At least one ordinal variable':
        list_recommendations.append("Kendall's Tau")
        list_recommendations.append("Spearman's Rho")
    
    #one continuous one binary
    elif dict_inputs['nature_of_variables_of_interest'] == 'One binary and one continuous variable':
        list_recommendations.append("Point biserial correlation")
       
    return list_recommendations



def render_inputs():
    
    hypothesis_type = None
    data_type = None
    number_of_samples = None
    is_normally_distributed = None
    population_variance_known = None
    sample_relationship = None
    numer_group_variables = None #was num_variables
    nature_of_variables_of_interest = None
    number_of_levels = None
    covariates_present = None
    sample_size_per_cell = None
    num_group_variables = None

    with st.expander('Click to enter data and test parameters'):
        default_option = '---'
        col1, col2 = st.columns(2)
        with col1:
            hypothesis_type = st.selectbox(
                label='Type of hypothesis',
                options= [default_option,
                    'Differences or Goodness of fit',
                    'Relationship'
                ])
        
        if hypothesis_type != 'Relationship':
            with col2:    
                data_type = st.selectbox(
                    label='What is the data type?',
                    options=[default_option,'Nominal', 'Ordinal', 'Interval', 'Ratio'],
                    help="""Data types reflect different levels of measurement:
                            \n- **Nominal:** Categories without a natural order. Example: Types of viruses (Influenza, Coronavirus, Rhinovirus).
                            \n- **Ordinal:** Categories with a natural order but not evenly spaced. Example: Stages of cancer (Stage I, II, III, IV).
                            \n- **Interval:** Numeric scales with equal spacing but no true zero point. Example: Temperature in Celsius when measuring fever.
                            \n- **Ratio:** Numeric scales with a true zero point. Example: Dosage of medication in milligrams.""")

            number_of_samples = st.selectbox(
                "How many samples are there in your dataset?",
                [default_option, 'One', 'Two', 'More than two'],
                help="""This refers to the number of distinct data groups or sets you are analyzing. 
                        \n- **'One'** means analyzing data from a single group.
                        \n- **'Two'** means comparing data between two groups, e.g., a control group and a treatment group in a clinical trial.
                        \n- **'More than two'** means comparing data across multiple groups, e.g., testing multiple treatments in a clinical study."""
            )

            if data_type in ['Nominal', 'Ordinal']:

                if number_of_samples == 'One':
                    number_of_levels = st.selectbox(
                        "Number of unique levels or values per variable:",
                        [default_option,'Two', 'More than two'],)
                
                    sample_size_per_cell = st.selectbox(
                        "How many observations are there in each cell (e.g. for each option):",
                        [default_option,'Less than 10 in a cell', 'More than 10 in every cell', 'More than 10 in every cell and more than 1000 in total'],)

                if number_of_samples == 'Two':
                    number_of_levels = st.selectbox(
                        "How many options (unique labels) are there in a group?",
                        [default_option,'Two', 'More than two'],)


                    sample_relationship = st.selectbox(
                            "Are the samples independent?",
                            [default_option, 'Independent', 'Paired'],
                            help="""Samples are 'independent' if the data groups do not influence each other and are not related. 
                                    \nExample of independent samples: Comparing the incidence of flu in different regions. 
                                    \nSamples are not independent (i.e., dependent or paired) if the groups are related, such as pre- and post-treatment cholesterol levels in the same patients."""
                        )
                    
                    if number_of_levels == 'Two' and sample_relationship == 'Independent':
                        sample_size_per_cell = st.selectbox(
                        "How many observations are there in each cell (e.g. for each option):",
                        [default_option,'Less than 10 in a cell', 'More than 10 in every cell', 'More than 10 in every cell and more than 1000 in total'],)
                    
                    elif number_of_levels == 'More than two' and sample_relationship == 'Independent':
                        sample_size_per_cell = st.selectbox(
                        "How many observations are there in each cell (e.g. for each option):",
                        [default_option,'Less than 10 in a cell', 'More than 10 in every cell', 'More than 1000 in total'],)

            #continuous data type branch
            else:
                if number_of_samples == 'One':
                    is_normally_distributed = st.selectbox(
                                "Is the data normally distributed?",
                                [default_option, 'Yes', 'No'],
                                help="""'Normally distributed' refers to data that follows a normal distribution (bell-shaped curve). 
                                        \nMethods to assess normality include visual methods like histograms and Q-Q plots, or statistical tests like the Shapiro-Wilk test (small samples) and the Kolmogorov-Smirnov test (large samples). 
                                        \nExample: Checking normality in the distribution of systolic blood pressure readings across a population."""
                            )
                    
                    if is_normally_distributed == 'Yes':
                        population_variance_known = st.selectbox(
                        label='Is the population variance known?',
                        options=[default_option, 'Yes', 'No']
                        )
                
                elif number_of_samples == 'Two':
                    sample_relationship = st.selectbox(
                            "Are the samples independent?",
                            [default_option, 'Independent', 'Paired'],
                            help="""Samples are 'independent' if the data groups do not influence each other and are not related. 
                                    \nExample of independent samples: Comparing the incidence of flu in different regions. 
                                    \nSamples are not independent (i.e., dependent or paired) if the groups are related, such as pre- and post-treatment cholesterol levels in the same patients."""
                        )
                    
                    is_normally_distributed = st.selectbox(
                            "Is the data normally distributed?",
                            [default_option, 'Yes', 'No'],
                            help="""'Normally distributed' refers to data that follows a normal distribution (bell-shaped curve). 
                                    \nMethods to assess normality include visual methods like histograms and Q-Q plots, or statistical tests like the Shapiro-Wilk test (small samples) and the Kolmogorov-Smirnov test (large samples). 
                                    \nExample: Checking normality in the distribution of systolic blood pressure readings across a population."""
                        )
                    
                    if is_normally_distributed == 'Yes':
                        if is_normally_distributed == 'Yes':
                            population_variance_known = st.selectbox(
                                label='Is the population variance known?',
                                options=[default_option, 'Yes', 'No']
                                )
                
                elif number_of_samples == 'More than two':
                    sample_relationship = st.selectbox(
                            "Are the samples independent?",
                            [default_option, 'Independent', 'Paired'],
                            help="""Samples are 'independent' if the data groups do not influence each other and are not related. 
                                    \nExample of independent samples: Comparing the incidence of flu in different regions. 
                                    \nSamples are not independent (i.e., dependent or paired) if the groups are related, such as pre- and post-treatment cholesterol levels in the same patients."""
                        )
                    
                    is_normally_distributed = st.selectbox(
                            "Is the data normally distributed?",
                            [default_option, 'Yes', 'No'],
                            help="""'Normally distributed' refers to data that follows a normal distribution (bell-shaped curve). 
                                    \nMethods to assess normality include visual methods like histograms and Q-Q plots, or statistical tests like the Shapiro-Wilk test (small samples) and the Kolmogorov-Smirnov test (large samples). 
                                    \nExample: Checking normality in the distribution of systolic blood pressure readings across a population."""
                        )
                
                    if is_normally_distributed == 'Yes':
                        numer_group_variables = st.selectbox(
                            "How many group variables are there?",
                            [default_option, 'One', 'Two or more'],
                        )

        #relationship path
        if hypothesis_type == 'Relationship':
            nature_of_variables_of_interest = st.selectbox(
                "What is the nature of the variables of interest?",
                (default_option, 'Two continuous variables', 'Two categorical variables', 'At least one ordinal variable', 'One binary and one continuous variable'),
            )

            if nature_of_variables_of_interest == 'Two continuous variables':
                covariates_present = st.selectbox(
                "Are covariates present?",
                [default_option, 'Yes', 'No'],
            )

            elif nature_of_variables_of_interest == 'Two categorical variables':
                number_of_levels = st.selectbox(
                "How many values per variable?",
                [default_option, 'Two', 'More than two'],
            )

    dict_inputs = {
        'data_type': data_type, 
        'normal_dist': is_normally_distributed, 
        'number_of_samples': number_of_samples, 
        'sample_relationship': sample_relationship, 
        'hypothesis_type': hypothesis_type,
        'population_variance_known': population_variance_known,
        'nature_of_variables_of_interest': nature_of_variables_of_interest,
        'numer_group_variables': numer_group_variables, #was num_variables
        'number_of_levels': number_of_levels,
        'covariates_present': covariates_present,
        'sample_size_per_cell': sample_size_per_cell,
        'num_group_variables': num_group_variables
    }

    return dict_inputs



 


#Diffs or goodness of fit | Nominal or Ordinal data | One sample/group | Two levels | sample size < 10 per cell 
'Exact test of Goodness of Fit'
#Diffs or goodness of fit | Nominal or Ordinal data | One sample/group | Two levels | sample size > 10 per cell 
'One-proportion z-test'
#Diffs or goodness of fit | Nominal or Ordinal data | One sample/group | Two levels | sample size > 10 per cell & > 1000 total
'G-test of Goodness of Fit'
#Diffs or goodness of fit | Nominal or Ordinal data | One sample/group | More than two levels | sample size < 10 per cell
'Exact test of Goodness of Fit (multinomial model)'
#Diffs or goodness of fit | Nominal or Ordinal data | One sample/group | More than two levels | sample size > 10 per cell
'Chi-square goodness of fit'
#Diffs or goodness of fit | Nominal or Ordinal data | One sample/group | More than two levels | sample size > 10 per cell & > 1000 total
'G-test of Goodness of Fit'
#Diffs or goodness of fit | Nominal or Ordinal data | Two samples/groups | Two levels | Independent samples | sample size < 10 per cell
'Fischers Exact test'
#Diffs or goodness of fit | Nominal or Ordinal data | Two samples/groups | Two levels | Independent samples | sample size > 10 per cell
'Two proportion z-test'
#Diffs or goodness of fit | Nominal or Ordinal data | Two samples/groups | Two levels | Independent samples | sample size > 10 per cell & > 1000 total
'G-test'
#Diffs or goodness of fit | Nominal or Ordinal data | Two samples/groups | Two levels | Paired samples
'McNemars test'
#Diffs or goodness of fit | Nominal or Ordinal data | Two samples/groups | More than two levels | Independent samples | sample size < 10 per cell
'Fischers Exact test'
#Diffs or goodness of fit | Nominal or Ordinal data | Two samples/groups | More than two levels | Independent samples | sample size > 10 per cell
'Chi-square test of independence'
#Diffs or goodness of fit | Nominal or Ordinal data | Three samples/groups
'Log-linear analysis'
#Diffs or goodness of fit | Interval or ratio data | One sample/group | normal dist | known pop var
'Single sample Z-test'
#Diffs or goodness of fit | Interval or ratio data | One sample/group | normal dist | unknown pop var
'Single sample T-test'
#Diffs or goodness of fit | Interval or ratio data | One sample/group | not normal dist
'Single sample wilcoxon signed-rank test'
#Diffs or goodness of fit | Interval or ratio data | Two samples/groups | Independent samples | normal dist | known pop var
'Independent samples Z-test'
#Diffs or goodness of fit | Interval or ratio data | Two samples/groups | Independent samples | normal dist | unknown pop var
'Independent samples T-test'
#Diffs or goodness of fit | Interval or ratio data | Two samples/groups | Independent samples | not normal dist 
'Mann-Whitney U Test'
#Diffs or goodness of fit | Interval or Ratio data | Two samples/groups | paired samples | normal dist | known pop var 
'Paired samples Z-test'
#Diffs or goodness of fit | Interval or Ratio data | Two samples/groups | paired samples | normal dist | unknown pop var 
'Paired samples T-test'
#Diffs or goodness of fit | Interval or Ratio data | Two samples/groups | paired samples | not normal dist 
'Wilcoxon signed-rank test'
#Diffs or goodness of fit | Interval or Ratio data | More than two samples/groups | Independent samples | normal dist | one variable
'One-way ANOVA'
#Diffs or goodness of fit | Interval or Ratio data | More than two samples/groups | Independent samples | normal dist | one variable with a covariate
'One-way ANCOVA'
#Diffs or goodness of fit | Interval or Ratio data | More than two samples/groups | Independent samples | normal dist | Multiple independent variables
'Factorial ANOVA'
#Diffs or goodness of fit | Interval or Ratio data | More than two samples/groups | Independent samples | not normal dist
'Kruskal-Wallis'
'One-way ANOVA'


#relationship hypotheses
#Relationship | Two continuous variables of interest | covariates present
'Partial correlation'
#Relationship | Two continuous variables of interest | covariates not present
'Pearson correlation'
#Relationship | Two categorical variables of interest | two unique values per variable
'Phi co-efficient'
#Relationship | Two categorical variables of interest | more than two unique values per variable
"Cramer's V"
#Relationship | At least one ordinal variable of interest
"Kendall's Tau"
"Spearman's Rho"
#Relationship | One binary and one continuous variable of interest
"Point biserial correlation"


