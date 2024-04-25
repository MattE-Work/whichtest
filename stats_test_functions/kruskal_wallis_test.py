import scipy.stats as stats
import pandas as pd
import streamlit as st
import altair as alt


#------------------------------------
# <<< Function to render assumptions >>>
#------------------------------------
#non-parametric alternative to one-way ANOVA when data does not meet the 
# assumptions of normality or when dealing with ordinal data


def display_kruskal_wallis_test_assumptions():
    """
    Displays the assumptions required for conducting the Kruskal-Wallis H-test.
    \nThis test is a non-parametric alternative to one-way ANOVA when 
    data does not meet the assumptions of normality or when dealing with ordinal data.
    """
    dict_assumptions = {
        "Independence": "The observations in each group must be independent. This means that the selection of any observation does not influence the selection of any other observation.",
        "Scale of Measurement": "The data should be at least ordinal, meaning the numeric or categorical values can be ranked or ordered logically.",
        "Identical Distribution Shape": "All groups should come from populations with the same shape of distribution, though they do not need to follow a normal distribution. This means the spread and skewness should be similar across groups, even if their medians differ.",
        "Group Size": "Each group should ideally have more than 5 observations to increase the reliability of the test results. Smaller groups might still be analyzed, but the power to detect differences diminishes."
    }

    with st.expander("Click for Kruskal-Wallis test Assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")

#------------------------------------
# <<< Function to select columns >>>
#------------------------------------

def select_columns_for_kruskal_wallis_test(df):
    """
    Renders select boxes for the user to choose the group and value columns from a dataframe for the Kruskal-Wallis H-test.

    Args:
    df (DataFrame): The dataframe from which columns will be selected.

    Returns:
    tuple: A tuple containing the selected group column and value column names, or None if "---" is selected for either.
    """
    st.write("Please select the column names for your analysis:")

    # Initialize placeholder option
    default_option = "---"
    
    # Get column names and include the placeholder as the first option
    options = [default_option] + list(df.columns)

    col1, col2 = st.columns(2)

    with col1:
        # Render select box for group column selection
        group_column = st.selectbox(
            "Select the Group Column",
            options=options,
            help="Select the column that categorizes the data into different groups for analysis."
        )
  
    with col2:
        # Render select box for value column selection
        value_column = st.selectbox(
            "Select the Value Column",
            options=options,
            help="Select the column that contains the numerical data to be analyzed across the groups."
        )

    # Return the selected columns if both are valid selections
    if group_column != "---" and value_column != "---":
        return group_column, value_column
    else:
        return None, None


#------------------------------------
def check_distribution_shape(df, group_column, value_column):
    """
    Displays Q-Q plots to check if the distribution shapes of different groups are similar.

    Args:
    df (DataFrame): The dataframe containing the data.
    group_column (str): The column in df that denotes the group.
    value_column (str): The column in df that contains the values to be tested.

    Returns:
    None: Displays Q-Q plots in Streamlit.
    """
    # Explanation of what Distribution Shape check involves
    with st.expander("Click for explanation"):
        st.write("""
        **Checking Distribution Shapes:**
        \nThis check involves comparing the distribution of each group against a theoretical distribution to see if the shapes are similar across groups. It is typically done using Q-Q (Quantile-Quantile) plots, where data quantiles are plotted against theoretical quantiles from a standard distribution like the normal distribution.
        """)

    # Guidance on how to interpret the Q-Q plots
    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Q-Q Plots:**
        - **Data Points Close to the Line:** Indicates that the group's distribution shape is similar to the theoretical distribution.
        - **Data Points Deviate from the Line:** Shows differences in the distribution shape, such as skewness or kurtosis, compared to the theoretical distribution. Significant deviations across groups might suggest that the shapes are not similar.
        """)

    # Generate and display Q-Q plots for each group
    groups = df[group_column].unique()

    with st.expander("Distribution Shape Check Results"):
        for group in groups:
            group_data = df[df[group_column] == group][value_column]
            qq = stats.probplot(group_data, dist="norm")
            qq_data = pd.DataFrame({
                'Theoretical Quantiles': [pt[0] for pt in qq[0]],
                'Ordered Values': [pt[1] for pt in qq[0]]
            })
            qq_plot = alt.Chart(qq_data).mark_circle(size=60, opacity=0.5).encode(
                x='Theoretical Quantiles',
                y='Ordered Values',
                tooltip=['Theoretical Quantiles', 'Ordered Values']
            ).properties(
                title=f'Q-Q Plot for Group: {group}'
            )
            line = alt.Chart(pd.DataFrame({
                'Theoretical Quantiles': qq_data['Theoretical Quantiles'],
                'Ordered Values': qq_data['Theoretical Quantiles']
            })).mark_line(color='red').encode(
                x='Theoretical Quantiles',
                y='Ordered Values'
            )
            st.altair_chart(qq_plot + line, use_container_width=True)

#----------------------------
#Confirm scale of measurement assumption
#----------------------------
def explain_scale_of_measurement():
    """
    Provides information about the scale of measurement assumption for the Kruskal-Wallis test.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Scale of Measurement Assumption:**
        The Kruskal-Wallis test requires that the data be at least ordinal. This means that the values should be capable of logical ranking or ordering. This is crucial because the test compares rankings of data across groups.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Scale of Measurement:**
        - **Data Are Ordinal or Higher (Interval, Ratio):** Suitable for the Kruskal-Wallis test. These scales allow for the ranking of data, which is necessary to perform the test.
        - **Data Are Nominal:** Not suitable for the Kruskal-Wallis test. Nominal data, which categorizes without implying any order, does not meet the requirements for this test and would prevent meaningful analysis of ranks.
        """)

#----------------------------
#Confirm independence assumption
#----------------------------

def explain_independence_assumption():
    """
    Asks the user to confirm the independence of observations for the Kruskal-Wallis test.

    Returns:
    bool: True if the user confirms independence, False otherwise.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Independence of Observations:**
        \nThe Kruskal-Wallis test assumes that all groups are independent of each other. This means that knowing the value of one observation should not give any information about the value of another observation in the same or different group.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Independence:**
        - **Data Are Independent:** Suitable for Kruskal-Wallis Test. This setup is essential because the test is designed to compare distributions across groups that do not influence each other.
        - **Data Are Not Independent:** The Kruskal-Wallis Test may not be appropriate. Dependencies within or between groups can affect the test’s validity, potentially leading to incorrect conclusions.
        """)

    # User confirmation
    #independence_confirmed = st.selectbox(
    #    "Confirm if the observations are independent:",
    #    options=["---", "Yes", "No"],
    #    index=0,  # Default to "---"
    #    help="Select 'Yes' if the observations are independent. Select 'No' if observations are dependent."
    #)
#
    ## Display result based on user input
    #if independence_confirmed == "Yes":
    #    st.success("Independence assumption confirmed. You can proceed with the Kruskal-Wallis test.")
    #    return True
    #elif independence_confirmed == "No":
    #    st.error("Independence assumption not met. Consider using another appropriate statistical method or revising the study design.")
    #    return False
    #else:
    #    return None  # No selection made



#----------------------------
#check group size assumption
#----------------------------
def check_group_size(df, group_column):
    """
    Checks if all groups in the dataset have a sufficient number of observations for the Kruskal-Wallis test.

    Args:
    df (DataFrame): The dataframe containing the data.
    group_column (str): The column in df that denotes the group.

    Returns:
    bool: True if all groups have sufficient size, False otherwise.
    """
    # Explanation of what Group Size means
    with st.expander("Click for explanation"):
        st.write("""
        **Group Size Assumption:**
        The Kruskal-Wallis test requires that each group has enough observations to provide a valid analysis. Typically, each group should have at least five observations to ensure that the rank sums can be accurately computed.
        """)

    # Guidance on how to interpret the Group Size requirement
    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Group Size Requirement:**
        - **Sufficient Size (5 or more):** Indicates that the group is large enough to perform the Kruskal-Wallis test reliably.
        - **Insufficient Size (less than 5):** May compromise the test's validity due to inadequate data, leading to unreliable statistical conclusions.
        """)

    # Check the size of each group and display results
    group_sizes = df[group_column].value_counts()

    with st.expander("Group Size Check Results"):
        st.write("Group Sizes:")
        st.dataframe(group_sizes)
        if (group_sizes >= 5).all():
            st.write(":green[All groups have sufficient size. Assumption satisfied.]")
            return True
        else:
            st.error(":red[One or more groups have fewer than 5 observations. Consider collecting more data or using another test method.]")
            return False


#----------------------------
#User inputs to confirm the assumptions that cannot be checked are true
#----------------------------
def confirm_kruskal_wallis_assumptions(group_size_check):
    """
    Renders select boxes for the user to manually confirm the assumptions required for the Kruskal-Wallis test,
    considering the check for group size.
    
    Args:
    group_size_check (bool): Result from the check_group_size function indicating if the group size assumption is met.

    Returns:
    bool: True if all manually checked assumptions are confirmed, False otherwise.
    """
    st.subheader("Confirming remaining assumptions for the Kruskal-Wallis test")

    # If the group size check is False, notify the user and do not proceed with further confirmations
    if not group_size_check:
        st.error("The group size assumption is not met. All groups should have at least five observations. Consider using a different statistical method or collecting more data.")
        return False

    # Initialize placeholders
    default_option = "---"
    options = [default_option, "Yes", "No"]

    col1, col2, col3 = st.columns(3)

    with col1:
        independence_confirmation = st.selectbox(
            "Confirm if the observations are independent:",
            options=options,
            help="Each observation in a group should be independent of the others. This means the collection of one data point should not influence any other."
        )

    with col2:
        scale_of_measurement_confirmation = st.selectbox(
            "Confirm if the data are at least ordinal:",
            options=options,
            help="Data should be ordinal or continuous, allowing for ranking or logical ordering."
        )

    with col3:
        distribution_shape_confirmation = st.selectbox(
            "Confirm if distribution shapes are similar based on the Q-Q plot:",
            options=options,
            help="Each group's distribution should be similarly shaped, as evidenced by Q-Q plots."
        )


    # Check if all necessary confirmations are 'Yes'
    if independence_confirmation == default_option or scale_of_measurement_confirmation == default_option or distribution_shape_confirmation == default_option:
        return None
    elif independence_confirmation == "Yes" and scale_of_measurement_confirmation == "Yes" and distribution_shape_confirmation == "Yes":
        st.success("All necessary assumptions for the Kruskal-Wallis test are confirmed.")
        return True
    else:
        #st.error("One or more critical assumptions are not met. Consider revising the data or using a different statistical method.")
        return False



#----------------------------
#User inputs to confirm the assumptions that cannot be checked are true
#----------------------------
def render_assumption_checks_for_kruskal_wallis_test(df):
    #display assumptions for this test
    display_kruskal_wallis_test_assumptions()
    
    #user selection for group and value columns
    group_column, value_column = select_columns_for_kruskal_wallis_test(df)

    tab1, tab2, tab3, tab4 = st.tabs(['Independence', 'Scale of Measurement', 'Identical Distribution Shape', 'Group Size'])

    with tab1:
        #remind user of independence assumption
        explain_independence_assumption()

    with tab2:
        #remind user of scale of measurement assumption
        explain_scale_of_measurement()
    
    with tab3:
        #reminder user of distribution shape assumption and render Q-Q plot for user to interpret
        check_distribution_shape(df, group_column, value_column)
        
    with tab4:
        #check sample size assumption, return a bool
        bool_sample_size = check_group_size(df, group_column)

    #render select boxes for use to confirm the assumptions are true that 
    # cannot be definitively checked - return a bool
    #only render user checks if the input bool is True 
    # (skip this if False, as assumptions already violated)
    bool_manual_check_assumptions = confirm_kruskal_wallis_assumptions(bool_sample_size)

    return bool_manual_check_assumptions
