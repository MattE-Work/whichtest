#import functions
from functions import functions as func
from stat_test_explanations import stat_test_explanations as st_exp

#import libraries
import streamlit as st
import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns

#start code
st.set_page_config(page_icon='🔍', layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.title(':blue[Which Stats Test?]')
with col2:
    debug_mode = st.radio(label='Turn on debug mode?', options=['Yes', 'No'], horizontal=True, index=1)

# User inputs
# User inputs with explanations

col1, col2 = st.columns(2)
with col1:
    data_type = st.radio(
        "What is the data type?",
        ('Nominal', 'Ordinal', 'Interval', 'Ratio'),
        horizontal=True,
        help="""Data types reflect different levels of measurement:
                \n- **Nominal:** Categories without a natural order. Example: Types of viruses (Influenza, Coronavirus, Rhinovirus).
                \n- **Ordinal:** Categories with a natural order but not evenly spaced. Example: Stages of cancer (Stage I, II, III, IV).
                \n- **Interval:** Numeric scales with equal spacing but no true zero point. Example: Temperature in Celsius when measuring fever.
                \n- **Ratio:** Numeric scales with a true zero point. Example: Dosage of medication in milligrams."""
    )

    with col2:
        if data_type == 'Interval' or data_type == 'Ratio':
            is_normally_distributed = st.radio(
                "Is the data normally distributed?",
                ('Yes', 'No', 'Unknown'),
                horizontal=True,
                help="""'Normally distributed' refers to data that follows a normal distribution (bell-shaped curve). 
                        \nMethods to assess normality include visual methods like histograms and Q-Q plots, or statistical tests like the Shapiro-Wilk test (small samples) and the Kolmogorov-Smirnov test (large samples). 
                        \nExample: Checking normality in the distribution of systolic blood pressure readings across a population."""
            )
        else:
            is_normally_distributed = 'Not applicable'

col1, col2 = st.columns(2)
with col1:
    number_of_samples = st.radio(
        "Number of samples:",
        ('One', 'Two', 'More than two'),
        horizontal=True,
        help="""This refers to the number of distinct data groups or sets you are analyzing. 
                \n- **'One'** means analyzing data from a single group.
                \n- **'Two'** means comparing data between two groups, e.g., a control group and a treatment group in a clinical trial.
                \n- **'More than two'** means comparing data across multiple groups, e.g., testing multiple treatments in a clinical study."""
    )



    if number_of_samples == 'One':
        diff_help_text = """Testing for differences with one sample involves comparing the data against a hypothesized value. This is typically done to determine if the sample mean or median significantly deviates from a known or expected value. 
                        \nExamples include: Comparing the average systolic blood pressure readings of a single group of patients against the global average to see if they are significantly higher or lower."""
        association_help_text = """Testing for associations within one sample containing multiple variables involves assessing the relationship between these variables. This analysis can reveal whether and how variables are correlated. 
        \nExamples include
        \nAnalyzing the relationship between age and systolic blood pressure within a sample of patients to see if higher age is associated with higher blood pressure.
        """
    
    elif number_of_samples == 'Two':
        diff_help_text = """Testing for differences with two samples typically involves comparing two independent or paired groups to see if there is a significant difference between their means or medians.
                            \nExamples include:
                            \nComparing the effectiveness of two different medications on lowering blood pressure in two independent groups of patients.
                            \nComparing pre-treatment and post-treatment cholesterol levels in the same group of patients to assess the effect of a new dietary program."""
        association_help_text = """Testing for associations between two samples can involve comparing two variables across these groups to see if there is a relationship between them. Note: Typically, association tests between two samples require a linkage between the samples, such as matched pairs or repeated measures. 
        \nExamples include:
        \nComparing the increase in physical activity and decrease in blood sugar levels before and after an intervention in diabetic patients.
        """
    
    else:
        diff_help_text = """When you have more than two samples, testing for differences usually means comparing the means or medians across multiple groups to see if at least one differs significantly from the others.
        \nExamples include:
        \nComparing the response to three different types of vaccines across three groups of patients to determine which vaccine leads to the highest antibody count.
        """
        association_help_text = """Associations in the context of more than two samples may focus on multivariate relationships across groups, such as investigating how different variables interact across different conditions.
        \nExamples include:
        \nAnalyzing how patient age, treatment type, and recovery time are related across several groups in a clinical trial.
        """


with col2:
        
    if number_of_samples != 'One':

        sample_relationship = st.radio(
            "Are the samples independent?",
            ['Independent', 'Not Independent'],
            horizontal=True,
            help="""Samples are 'independent' if the data groups do not influence each other and are not related. 
                    \nExample of independent samples: Comparing the incidence of flu in different regions. 
                    \nSamples are not independent (i.e., dependent) if the groups are related, such as pre- and post-treatment cholesterol levels in the same patients."""
        )
        num_variables = 'Not applicable'

    else:
        sample_relationship = 'Not applicable - only one sample'
        
        num_variables = st.radio(
        "Number of variables in your dataset:",
        ('One variable', 'Two variables'),
        horizontal=True,
        help="""Select the number of variables:
                \n- **'One variable'** if you're looking to test a single characteristic, such as the proportion of a single categorical variable.
                \n- **'Two variables'** if you're looking to test the association between two characteristics within your dataset.
                """
    )

col1, col2 = st.columns(2)
with col1:
    if num_variables == 'One variable':
        hypothesis_type = st.radio(
            "Type of hypothesis:",
            ['Differences'],
            horizontal=True, 
            index=0, 
            disabled=True,
            help=f"""Type of hypothesis to test:
                    \n- **'Differences'** {diff_help_text}"""
        ) 
    
    elif number_of_samples == 'Two':
        hypothesis_type = st.radio(
            "Type of hypothesis:",
            ['Differences'],
            horizontal=True, 
            index=0, 
            disabled=True,
            help=f"""Type of hypothesis to test:
                    \n- **'Differences'** {diff_help_text}"""
        ) 
    
    elif num_variables == 'Two variables':
        hypothesis_type = st.radio(
            "Type of hypothesis:",
            ['Associations'],
            horizontal=True,
            index=0,
            disabled=True,
            help=f"""Type of hypothesis to test:
                    \n- **'Associations'** {association_help_text}."""
        ) 
    
    elif number_of_samples == 'More than two' and sample_relationship == 'Not Independent':
        hypothesis_type = st.radio(
            "Type of hypothesis:",
            ['Differences'],
            horizontal=True,
            index=0,
            disabled=True,
            help=f"""Type of hypothesis to test:
                    \n- **'Differences'** {diff_help_text}."""
        ) 
    else:
        hypothesis_type = st.radio(
            "Type of hypothesis:",
            ('Differences', 'Associations'),
            horizontal=True,
            help=f"""Type of hypothesis to test:
                    \n- **'Differences'** {diff_help_text}
                    \n- **'Associations'** {association_help_text}."""
        ) 


# pass inputs to the function to identify the recommended stats test(s) to use
recommendations, recommendations_keys = func.recommend_test(data_type, is_normally_distributed, number_of_samples, sample_relationship, hypothesis_type, num_variables)

dict_test_explanations = st_exp.get_dict_test_explanation()
dict_test_videos = st_exp.get_test_explanation_video()


for key in dict_test_explanations.keys():
    dict_test_explanations[key]['video'] = dict_test_videos[key]

st.header(':blue[Recommended Stats Test(s):]')
for test_index in range(len(recommendations)):
    test_name = recommendations_keys[test_index]
    test_name_for_expander = recommendations[test_index]
    test_details = dict_test_explanations[test_name]  # Access the dictionary for this particular test

    st.subheader(test_name_for_expander)
    with st.expander(f"{test_name_for_expander} - Click for information about this test"):
        tab_keys = test_details.keys()  # Get all keys which are tab names like 'Explanation', 'Requirements', etc.
        tabs = st.tabs([key for key in tab_keys])  # Create a tab for each key

        for tab, key in zip(tabs, tab_keys):
            with tab:
                if test_details[key] != 'video':
                    st.write(test_details[key])  # Display the content under each tab corresponding to the key
                else:
                    st.video(test_details[key])

    with st.expander(f"{test_name_for_expander} video"):
        st.video(test_details[key])

#--------------------------------------------
st.header(':blue[Running the tests]')
st.write('To update with a feature to either enable running the test(s) in the app, and/or instructions on how to run in python or excel etc.')


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

