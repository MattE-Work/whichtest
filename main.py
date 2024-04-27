#import functions
from functions import functions as func
from stat_test_explanations import stat_test_explanations as st_exp
from stats_test_functions import stats_tests as stat_tests
from stats_test_functions import dummy_data_creator as dummy_data

#import decision tree and user input module
from functions import stat_test_decision_tree

#import module to render assumptions for the selected test
from stats_test_functions import render_assumptions

#parametric test modules
#from stats_test_functions import paired_t_test
#from stats_test_functions import independent_t_test
#from stats_test_functions import repeated_measures_anova_v1
#from stats_test_functions import anova_test
#from stats_test_functions import one_sample_t_test
#from stats_test_functions import pearson_correlation
#from stats_test_functions import chi_square_test_of_independence as chi_toi
#from stats_test_functions import chi_square_goodness_of_fit as chi_gof

#import libraries
import streamlit as st
import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns

#start code
st.set_page_config(page_icon='🔍', layout='wide')

#list of tests in scope - status: 12 / 31 complete ! 
stats_test_options = { 
    'Chi-square goodness of fit': 'done', #done
    'Chi-square test of independence': 'done', #done
    "Cramer's V": 'To do',
    'Exact test of Goodness of Fit (multinomial model)': 'To do',
    'Exact test of Goodness of Fit': 'To do',
    'Factorial ANOVA': 'To do',
    'Fischers Exact test': 'done', #done
    'G-test of Goodness of Fit': 'To do',
    'G-test': 'To do',
    'Independent samples T-test': 'done', #done
    'Independent samples Z-test': 'done', #done
    "Kendall's Tau": 'To do',
    'Kruskal-Wallis': 'done', #done (but needs alternative test logic adding - as is, if assumptions not met, logic stops and nothing else to try)
    'Log-linear analysis': 'To do',
    'Mann-Whitney U Test': 'To do', 
    'McNemars test': 'done', #done
    'One-proportion z-test': 'To do',
    'One-way ANCOVA': 'To do',
    'One-way ANOVA': 'done', #done
    'Paired samples T-test': 'done', #done
    'Paired samples Z-test': 'done', #done
    'Partial correlation': 'To do',
    'Pearson correlation': 'done', #done 
    'Phi co-efficient': 'To do',
    "Point biserial correlation": 'To do',
    'Single sample T-test': 'done', #done
    'Single sample wilcoxon signed-rank test': 'To do',
    'Single sample Z-test': 'done', #done
    "Spearman's Rho": 'To do',
    'Two proportion z-test': 'To do',
    'Wilcoxon signed-rank test': 'To do',
}

#subset from the dictionary above to a list of those tests that are recorded as having been built
stats_test_options_subset = [key for key, value in stats_test_options.items() if value == 'done']

st.title(':blue[Which Stats Test?]')
col1, col2, col3 = st.columns(3)
with col1:
    load_dummy_data = st.radio(label='Load dummy data to test the tool?', options=['Yes', 'No'], horizontal=True, index=1)
with col2:
    debug_mode = st.radio(label='Turn on debug mode?', options=['Yes', 'No'], horizontal=True, index=1)
with col3:
    filter_to_just_completed_tests = st.radio(label=f'Only inc. the {len(stats_test_options_subset)} built tests?', options=['Yes', 'No'], horizontal=True, index=1)

#determine whether to subset the pick-list to just the tests that are built
if filter_to_just_completed_tests =='Yes':
    stats_test_options = stats_test_options_subset
else:
    stats_test_options = [key for key in stats_test_options.keys()]


how_to_use_tool = st.selectbox(
    label='How do you want to use this tool?',
    options=[
        'Select a test from the list',
        'Have the tool suggest the test to use'
    ]
)

if how_to_use_tool != 'Select a test from the list':

    #Render user inputs
    dict_inputs = stat_test_decision_tree.render_inputs()

    #Use inputs to determine recommended stats test(s)
    list_recommendations = stat_test_decision_tree.recommend_test(dict_inputs)

    if debug_mode == 'Yes':
        col1, col2 = st.columns(2)
        with col1:
            st.write(dict_inputs)
        with col2:
            st.write(list_recommendations)

    st.header(':blue[Recommended Stats Test(s):]')

else:
    st.header(':blue[Select the stats test to use:]')
# ----------------------------

if how_to_use_tool != 'Select a test from the list':
    selected_recommended_test = st.selectbox(label='Select the recommended test to use', options=list_recommendations, index=0)

#Select test to use from the list
else:
    selected_recommended_test = st.selectbox(label='Select the recommended test to use', options=stats_test_options, index=0)


#list_selected_recommended_test = []
#list_selected_recommended_test.append(selected_recommended_test)

try:
    dict_test_explanations = st_exp.get_dict_test_explanation(selected_recommended_test)
except:
    st.write('The assumption checks for this test have not been built yet 😞, please select a different test from the list above 🙄. To filter the selection list to just tests that do have assumption checks built (and no longer see this message 😉), use the radio buttons to the top right 👆🏻👉🏻')
    st.stop()

#st.subheader(test_name_for_expander)
with st.expander(f"Click for information about this test"):
    tab_keys = dict_test_explanations.keys()  # Get all keys which are tab names like 'Explanation', 'Requirements', etc.
    tabs = st.tabs([key for key in tab_keys])  # Create a tab for each key

    for tab, key in zip(tabs, tab_keys):
        with tab:
            if key != 'video':
                st.write(dict_test_explanations[key])  # Display the content under each tab corresponding to the key
            elif "youtu" in dict_test_explanations[key]:
                width=40
                side = max((100 - width) / 2, 0.01)

                #st.video(test_details[key])
                _, container, _ = st.columns([side, width, side])
                container.video(data=dict_test_explanations[key])
            else:
                st.write(f"""A video isn't incorporated for this test yet. 
                Please refer to the url below for more information about this test:
                \n{dict_test_explanations[key]}""")

# ----------------------------


#--------------------------------------------
st.header(':blue[Select your data]')

df_location = st.file_uploader("Select the file containing your data you wish to run through the appropriate stats test", type=['csv', 'xlsx'])
dummy_data.expected_data_structure_examples(selected_recommended_test)

if df_location is None and load_dummy_data != 'Yes':
    st.stop()

if load_dummy_data == 'Yes':
    #produce dummy data
    df = dummy_data.get_dummy_data_for_tests(selected_recommended_test)

    #advise user dummy data in use
    st.write(':red[**Debug mode on and dummy data in use**]')

else:
    df = pd.DataFrame(df_location)



st.header(':blue[Checking assumptions...]')

#--------------------------------------------



#display the test(s) applicable based on the inputs provided, along with any prior assumption checks before running the test, if applicable

#CONTINUE FROM HERE
#DEV SECTION - Working on chi square goodness of fit test


#test_bool = pzt.render_assumption_checks_for_paired_z_test(df)

#--------------------------------

try:
    test_bool_result = render_assumptions.render_assumptions_for_selected_test(selected_recommended_test, df)
    if test_bool_result == None:
        st.write('Make the required selections using the drop down boxes above')
        st.stop()
except:
    st.write('Make the required selections using the drop down boxes above')
    st.stop()

if test_bool_result == False:
    alt_test = render_assumptions.get_alternative_test(selected_recommended_test)
    st.write(f":red[Recommend using the alternative test: **{alt_test}**]")
    selected_recommended_test = alt_test


#Identify the index of the recommended list. Use this later to default the test confirmation 
#to the recommended test

try:
    recommended_test_index = stats_test_options.index(selected_recommended_test)
    
except:
    st.stop()

#if "Paired t-test (for normally distributed data)" in list_selected_recommended_test:
#    normal_dist_can_use_paired_t = paired_t_test.render_assumption_checks_for_paired_t_test(df)
    
#elif "Independent t-test (for normally distributed data)" in list_selected_recommended_test:
#    independent_t_test.render_assumption_checks_for_independent_t_test(df)

#elif "Repeated measures ANOVA (for normally distributed data)" in list_selected_recommended_test:
#    rm_anova_assumptions_met = repeated_measures_anova_v1.render_assumption_checks_for_repeated_measures_anova(df)

#elif "ANOVA (for normally distributed data)" in list_selected_recommended_test:
#    group_column, value_column = anova_test.select_columns_for_anova_test(df)
    
#elif 'One-sample t-test' in list_selected_recommended_test:
#    selected_column = one_sample_t_test.select_column_for_one_sample_t_test(df)
    
#    one_sample_t_test_assumptions_met = one_sample_t_test.render_one_sample_t_test_checks(df, selected_column)
#    if one_sample_t_test_assumptions_met == False:
#        alternative = ' Wilcoxon Signed-Rank Test' #TODO add creation of alternative variable to all other test checks above to simplify decision making for running the test (e.g. confirm run original suggestion, or, default to alternative)

#elif 'Pearson Correlation (for normally distributed data)' in list_selected_recommended_test:
    #render pearson correlation assumptions
    #pearson_correlation.display_pearson_correlation_assumptions()
    
    #user selects columns 1 and 2
    #selected_column_1, selected_column_2 = pearson_correlation.select_two_columns_for_pearson_correlation_test(df)
    
    #check normality assumption - Q-Q plot
    #pearson_correlation.check_normality_qqplot_altair(df, selected_column_1, selected_column_2)
    
    #check normality assumption - shapiro wilk plot
    #dict_shapiro_wilk_check_for_each_variable = pearson_correlation.check_normality_pearson_correlation_shapiro(df, selected_column_1, selected_column_2)

    #visualise linearity check
    #pearson_correlation.check_linearity_scatter_plot(df, selected_column_1, selected_column_2)

    #check homoscedascity
    #pearson_correlation.check_homoscedasticity(df, selected_column_1, selected_column_2)

    #user confirm interpretation:
    #pearson_correlation.check_assumptions_and_recommend_test(dict_shapiro_wilk_check_for_each_variable)

#    proceed_with_pearson_correlation = pearson_correlation.render_assumption_checks_for_pearson_correlation(df)
#    if proceed_with_pearson_correlation == False:
#        alternative = "Spearman's rank correlation coefficient"



#--------------------------------------------
#Section TODO to enable selecting the relevant test

st.title('Confirm which stat test to use')

#user input to confirm chosen test
selected_test = st.selectbox(label='Select the test to use', options = stats_test_options, index=recommended_test_index)

#--------------------------------------------

#section TODO to incorporate running the selected test.

button = st.button('Run selected stats test')
if button:
    pass
else:
    st.stop()

#--------------------------------------------

if debug_mode == 'Yes':
    st.title('Debug section beneath this point')

    st.subheader(':blue[Testing all combinations of inputs:]')
    from itertools import product

    # Define the options for each input parameter with logical conditions
    data_types = ['Nominal', 'Ordinal', 'Interval', 'Ratio']
    distribution_statuses = {
        'Nominal': ['Not Applicable'],  # Normal distribution does not apply to nominal data
        'Ordinal': ['Not Applicable'],  # Normal distribution does not apply to ordinal data
        'Interval': ['Yes', 'No', 'Unknown'],
        'Ratio': ['Yes', 'No', 'Unknown']
    }
    sample_numbers = ['One', 'Two', 'More than two']
    sample_relationships = {
        'One': ['Not Applicable'],  # Sample relationship does not apply when there's only one sample
        'Two': ['Independent', 'Not Independent'],
        'More than two': ['Independent', 'Not Independent']
    }
    num_variables_options = {
        'One': ['One variable', 'Two variables'],  # 'More than two variables' removed based on context
        'Two': ['Not Applicable'],  # num_variables does not apply to more than one sample
        'More than two': ['Not Applicable']
    }

    # Generate all possible logical combinations of these parameters
    all_combinations = []
    for data_type in data_types:
        for dist_status in distribution_statuses[data_type]:
            for num_samples in sample_numbers:
                for sample_rel in sample_relationships[num_samples]:
                    if num_samples == 'One':
                        # Special rules for one sample
                        for num_vars in num_variables_options[num_samples]:
                            if num_vars == 'One variable':
                                hypo_type = 'Differences'  # Only differences make sense with one variable
                            else:
                                hypo_type = 'Associations'  # Only associations make sense with two variables
                            all_combinations.append(
                                (data_type, dist_status, num_samples, sample_rel, hypo_type, num_vars)
                            )
                    else:
                        # Standard rules for two or more samples
                        for hypo_type in ['Differences', 'Associations']:
                            for num_vars in num_variables_options[num_samples]:
                                all_combinations.append(
                                    (data_type, dist_status, num_samples, sample_rel, hypo_type, num_vars)
                                )

    # Create a dictionary to hold these combinations with detailed keys
    combinations_dict = {}
    for i, combo in enumerate(all_combinations, 1):
        recommendations, recommendations_keys = func.recommend_test(combo[0], combo[1], combo[2], combo[3], combo[4], combo[5])
        combinations_dict[f"combination_{i}"] = {
            'data_type': combo[0],
            'is_normally_distributed': combo[1],
            'number_of_samples': combo[2],
            'sample_relationship': combo[3],
            'hypothesis_type': combo[4],
            'Number Variables': combo[5],
            'recommended test': recommendations
        }

    df_unique_combinations = pd.DataFrame(combinations_dict).T
    st.dataframe(df_unique_combinations)

    unique_tests = set()
    for tests in df_unique_combinations['recommended test']:
        unique_tests.update(tests)  # Add all tests from each list to the set
    
    unique_tests_list = sorted(unique_tests)
    # Display the unique tests
    st.subheader('Unique Recommended Tests:')
    st.write(list(unique_tests_list))

