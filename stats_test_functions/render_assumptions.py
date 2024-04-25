
#imports
import streamlit as st


#parametric test modules
from stats_test_functions import paired_t_test
from stats_test_functions import independent_t_test
from stats_test_functions import repeated_measures_anova_v1
from stats_test_functions import anova_test
from stats_test_functions import one_sample_t_test
from stats_test_functions import pearson_correlation
from stats_test_functions import chi_square_goodness_of_fit as chi_gof
from stats_test_functions import chi_square_test_of_independence as chi_toi
from stats_test_functions import fishers_exact_test as fishers_et
from stats_test_functions import mcnemars_test as mcnt
from stats_test_functions import kruskal_wallis_test as kwt
from stats_test_functions import independent_samples_z_test as izt
from stats_test_functions import one_sample_z_test as ozt


#-----------------------------------------
def render_assumptions_for_selected_test(selected_recommended_test, df):
    """
    Returns a dictionary containing references to functions for each test, which 
    themselves render the assumptions for the given test in the app display.
    Where assumption functions are not yet built, this is hard coded to default to 
    placeholder text. 

    Returns:
    Bool value to confirm whether the assumptions have been met for the test in scope. 
    This can then be used to either allow the intended to test to proceed, or 
    direct the user to the non-parametric alternatve (for example)
    """

    placeholder_text = f'Functions to check assumptions of {selected_recommended_test} not yet incorporated'

    #logic to render the required assumptions for the test in scope:

    if selected_recommended_test == 'Chi-square goodness of fit':
        test_assumptions_met = chi_gof.render_chi_square_goodness_of_fit_test_checks(df)
    
    elif selected_recommended_test == 'Chi-square test of independence': 
        test_assumptions_met = chi_toi.render_chi_square_test_of_independence_checks(df)
    
    elif selected_recommended_test == "Cramer's V": 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Exact test of Goodness of Fit (multinomial model)': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Exact test of Goodness of Fit': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Factorial ANOVA': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Fischers Exact test': 
        test_assumptions_met = fishers_et.render_assumption_checks_for_fishers_exact_test(df)
    
    elif selected_recommended_test == 'G-test of Goodness of Fit': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'G-test': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Independent samples T-test': 
        test_assumptions_met = independent_t_test.render_assumption_checks_for_independent_t_test(df)
    
    elif selected_recommended_test == 'Independent samples Z-test': 
        test_assumptions_met = izt.render_assumption_checks_for_independent_z_test(df)
    
    elif selected_recommended_test == "Kendall's Tau": 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Kruskal-Wallis': 
        test_assumptions_met = kwt.render_assumption_checks_for_kruskal_wallis_test(df)
    
    elif selected_recommended_test == 'Log-linear analysis': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Mann-Whitney U Test': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'McNemars test': 
        test_assumptions_met = mcnt.render_assumption_checks_for_mcnemars_test(df)
    
    elif selected_recommended_test == 'One-proportion z-test': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'One-way ANCOVA': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'One-way ANOVA': 
        group_column, value_column = anova_test.select_columns_for_anova_test(df)
        test_assumptions_met = anova_test.render_anova_checks(df, group_column, value_column)
    
    elif selected_recommended_test == 'Paired samples T-test': 
        test_assumptions_met = paired_t_test.render_assumption_checks_for_paired_t_test(df)
    
    elif selected_recommended_test == 'Paired samples Z-test': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Partial correlation': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Pearson correlation': 
        test_assumptions_met = pearson_correlation.render_assumption_checks_for_pearson_correlation(df)
    
    elif selected_recommended_test == 'Phi co-efficient': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == "Point biserial correlation": 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Single sample T-test': 
        selected_column = one_sample_t_test.select_column_for_one_sample_t_test(df),
        test_assumptions_met = one_sample_t_test.render_one_sample_t_test_checks(df, selected_column[0])
        
    elif selected_recommended_test == 'Single sample wilcoxon signed-rank test': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Single sample Z-test': 
        test_assumptions_met = ozt.render_assumption_checks_for_independent_z_test(df)
    
    elif selected_recommended_test == "Spearman's Rho": 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Two proportion z-test': 
        st.write(placeholder_text)
    
    elif selected_recommended_test == 'Wilcoxon signed-rank test': 
        st.write(placeholder_text)

    return test_assumptions_met #need to update all assumptions functions to return a bool if the assumptions are met


#---------------------------------------------------

def get_alternative_test(test_name):

    placeholder_text = f'An alternative test for {test_name} has not been incorporated yet'

    dict_alternative_test_names = {
    'Chi-square goodness of fit': placeholder_text,
    'Chi-square test of independence': 'Fischers Exact test',
    "Cramer's V": placeholder_text,
    'Exact test of Goodness of Fit (multinomial model)': placeholder_text,
    'Exact test of Goodness of Fit': placeholder_text,
    'Factorial ANOVA': placeholder_text,
    'Fischers Exact test': 'Chi-square test of independence',
    'G-test of Goodness of Fit': placeholder_text,
    'G-test': placeholder_text,
    'Independent samples T-test': placeholder_text,
    'Independent samples Z-test': 'Please see error message above.', #3 possible alternatives.. User given message if assumptions not met to inform their decision.
    "Kendall's Tau": placeholder_text,
    'Kruskal-Wallis': placeholder_text,
    'Log-linear analysis': placeholder_text,
    'Mann-Whitney U Test': placeholder_text,
    'McNemars test': placeholder_text,
    'One-proportion z-test': placeholder_text,
    'One-way ANCOVA': placeholder_text,
    'One-way ANOVA': placeholder_text,
    'Paired samples T-test': 'Wilcoxon signed-rank test',
    'Paired samples Z-test': placeholder_text,
    'Partial correlation': placeholder_text,
    'Pearson correlation': "Spearman's Rho", #done 
    'Phi co-efficient': placeholder_text,
    "Point biserial correlation": placeholder_text,
    'Single sample T-test': 'Wilcoxon signed-rank test', #done
    'Single sample wilcoxon signed-rank test': placeholder_text,
    'Single sample Z-test': 'Single sample wilcoxon signed-rank test',
    "Spearman's Rho": placeholder_text,
    'Two proportion z-test': placeholder_text,
    'Wilcoxon signed-rank test': placeholder_text,
    }

    alt_test = dict_alternative_test_names[test_name]

    return alt_test
