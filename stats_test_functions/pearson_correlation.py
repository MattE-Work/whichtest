import streamlit as st
import pandas as pd
import altair as alt

#------------------------------------
# <<< Function to render assumptions >>>
#------------------------------------

def display_pearson_correlation_assumptions():
    """
    Displays the assumptions required for conducting a Pearson correlation analysis.
    """
    dict_assumptions = {
        "Normality": "Both variables should be normally distributed. Normality of each variable can be checked using a Shapiro-Wilk test or visually inspected through Q-Q plots.",
        "Linearity": "The relationship between the variables must be linear. This implies that the relationship can be well-described by a straight line. Non-linearity can distort the correlation coefficient.",
        "Homoscedasticity": "The scatterplot of the two variables should show a constant spread along the range of variables, indicating that the variance around the regression line is the same for all values of the predictor variable.",
        "Independence": "The observations must be independent of each other. This means the data collected from one observation should not influence the data from another, which is crucial for the validity of the test.",
        "Scale of Measurement": "Both variables should be measured at least at the interval level, which allows for the use of addition and subtraction operations."
    }

    with st.expander("Click for Pearson Correlation Assumptions"):
        for key, value in dict_assumptions.items():
            st.write(f":red[**{key}**:]\n{value}")

# Example of how to call the function in a Streamlit app
# display_pearson_correlation_assumptions()

#------------------------------------
# <<< Function to select columns >>>
#------------------------------------

def select_two_columns_for_pearson_correlation_test(df):
    """
    Renders a 2x select boxes for the user to choose the columns from a dataframe for the pearson correlation.

    Args:
    df (DataFrame): The dataframe from which a column will be selected.

    Returns:
    str: The selected column name or None if "---" is selected.
    """
    st.write("Please select the column names for the variables you want to include in your analysis:")
    
    # Initialize placeholders
    default_option = "---"
    
    # Get column names and include the placeholder as the first option
    options = [default_option] + list(df.columns)
    
    col1, col2 = st.columns(2)

    with col1:
        # Render select box for column selection    
        selected_column_1 = st.selectbox(
            "Select the First Data Column",
            options=options,
            help="Select the column that contains the numerical data for the first variable"
        )
  
    with col2:
        # Render select box for column selection    
        selected_column_2 = st.selectbox(
            "Select the Second Data Column",
            options=options,
            help="Select the column that contains the numerical data for second variable"
        )


    if selected_column_1 == default_option or selected_column_2 == default_option:
        return None
    return selected_column_1, selected_column_2


#------------------------------------
# <<< Function to check normality - Q-Q plot>>>
#------------------------------------
import streamlit as st
import pandas as pd
import scipy.stats as stats
import altair as alt

def check_normality_qqplot_altair(df, variable_1, variable_2):
    """
    Displays a Q-Q plot using Altair to check if a variable is normally distributed.

    Args:
    df (DataFrame): Source pandas DataFrame containing the data.
    variable (str): Column name for the variable to be checked.

    Interpretation:
    - Data points closely following the line suggest normality.
    - Significant deviations from the line indicate departures from normality.
    """
    with st.expander(label='Click for explanation'):
        st.subheader('Explanation:')
        st.write('The Q-Q (Quantile-Quantile) plot compares the quantiles of the variable data against the quantiles of a theoretical normal distribution to assess normality.')
        st.write(":blue[**Blue Points:**] Each point represents a quantile in your data compared to the corresponding quantile of the theoretical normal distribution.")
        st.write(":red[**Red line:**] This line represents a perfect fit where the data are normally distributed. The theoretical quantiles match the data quantiles.")

    with st.expander(label='Click for interpretation'):
        st.subheader('Interpretation:')
        st.write("**If the Points Lie on the Red Line:** This suggests the data are well-modeled by a normal distribution.")
        st.write("**If the Points Deviate from the Red Line:** Significant deviations indicate that the data may not be normally distributed.")

    list_variables = [variable_1, variable_2]

    with st.expander('Click for Q-Q Plot'):
        for variable in list_variables:
            st.subheader(f"***{variable}***")
            # Perform the Q-Q analysis
            qq = stats.probplot(df[variable], dist="norm")

            # Prepare data for plotting
            qq_data = pd.DataFrame({
                'Theoretical Quantiles': [pt[0] for pt in qq[0]],
                'Ordered Values': [pt[1] for pt in qq[0]]
            })

            # Create the Q-Q plot using Altair
            qq_plot = alt.Chart(qq_data).mark_circle(size=60, opacity=0.5).encode(
                x=alt.X('Theoretical Quantiles', title='Theoretical Quantiles'),
                y=alt.Y('Ordered Values', title='Sample Quantiles')
            ).properties(
                title=f'Q-Q plot for Checking Normality of {variable}'
            )

            # Adding a line to represent y=x
            line = alt.Chart(pd.DataFrame({
                'Theoretical Quantiles': qq_data['Theoretical Quantiles'],
                'Ordered Values': qq_data['Theoretical Quantiles']
            })).mark_line(color='red').encode(
                x='Theoretical Quantiles',
                y='Ordered Values'
            )

            # Combine the points and the line
            st.altair_chart(qq_plot + line, use_container_width=True)

# Example usage
# df = pd.DataFrame({'Variable1': np.random.normal(0, 1, 100)})
# check_normality_qqplot_altair(df, 'Variable1')

#------------------------------------
# <<< Function to check normality - Shapiro Wilk Test>>>
#------------------------------------

def check_normality_pearson_correlation_shapiro(df, variable_1, variable_2):
    """
    Checks the normality of the data using the Shapiro-Wilk test for a one-sample t-test.

    Args:
    df (DataFrame): The dataframe containing the data.
    value_column (str): The column in df that contains the values to be tested for normality.

    Returns:
    tuple: The Shapiro-Wilk test statistic and the p-value, indicating normality.
    """

    # Explanation of what a Normality Test is
    with st.expander("Click for explanation"):
        st.write("""
        **Normality tests** such as the **Shapiro-Wilk Test** are used to determine if a dataset is well-modeled by a normal distribution. This test is crucial for methods that assume normality, such as the one-sample t-test, as the conclusions drawn from these tests can be heavily influenced by this assumption.
        """)

    # Guidance on how to interpret the results from the normality test
    #with st.expander("How to Interpret Normality Test Results"):
    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting the Shapiro-Wilk Test:**
        - **P-value > 0.05**: This suggests that the data can be considered normally distributed under the assumption of normality. This means you can proceed with statistical tests that assume normality.
        - **P-value ≤ 0.05**: This indicates that the data do not follow a normal distribution. You might need to consider using non-parametric alternatives if normality is a crucial assumption for your analysis.
        """)

    list_variables = [variable_1, variable_2]

    dict_results = {}
    for variable in list_variables:
        # Extract the data from the specified column
        data = df[variable]

        # Performing the Shapiro-Wilk test
        stat, p_value = stats.shapiro(data)
        
        # Store results in dictionary
        dict_results[variable] = (stat, p_value)

    # Displaying the normality check results
    with st.expander(f"Normality Check Results"):
        for key in dict_results.keys():
            st.subheader(key)
            st.write(f"**{key}**: Shapiro-Wilk Test Statistic: {dict_results[key][0]:.4f}, P-value: {dict_results[key][1]:.4f}")
            if dict_results[key][1] > 0.05:
                st.write("This suggests that the data can be considered normally distributed under the assumption of normality. This means you can proceed with statistical tests that assume normality for this variable.")
            else:
                st.write("This indicates that the data do not follow a normal distribution. You might need to consider using non-parametric alternatives if normality is a crucial assumption for your analysis.")

    return dict_results

#------------------------------------
# <<< Function to check linearity assumption >>>
#------------------------------------

def check_linearity_scatter_plot(df, variable1, variable2):
    """
    Displays a scatter plot with a fitted line to check the linearity between two variables.

    Args:
    df (DataFrame): The dataframe containing the data.
    variable1 (str): The first column in df to plot on the x-axis.
    variable2 (str): The second column in df to plot on the y-axis.

    Returns:
    None: Displays a plot in Streamlit.
    """
    
    with st.expander("Click for explanation"):
        # Explanation of what Linearity is
        st.write("""
        **Linearity** is an assumption of Pearson correlation, which implies that the relationship between the two variables is best described by a straight line. Non-linear relationships (curved patterns, exponential growth, etc.) may not be adequately captured by Pearson correlation.
        """)
    with st.expander("Click for interpretation"):
        # Guidance on how to interpret the scatter plot
        st.write("""
        **Interpreting the Scatter Plot:**
        - **Straight Line Pattern**: Suggests a linear relationship, suitable for Pearson correlation.
        - **Curved Pattern**: Indicates a non-linear relationship. Consider Spearman's rank correlation or other methods suitable for non-linear data.
        """)
    with st.expander("Scatter Plot with Line of Best Fit"):
        # Create the scatter plot
        scatter_plot = alt.Chart(df).mark_circle(size=60, opacity=0.5).encode(
            x=alt.X(variable1, title=f'{variable1}'),
            y=alt.Y(variable2, title=f'{variable2}')
        ).properties(
            title=f'Scatter Plot between {variable1} and {variable2}'
        )
        
        # Adding a line of best fit
        final_plot = scatter_plot + scatter_plot.transform_regression(variable1, variable2).mark_line()
        
        # Combine the scatter plot and the trend line
        st.altair_chart(final_plot, use_container_width=True)


#------------------------------------
# <<< Function to check Homoscedasticity assumption >>>
#------------------------------------

def check_homoscedasticity(df, variable1, variable2):
    """
    Displays a scatter plot and performs Levene's test to check the homoscedasticity between two variables.

    Args:
    df (DataFrame): The dataframe containing the data.
    variable1 (str): The first variable/column in df to test.
    variable2 (str): The second variable/column in df to test.

    Returns:
    None: Displays results in Streamlit.
    """
    with st.expander("Click for explanation"):
        st.write("""
        **Homoscedasticity**, also known as homogeneity of variances, is an assumption that the variance among groups is approximately equal. This is crucial for certain statistical tests, including ANOVA and regression analysis, to ensure reliable results.
        """)

    with st.expander("Click for interpretation"):
        st.write("""
        **Interpreting Homoscedasticity Test Results (Levene's Test):**
        - **P-value > 0.05**: Suggests that the variances are equal across the groups, indicating that the homoscedasticity assumption holds.
        - **P-value ≤ 0.05**: Indicates that variances are not equal across the groups, suggesting a violation of the homoscedasticity assumption. This may require transformations of the data or the use of robust statistical techniques that do not assume equal variances.
        """)

    with st.expander("Homoscedasticity Check"):
        # Prepare data and perform Levene's test
        data1 = df[variable1]
        data2 = df[variable2]
        
        # Levene's test for equal variances
        stat, p_value = stats.levene(data1, data2)

        # Create a scatter plot to visualize the variance distribution
        #scatter_plot = alt.Chart(df).mark_circle(size=60, opacity=0.5).encode(
        #    x=alt.X(variable1, title=f'{variable1}'),
        #    y=alt.Y(variable2, title=f'{variable2}')
        #).properties(
        #    title=f'Scatter Plot for Homoscedasticity Check between {variable1} and {variable2}'
        #)

        #st.altair_chart(scatter_plot, use_container_width=True)
        st.write(f"Levene's Test Statistic: {stat:.4f}, P-value: {p_value:.4f}")
        
        if p_value > 0.05:
            st.success("The test indicates that the assumption of homoscedasticity holds.")
        else:
            st.error("The test indicates a violation of the homoscedasticity assumption.")

# Example usage (to be uncommented and modified as needed)
# df = pd.DataFrame({
#     'Variable1': np.random.normal(0, 1, 100),
#     'Variable2': np.random.normal(0, 1, 100) + np.random.normal(0, 1, 100) * 0.5
# })
# check_homoscedasticity(df, 'Variable1', 'Variable2')


#-----------------------------------------------

#function to render inputs for user to confirm whether assumptions are met, and based on these inputs and bool param, recommend appropriate test
def check_assumptions_and_recommend_test(dict_shapiro_wilk_check_for_each_variable):
    """
    Asks the user to confirm assumptions based on the Q-Q plot and box-plot results and uses the Shapiro-Wilk test result
    to determine if the pearson correlation should be used.

    Args:
    dict_shapiro_wilk_check_for_each_variable (dict): Result from the Shapiro-Wilk test indicating if differences are normally distributed for each of the 2 variables in scope.

    Returns:
    str: Recommendation on which statistical test to use based on the assumptions checks.
    """
    st.subheader("Confirming interpretation of assumption checks")
    col1, col2 = st.columns(2)

    with col1:
        qq_plot_confirmation = st.selectbox(
            "Having reviewed the Q-Q plots, do the points approximately follow the line in both cases?",
            options=["Yes", "No"],
            index=0  # Default to 'Yes'
        )

    with col2:
        scatter_plot_confirmation = st.selectbox(
            "Having reviewed the scatter-plot, is there a visual linear trend?",
            options=["Yes", "No"],
            index=0  # Default to 'Yes'
        )

    list_bool_shapiro_results = [dict_shapiro_wilk_check_for_each_variable[key][1] > 0.05  for key in dict_shapiro_wilk_check_for_each_variable.keys()]

    # Apply logic based on responses and the boolean value
    if qq_plot_confirmation == "Yes" and scatter_plot_confirmation == "Yes" and False not in list_bool_shapiro_results:
        pearson_correlation_confirmation_string = "The assumptions that can be checked have been met. If you are happy the other assumptions are met (outlined in the expander at the top of this section) then you can **:green[proceed with the Pearson Correlation]**."
        proceed_with_pearson_correlation = True
    else:
        issues = []
        if qq_plot_confirmation == "No":
            issues.append("the points do not follow the line in the Q-Q plot")
        if scatter_plot_confirmation == "No":
            issues.append("the scatterplot did not show a linear trend")
        if False in list_bool_shapiro_results:
            issues.append("the differences are not normally distributed (Shapiro-Wilk test)")

        issues_str = ", ".join(issues)
        pearson_correlation_confirmation_string = f"Assumptions not met because {issues_str}. Recommend using the **:red[Spearman's Rank Correlation Coefficient]** as a non-parametric alternative."
        proceed_with_pearson_correlation = False
    
    st.write(pearson_correlation_confirmation_string)
    return proceed_with_pearson_correlation


#-----------------------------------------------
#Function to render all the above functions in the app:
def render_assumption_checks_for_pearson_correlation(df):
    
    #render pearson correlation assumptions
    display_pearson_correlation_assumptions()
    
    #user selects columns 1 and 2
    selected_column_1, selected_column_2 = select_two_columns_for_pearson_correlation_test(df)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        'Q-Q plot (visual normal dist. check)', 
        'Normal dist check',
        'Linearity check',
        'Homoscedasticity check'
        ])

    with tab1:
        #check normality assumption - Q-Q plot
        check_normality_qqplot_altair(df, selected_column_1, selected_column_2)
    
    with tab2:
        #check normality assumption - shapiro wilk plot
        dict_shapiro_wilk_check_for_each_variable = check_normality_pearson_correlation_shapiro(df, selected_column_1, selected_column_2)

    with tab3:
        #visualise linearity check
        check_linearity_scatter_plot(df, selected_column_1, selected_column_2)
    
    with tab4:
        #check homoscedascity
        check_homoscedasticity(df, selected_column_1, selected_column_2)

    #user confirm interpretation:
    proceed_with_pearson_correlation = check_assumptions_and_recommend_test(dict_shapiro_wilk_check_for_each_variable)

    return proceed_with_pearson_correlation