import pandas as pand
import scipy.stats as stat

# Load the cleaned data from a CSV file
cleaned_data = pand.read_csv("//content//drive//MyDrive//Frailty//cleaned_data.csv")

# Extract weight data for two groups based on frailty
fr_w1 = cleaned_data[cleaned_data['Frailty'] == 1]['Weight']
fr_w0 = cleaned_data[cleaned_data['Frailty'] == 0]['Weight']

# Define the path to the text file
txt_file = '//content//drive//MyDrive//Frailty//frailty_analysis.txt'

# Open the text file for writing results
with open(txt_file, 'w') as result_file:
    # Calculate the t-statistic and p-value for a Student's t-test
    result = stat.ttest_ind(fr_w1, fr_w0)
    t_stat = result.statistic
    p_val = result.pvalue

    # Write the results to the text file
    result_file.write("Student's t test t_statistic: " + str(t_stat) + "\n")
    result_file.write("Student's t test p_value: " + str(p_val) + "\n")

    alpha = 0.10
    if p_val < alpha:
        result_file.write("Based on the statistical analysis, we have strong evidence to conclude that there is a significant difference in grip strength between the two groups.")
    else:
        result_file.write("According to the statistical analysis, we do not have sufficient evidence to assert a significant difference in grip strength between the two groups.")
