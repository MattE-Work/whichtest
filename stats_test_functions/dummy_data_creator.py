
import numpy as np
import pandas as pd
import streamlit as st

#--------------------------

def create_dummy_data_pearson_correlation(num_samples=100, random_seed=42):
    """
    Generates a dummy dataset for testing Pearson correlation assumptions.

    Args:
    num_samples (int): Number of samples in the dataset.
    random_seed (int): Seed for the random number generator to ensure reproducibility.

    Returns:
    DataFrame: A pandas DataFrame with two columns 'Variable1' and 'Variable2' containing continuous data.
    """
    np.random.seed(random_seed)  # Set the random seed for reproducibility

    # Generate two variables that are positively correlated
    mean = [0, 0]
    cov = [[1, 0.8], [0.8, 1]]  # Covariance matrix: adjust 0.8 for different strengths of correlation

    data = np.random.multivariate_normal(mean, cov, size=num_samples)
    df = pd.DataFrame(data, columns=['Variable1', 'Variable2'])

    return df

# Example use
#df_dummy = create_dummy_data_pearson_correlation()
#print(df_dummy.head())  # Print the first few rows to check the data


#--------------------------

def create_dummy_data_one_sample_t_test(num_samples=30, random_seed=42):
    """
    Generates a dummy dataset for testing the one-sample t-test.

    Args:
    num_samples (int): Number of samples in the dataset.
    random_seed (int): Seed for the random number generator to ensure reproducibility.

    Returns:
    DataFrame: A pandas DataFrame with a single column 'Values' containing the sample data.
    """
    np.random.seed(random_seed)  # Set the random seed for reproducibility

    # Generate data: Random normal data around a hypothetical population mean (e.g., 50) with some added noise
    data = np.random.normal(loc=50, scale=10, size=num_samples)  # loc is the mean, scale is the standard deviation

    # Create DataFrame
    data = pd.DataFrame(data, columns=['Values'])['Values']
    df = pd.DataFrame(data)

    return df

#--------------------------

def create_dummy_data_repeated_measures_anova():
    """
    Generates a dummy dataset for testing Repeated Measures ANOVA.

    Returns:
    DataFrame: A pandas DataFrame with columns for subject ID, condition, and measurement scores.
    """
    np.random.seed(42)  # For reproducible results

    # Parameters
    num_subjects = 10
    conditions = ['Baseline', 'Time1', 'Time2']

    # Generate data
    data = {
        'SubjectID': np.repeat(np.arange(1, num_subjects + 1), len(conditions)),
        'Condition': np.tile(conditions, num_subjects),
        'Score': np.random.normal(20, 5, num_subjects * len(conditions))  # Random normal scores
    }

    df = pd.DataFrame(data)

    # Simulate some progression in the score across conditions for more realistic data
    df.loc[df['Condition'] == 'Time1', 'Score'] += np.random.normal(2, 1, num_subjects)  # Slight increase
    df.loc[df['Condition'] == 'Time2', 'Score'] += np.random.normal(5, 1.5, num_subjects)  # More increase

    # Reshape data to wide format for Pingouin
    df_wide = df.pivot(index='SubjectID', columns='Condition', values='Score')
    df_wide.reset_index(inplace=True)
    df_wide.columns.name = None  # Clean up the columns name to remove 'Condition'

    return df_wide

#--------------------------

def create_dummy_data_anova(num_groups=3, num_samples_per_group=10, random_seed=42):
    """
    Generates a dummy dataset for testing one-way ANOVA.

    Args:
    num_groups (int): Number of different groups.
    num_samples_per_group (int): Number of samples per group.
    random_seed (int): Seed for the random number generator to ensure reproducibility.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Group' and 'Value' suitable for one-way ANOVA.
    """
    np.random.seed(random_seed)  # Set the random seed for reproducibility

    # Define the groups
    groups = ['Group_' + str(i) for i in range(1, num_groups + 1)]

    # Generate data
    data = {
        'Group': np.repeat(groups, num_samples_per_group),  # Repeat each group name for 'num_samples_per_group' times
        'Value': np.concatenate([np.random.normal(loc=20 + i*5, scale=3, size=num_samples_per_group) for i in range(num_groups)])
    }

    df = pd.DataFrame(data)

    return df

#--------------------------

def create_dummy_data_chi_square():
    """
    Generates a dummy dataset with a categorical column and observed counts,
    suitable for a Chi-square goodness of fit test.

    Returns:
    DataFrame: A pandas DataFrame with columns for category and observed counts.
    """
    np.random.seed(42)  # For reproducibility

    # Create data
    data = {
        'Category': ['Red', 'Blue', 'Green', 'Yellow', 'Purple'],
        'Observed': np.random.randint(10, 100, size=5)  # Random counts between 10 and 100
    }

    df = pd.DataFrame(data)

    return df

#--------------------------

def create_long_format_data_for_chi_square_test_independence():
    # Simulating individual response data
    np.random.seed(42)  # For reproducibility
    data = {
        'Gender': np.random.choice(['Male', 'Female'], size=200, p=[0.5, 0.5]),
        'Preference': np.random.choice(['Option A', 'Option B'], size=200, p=[0.4, 0.6])
    }
    df = pd.DataFrame(data)
    return df

#--------------------------
#Function to produce dummy data for each test - for debug mode / build use
#--------------------------
'''
def get_dummy_data_for_tests(selected_recommended_test):
    """
    Returns a dictionary containing dummy data suitable for a variety of statistical tests.
    Each key represents a statistical test, and the value is a tuple or list of data that can be used to perform the test.
    Random seed is set to ensure reproducibility.

    Returns:
    dict: A dictionary with test names as keys and dummy data as values.
    """

    # Set the random seed for reproducibility
    np.random.seed(42)

    # Creating a base normal distribution and a slightly shifted distribution
    base_data = np.random.normal(loc=10, scale=2, size=100)
    shifted_data = base_data + np.random.normal(loc=1, scale=0.5, size=100)
    ordinal_data = np.random.randint(1, 5, size=100)  # For non-parametric tests
    categories = np.random.choice(['A', 'B', 'C'], size=100)

    # Dictionary containing dummy data for each test
    dict_dummy_data = {
        'One-sample t-test': create_dummy_data_one_sample_t_test(),
        'Independent t-Test': (base_data, shifted_data),
        'Paired t-Test': (base_data, base_data * 1.1),
        'Repeated measures ANOVA (for normally distributed data)': create_dummy_data_repeated_measures_anova(),
        'ANOVA (for normally distributed data)': create_dummy_data_anova(),
        'Pearson Correlation (for normally distributed data)': create_dummy_data_pearson_correlation(),
        
        'One-Sample Wilcoxon': (shifted_data, 12),
        'Chi-Square Test of Independence': {
            'data': np.random.randint(1, 100, size=(3, 3))
        },
        'Chi-Square Goodness of Fit': {
            'observed': np.random.randint(1, 100, size=5),
            'expected': np.array([20, 20, 20, 20, 20])
        },
        'One-Sample Non-Parametric Test': (ordinal_data,),
        'Wilcoxon Signed-Rank': (base_data, shifted_data),
        'Kruskal Wallis': {
            'data': np.random.normal(loc=[10, 12, 14], scale=1, size=(100, 3)),
            'groups': np.repeat(['Group1', 'Group2', 'Group3'], 33)
        },
        'Friedman Test': {
            'data': np.random.normal(loc=[10, 12, 14], scale=1, size=(100, 3)),
            'repeated_measures': np.tile(np.arange(1, 101), (3, 1)).T
        },
        'Mann-Whitney U Test': (base_data, shifted_data),
        'Spearman Rank Correlation': (ordinal_data, np.sort(ordinal_data)),
        "Kendall's Tau": (ordinal_data, np.sort(ordinal_data) * -1)
    }

    df = pd.DataFrame(dict_dummy_data[selected_recommended_test])

    return df
'''

#-----------------------------------------
def get_dummy_data_for_tests(selected_recommended_test):
    """
    Returns a dictionary containing dummy data suitable for a variety of statistical tests.
    Each key represents a statistical test, and the value is a tuple or list of data that can be used to perform the test.
    Random seed is set to ensure reproducibility.

    Returns:
    dict: A dictionary with test names as keys and dummy data as values.
    """

    # Set the random seed for reproducibility
    np.random.seed(42)

    # Creating a base normal distribution and a slightly shifted distribution
    base_data = np.random.normal(loc=10, scale=2, size=100)
    shifted_data = base_data + np.random.normal(loc=1, scale=0.5, size=100)
    ordinal_data = np.random.randint(1, 5, size=100)  # For non-parametric tests
    categories = np.random.choice(['A', 'B', 'C'], size=100)

    placeholder_text = 'creation of test data not yet incorporated'

    # Dictionary containing dummy data for each test
    dict_dummy_data = {
    'Chi-square goodness of fit': create_dummy_data_chi_square(),
    'Chi-square test of independence': create_long_format_data_for_chi_square_test_independence(),
    "Cramer's V": placeholder_text,
    'Exact test of Goodness of Fit (multinomial model)': placeholder_text,
    'Exact test of Goodness of Fit': placeholder_text,
    'Factorial ANOVA': placeholder_text,
    'Fischers Exact test': placeholder_text,
    'G-test of Goodness of Fit': placeholder_text,
    'G-test': placeholder_text,
    'Independent samples T-test': pd.DataFrame((base_data, shifted_data)).T.rename(columns={0:'sample1', 1:'sample2'}),
    'Independent samples Z-test': placeholder_text,
    "Kendall's Tau": (ordinal_data, np.sort(ordinal_data) * -1),
    'Kruskal-Wallis': {
            'data': np.random.normal(loc=[10, 12, 14], scale=1, size=(100, 3)),
            'groups': np.repeat(['Group1', 'Group2', 'Group3'], 33)
        },
    'Log-linear analysis': placeholder_text,
    'Mann-Whitney U Test': (base_data, shifted_data),
    'McNemars test': placeholder_text,
    'One-proportion z-test': placeholder_text,
    'One-way ANCOVA': placeholder_text,
    'One-way ANOVA': create_dummy_data_anova(),
    'Paired samples T-test': pd.DataFrame((base_data, base_data * 1.1)).T.rename(columns={0:'sample1_time_point_A', 1:'sample1_time_point_B'}),
    'Paired samples Z-test': placeholder_text,
    'Partial correlation': placeholder_text,
    'Pearson correlation': create_dummy_data_pearson_correlation(),
    'Phi co-efficient': placeholder_text,
    "Point biserial correlation": placeholder_text,
    'Single sample T-test': create_dummy_data_one_sample_t_test(),
    'Single sample wilcoxon signed-rank test': (shifted_data, 12),
    'Single sample Z-test': placeholder_text,
    "Spearman's Rho": placeholder_text,
    'Two proportion z-test': placeholder_text,
    'Wilcoxon signed-rank test': (base_data, shifted_data),
    }

    #retrieve test data from above dict
    test_data_response = dict_dummy_data[selected_recommended_test]

    #if it isn't placeholder string text, return it
    if type(test_data_response) != str:
        #df = pd.DataFrame(dict_dummy_data[selected_recommended_test])
        return test_data_response

    else:
        st.write(placeholder_text)
        st.write(f'App stopped. Required to add test data for: {selected_recommended_test}.')
        st.stop()

#-----------------------------------

#function to provide example of the required structure of the dataset for each test

def expected_data_structure_examples(test_name):
    
    placeholder_text = 'update "expected_data_structure_examples function for this test)'

    with st.expander("Click here to see an example of the expected data format for this test"):

        if test_name == 'Repeated measures ANOVA (for normally distributed data)':
        # Show data format example
            st.write("Your data should be in a wide format for Repeated Measures ANOVA:")
            example_data = {
                'Baseline': [20, 21, 'etc...'],
                'Follow_Up_1': [22, 23, 'etc...'],
                'Follow_Up_2': [24, 25, 'etc...'],
                'etc..': ['etc...', 'etc...', 'etc...'],
            }
            example_df = pd.DataFrame(example_data)

        elif test_name == 'Chi-square goodness of fit':
            example_df = pd.DataFrame(get_dummy_data_for_tests(test_name)).iloc[:20,:]

        elif test_name == 'Chi-square test of independence':
            example_df = create_long_format_data_for_chi_square_test_independence().iloc[:20,:]

        elif test_name == "Cramer's V":
            st.write(placeholder_text)

        elif test_name == 'Exact test of Goodness of Fit (multinomial model)':
            st.write(placeholder_text)

        elif test_name == 'Exact test of Goodness of Fit':
            st.write(placeholder_text)

        elif test_name == 'Factorial ANOVA':
            st.write(placeholder_text)

        elif test_name == 'Fischers Exact test':
            st.write(placeholder_text)

        elif test_name == 'G-test of Goodness of Fit':
            st.write(placeholder_text)

        elif test_name == 'G-test':
            st.write(placeholder_text)
        
        elif test_name == 'Independent samples T-test': #done
            example_df = pd.DataFrame(get_dummy_data_for_tests(test_name)).iloc[:20,:]

        elif test_name == 'Independent samples Z-test':
            st.write(placeholder_text)

        elif test_name == "Kendall's Tau":
            st.write(placeholder_text)

        elif test_name == 'Kruskal-Wallis':
            st.write(placeholder_text)

        elif test_name == 'Log-linear analysis':
            st.write(placeholder_text)

        elif test_name == 'Mann-Whitney U Test':
            st.write(placeholder_text)

        elif test_name == 'McNemars test':
            st.write(placeholder_text)

        elif test_name == 'One-proportion z-test':
            st.write(placeholder_text)

        elif test_name == 'One-way ANCOVA':
            st.write(placeholder_text)

        elif test_name == 'One-way ANOVA':  #done
            # Show data format example
            st.write("Your data should be in a **long** format for ANOVA:")
            #example_df = pd.DataFrame(create_dummy_data_anova()).iloc[:20,:]
            example_df = get_dummy_data_for_tests(test_name).iloc[:20,:]
        
        elif test_name == 'Paired samples T-test': #done
            example_df = get_dummy_data_for_tests(test_name).iloc[:20,:]

        elif test_name == 'Paired samples Z-test':
            st.write(placeholder_text)

        elif test_name == 'Partial correlation':
            st.write(placeholder_text)
            
        elif test_name == 'Pearson correlation': #done
            example_df = get_dummy_data_for_tests(test_name).iloc[:20,:]
        
        elif test_name == 'Phi co-efficient':
            st.write(placeholder_text)

        elif test_name == "Point biserial correlation":
            st.write(placeholder_text)
        
        elif test_name == 'Single sample T-test': #done
            example_df = get_dummy_data_for_tests(test_name).iloc[:20,:]

        elif test_name == 'Single sample wilcoxon signed-rank test':
            st.write(placeholder_text)

        elif test_name == 'Single sample Z-test':
            st.write(placeholder_text)

        elif test_name == "Spearman's Rho":
            st.write(placeholder_text)

        elif test_name == 'Two proportion z-test':
            st.write(placeholder_text)

        elif test_name == 'Wilcoxon signed-rank test':
            st.write(placeholder_text)

        try:
            #render df preview for selected test
            st.table(example_df)
        except:
            pass
    