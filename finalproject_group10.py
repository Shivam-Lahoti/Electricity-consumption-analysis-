# -*- coding: utf-8 -*-
"""FinalProject_Group10

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-AgEc-5g9VBVjEXVDLLFSAJ9oJZHvxIY

## Final Project: INFO6105 Data Science Engineering Methods & Tools
*Professor: Dino Konstantopoulos*

*Group 10: Viswanath Raju Indukuri, Shivam Subhash Lahoti, Hariti Bhatia*

# Energy Consumption and Production Analysis from various sources, Trends and Predictions using Bayesian Model.

## *Data set*
It is the Hourly timeseries data of electricity consumption and production (with production type) in Romania.

In this dataset, It includes the hourly consumption and production, and the production is split in one of the categories: Nuclear, Wind, Hydroelectric, Oil and Gas, Coal, Solar, Biomass. data from January 1st, 2019 to march 3rd, 2023.

The 'DateTime' column details the timestamps for each record, giving us a clear temporal understanding of energy trends. The 'Consumption' column quantifies the total energy consumed during these hourly intervals, while the 'Production' column outlines the total energy generated in the same periods. All values are in MWs.

Each row represents a specific hour, providing a comprehensive view of energy dynamics throughout the day.

source: https://www.kaggle.com/datasets/stefancomanita/hourly-electricity-consumption-and-production

Importing the necessary libraries for data manipulation and visualizations.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""Reading a CSV file containing electricity consumption and production data into a Pandas DataFrame for analysis."""

df = pd.read_csv("/content/drive/MyDrive/Copy of electricityConsumptionAndProduction.csv", parse_dates=['DateTime'], dayfirst=True)
df.head()

"""## *Exploratory Data Analysis*

Quick overview of the DataFrame's structure and content
"""

df.info()

"""Checking if there are any null values"""

df.isnull().sum(axis=0)

"""Checking the summary statistics of the numerical columns within the DataFrame"""

df.describe()

"""Generating histograms in the DataFrame using Matplotlib and Seaborn libraries to visualize the distributions and frequency of values to understanding the data's characteristics and potential insights."""

plt.figure(figsize=(12, 8))
for column in df.columns[1:10]:
    plt.figure(figsize=(10,6))
    sns.histplot(df[column], kde=True, bins=30, color='orange')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

"""## *Electricity Consumption Trends, Visualizations over time & Analysis*

Let's look into the Consumption trends over time.
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['DateTime'], df['Consumption'] , color='red')
plt.title('Hourly Energy Consumption Trend')
plt.xlabel('Date and Time')
plt.ylabel('Consumption in MWs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Diffentiating the visualizations for each year. This visualization allows for a clear comparison of energy consumption patterns across different years."""

df['DateTime'] = pd.to_datetime(df['DateTime'])

# Filter data for the years 2019 through 2023
df_2019 = df[df['DateTime'].dt.year == 2019]
df_2020 = df[df['DateTime'].dt.year == 2020]
df_2021 = df[df['DateTime'].dt.year == 2021]
df_2022 = df[df['DateTime'].dt.year == 2022]
df_2023 = df[df['DateTime'].dt.year == 2023]

# Create line plots for the years 2019 through 2023
plt.figure(figsize=(12, 6))
plt.plot(df_2019['DateTime'], df_2019['Consumption'], linestyle='-', label='2019')
plt.plot(df_2020['DateTime'], df_2020['Consumption'], linestyle='-', label='2020')
plt.plot(df_2021['DateTime'], df_2021['Consumption'], linestyle='-', label='2021')
plt.plot(df_2022['DateTime'], df_2022['Consumption'], linestyle='-', label='2022')
plt.plot(df_2023['DateTime'], df_2023['Consumption'], linestyle='-', label='2023')
plt.title('Hourly Energy Consumption from 2019 to 2023')
plt.xlabel('Date and Time')
plt.ylabel('Consumption in MWs')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

"""Plotting the Consumption trends for each year separetly"""

df['DateTime'] = pd.to_datetime(df['DateTime'])

# Create a loop to plot hourly energy consumption for each year from 2019 to 2023
for year in range(2019, 2024):
    # Filter data for the current year
    df_year = df[df['DateTime'].dt.year == year]

    # Create a line plot for the current year
    plt.figure(figsize=(12, 6))
    plt.plot(df_year['DateTime'], df_year['Consumption'], color='red')
    plt.title(f'Hourly Energy Consumption in {year}')
    plt.xlabel('Date and Time')
    plt.ylabel('Consumption')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

"""Print the mean consumptions for each Month for each Year"""

df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extracting year and month from the 'DateTime' column
df['Year'] = df['DateTime'].dt.year
df['Month'] = df['DateTime'].dt.month

# Grouping by year and month, calculating the mean consumption for each group
monthly_mean_consumption = df.groupby(['Year', 'Month'])['Consumption'].mean().reset_index()

# Displaying mean consumptions for each month in a year
for year in monthly_mean_consumption['Year'].unique():
    print(f"Year: {year}")
    yearly_data = monthly_mean_consumption[monthly_mean_consumption['Year'] == year]
    for month in range(1, 13):
        mean_consumption = yearly_data[yearly_data['Month'] == month]['Consumption'].values
        if len(mean_consumption) > 0:
            print(f"Month: {month}, Mean Consumption: {mean_consumption[0]}")

"""Visualize the monthly average energy consumption across each of the years."""

import calendar

df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extracting monthly information and mean consumption for each year
df['Year'] = df['DateTime'].dt.year
df['Month'] = df['DateTime'].dt.month
monthly_consumption = df.groupby(['Year', 'Month'])['Consumption'].mean().unstack()
print(monthly_consumption)

# Plotting line graph for monthly consumption for each year
plt.figure(figsize=(12, 6))
for year in monthly_consumption.index:
    plt.plot(monthly_consumption.columns, monthly_consumption.loc[year], label=str(year))

# Replace numeric x-axis ticks with month names
plt.xticks(ticks=range(1, 13), labels=[calendar.month_name[i] for i in range(1, 13)])

plt.title('Monthly Consumption for Each Year')
plt.xlabel('Month')
plt.ylabel('Mean Consumption')
plt.legend(title='Year')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

"""Mean consumption for each Month across all years and a line plot illustrating the Monthly Mean consumption trends across all years"""

# Extracting 'Month' and 'Year' information
df['Month'] = df['DateTime'].dt.month
df['Year'] = df['DateTime'].dt.year

# Calculating mean consumption for each month across all years
mean_monthly_consumption = df.groupby('Month')['Consumption'].mean()

# Plotting line graph for mean monthly consumption across all years
plt.figure(figsize=(10, 6))
plt.plot(mean_monthly_consumption.index, mean_monthly_consumption.values, marker='o', linestyle='-', color='red')
plt.title('Mean Monthly Consumption Across All Years')
plt.xlabel('Month')
plt.ylabel('Mean Consumption')
plt.xticks(range(1, 13), [calendar.month_name[i] for i in range(1, 13)])  # Setting month names as x-axis ticks
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Printing the mean consumptions for each Hour for each Year"""

df['DateTime'] = pd.to_datetime(df['DateTime'])
# Extract 'Year' and 'Hour' information from 'DateTime' column
df['Year'] = df['DateTime'].dt.year
df['Hour'] = df['DateTime'].dt.hour

# Calculate mean consumption for each hour for each year
hourly_mean_consumption_each_year = df.groupby(['Year', 'Hour'])['Consumption'].mean().reset_index()

# Display mean consumptions for each hour for each year
for year in hourly_mean_consumption_each_year['Year'].unique():
    print(f"Year: {year}")
    yearly_data = hourly_mean_consumption_each_year[hourly_mean_consumption_each_year['Year'] == year]
    for hour in range(24):
        mean_consumption = yearly_data[yearly_data['Hour'] == hour]['Consumption'].values
        if len(mean_consumption) > 0:
            print(f"Hour: {hour}, Mean Consumption: {mean_consumption[0]}")

"""Line plot illustrating the hourly consumption trends for each year."""

df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extracting hourly information and mean consumption for each year
df['Year'] = df['DateTime'].dt.year
hourly_consumption = df.pivot_table(index=df['DateTime'].dt.hour, columns='Year', values='Consumption', aggfunc='mean')
print(hourly_consumption)

# Plotting line graph for hourly consumption for all years
plt.figure(figsize=(12, 6))
for year in hourly_consumption.columns:
    plt.plot(hourly_consumption.index, hourly_consumption[year], label=str(year))

# Set x-axis ticks to show all 24 hours
plt.xticks(range(24))

plt.title('Hourly Consumption for All Years')
plt.xlabel('Hour of the Day')
plt.ylabel('Consumption')
plt.legend(title='Year')
plt.grid(True)
plt.tight_layout()
plt.show()

"""Line plot illustrating the hourly Mean consumption trends across all years"""

# Extract 'Hour' information from 'DateTime' column
df['Hour'] = df['DateTime'].dt.hour

# Calculate mean consumption for each hour across all years
hourly_mean_consumption_all_years = df.groupby('Hour')['Consumption'].mean()
print(hourly_mean_consumption_all_years)

# Plotting a line graph for mean consumption for each hour across all years
plt.figure(figsize=(10, 6))
plt.plot(hourly_mean_consumption_all_years.index, hourly_mean_consumption_all_years.values, marker='o', linestyle='-', color='red')
plt.title('Mean Consumption for Each Hour Across All Years')
plt.xlabel('Hour of the Day')
plt.ylabel('Mean Consumption')
plt.xticks(range(24))  # Setting x-axis ticks for all 24 hours
plt.grid(True)
plt.tight_layout()
plt.show()

"""## *Electricity production Trends, Visualizations & Analysis*

General trend of Production and Consumption
"""

df[["Consumption", "Production"]].plot(style="-", figsize=(15, 5), title="Electricity Consumption and Production, in MW")
plt.ylabel('MW')
plt.show()

"""Total production and thier percentages for renewable and non-renewable sources for each year"""

renewable_sources = ['Wind', 'Hydroelectric', 'Solar', 'Biomass']
non_renewable_sources = ['Nuclear', 'OilandGas', 'Coal']
# Calculate total production for renewable and non-renewable sources for each year
yearly_total_renewable = df.groupby(df['DateTime'].dt.year)[renewable_sources].sum()
yearly_total_non_renewable = df.groupby(df['DateTime'].dt.year)[non_renewable_sources].sum()

# Calculate percentage contribution of renewable and non-renewable sources for each year
yearly_percentage_renewable = (yearly_total_renewable.div(yearly_total_renewable.sum(axis=1), axis=0)) * 100
yearly_percentage_non_renewable = (yearly_total_non_renewable.div(yearly_total_non_renewable.sum(axis=1), axis=0)) * 100

# Display numerical values of production and percentage contribution for each year
for year in df['DateTime'].dt.year.unique():
    print(f"Year: {year}")
    print("Renewable Energy Production:")
    print(yearly_total_renewable.loc[year])
    print("Percentage Contribution of Renewable Energy:")
    print(yearly_percentage_renewable.loc[year])
    print("Non-Renewable Energy Production:")
    print(yearly_total_non_renewable.loc[year])
    print("Percentage Contribution of Non-Renewable Energy:")
    print(yearly_percentage_non_renewable.loc[year])
    print("=" * 50)

# Define renewable and non-renewable energy sources
renewable_sources = ['Wind', 'Hydroelectric', 'Solar', 'Biomass']
non_renewable_sources = ['Nuclear', 'OilandGas', 'Coal']

# Calculate total production for renewable and non-renewable sources for each year
yearly_total_renewable = df.groupby(df['DateTime'].dt.year)[renewable_sources].sum()
yearly_total_non_renewable = df.groupby(df['DateTime'].dt.year)[non_renewable_sources].sum()

# Calculate percentage contribution of renewable and non-renewable sources for each year
yearly_percentage_renewable = (yearly_total_renewable.div(yearly_total_renewable.sum(axis=1), axis=0)) * 100
yearly_percentage_non_renewable = (yearly_total_non_renewable.div(yearly_total_non_renewable.sum(axis=1), axis=0)) * 100

# Plot pie charts for percentage contribution of renewable and non-renewable sources for each year
for year in df['DateTime'].dt.year.unique():
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.pie(yearly_percentage_renewable.loc[year], labels=renewable_sources, autopct='%1.1f%%', startangle=90)
    plt.title(f'Renewable Energy Contribution for {year}')

    plt.subplot(1, 2, 2)
    plt.pie(yearly_percentage_non_renewable.loc[year], labels=non_renewable_sources, autopct='%1.1f%%', startangle=90)
    plt.title(f'Non-Renewable Energy Contribution for {year}')

    plt.tight_layout()
    plt.show()

"""Contribution of Each Energy Source to Overall Production"""

# total production for each energy source
energy_sources = ['Wind', 'Hydroelectric', 'Solar', 'Biomass', 'Nuclear', 'OilandGas', 'Coal']
total_production = df[energy_sources].sum()
print(total_production)

plt.figure(figsize=(10, 6))
total_production.plot(kind='bar')
plt.title('Contribution of Each Energy Source to Overall Production')
plt.xlabel('Energy Sources')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Percentage contribution for electricity production from renewable and non-renewable sources for each year"""

renewable_sources = ['Wind', 'Hydroelectric', 'Solar', 'Biomass']
non_renewable_sources = ['Nuclear', 'OilandGas', 'Coal']
# total production for renewable and non-renewable sources for each year
yearly_total_renewable = df.groupby(df['DateTime'].dt.year)[renewable_sources].sum()
yearly_total_non_renewable = df.groupby(df['DateTime'].dt.year)[non_renewable_sources].sum()
print(yearly_total_renewable)
print(yearly_total_non_renewable)

# percentage contribution of renewable and non-renewable sources for each year
yearly_percentage_renewable = (yearly_total_renewable.div(yearly_total_renewable.sum(axis=1), axis=0)) * 100
yearly_percentage_non_renewable = (yearly_total_non_renewable.div(yearly_total_non_renewable.sum(axis=1), axis=0)) * 100
# percentages of renewable and non-renewable sources for each year
combined_percentage = yearly_percentage_renewable.add(yearly_percentage_non_renewable, fill_value=0)

for year in df['DateTime'].dt.year.unique():
    plt.figure(figsize=(8, 6))

    plt.pie(combined_percentage.loc[year], labels=combined_percentage.columns, autopct='%1.1f%%', startangle=90)
    plt.title(f'Production Contribution for {year}')

    plt.tight_layout()
    plt.show()

"""Contribution from the each energy source to the overall Electricity production"""

total_combined_percentage = combined_percentage.sum()

plt.figure(figsize=(8, 6))

plt.pie(total_combined_percentage, labels=total_combined_percentage.index, autopct='%1.1f%%', startangle=90)
plt.title('Production Contribution for All Years')

plt.tight_layout()
plt.show()

"""Year with maxium percentage contribution for each energy sources: Renewable and Non-Renewable"""

# Calculate total production for renewable and non-renewable sources for each year
yearly_total_renewable = df.groupby(df['DateTime'].dt.year)[renewable_sources].sum()
yearly_total_non_renewable = df.groupby(df['DateTime'].dt.year)[non_renewable_sources].sum()

# Calculate percentage contribution of renewable and non-renewable sources for each year
yearly_percentage_renewable = (yearly_total_renewable.div(yearly_total_renewable.sum(axis=1), axis=0)) * 100
yearly_percentage_non_renewable = (yearly_total_non_renewable.div(yearly_total_non_renewable.sum(axis=1), axis=0)) * 100

# Find the year with the highest percentage contribution for each energy source (renewable)
print("Year with highest percentage contribution for renewable energy sources:")
for source in renewable_sources:
    max_year_renewable = yearly_percentage_renewable[source].idxmax()
    print(f"{source}: {max_year_renewable} - {yearly_percentage_renewable.loc[max_year_renewable, source]:.2f}%")

# Find the year with the highest percentage contribution for each energy source (non-renewable)
print("\nYear with highest percentage contribution for non-renewable energy sources:")
for source in non_renewable_sources:
    max_year_non_renewable = yearly_percentage_non_renewable[source].idxmax()
    print(f"{source}: {max_year_non_renewable} - {yearly_percentage_non_renewable.loc[max_year_non_renewable, source]:.2f}%")

"""Year with minimum percentage contribution for each energy sources: Renewable and Non-Renewable"""

# lowest percentage contribution for each energy source (renewable)
print("Year with lowest percentage contribution for renewable energy sources:")
for source in renewable_sources:
    min_year_renewable = yearly_percentage_renewable[source].idxmin()
    print(f"{source}: {min_year_renewable} - {yearly_percentage_renewable.loc[min_year_renewable, source]:.2f}%")

# lowest percentage contribution for each energy source (non-renewable)
print("\nYear with lowest percentage contribution for non-renewable energy sources:")
for source in non_renewable_sources:
    min_year_non_renewable = yearly_percentage_non_renewable[source].idxmin()
    print(f"{source}: {min_year_non_renewable} - {yearly_percentage_non_renewable.loc[min_year_non_renewable, source]:.2f}%")

"""Scatter plot of the electricity production from each energy source"""

for i in ['Nuclear','Wind','Hydroelectric','OilandGas','Coal','Solar','Biomass']:
    plt.figure(figsize=(15,6))
    sns.scatterplot(data=df,y='Production',x=i)
    plt.show()

"""## *Bayesian model for predictions of Consumption and Production from Renewable sources with highest percentage of power generation*

To make informed decisions regarding the amount of electricity to produce from non-renewable sources, it's important to consider the predictive consumption and production from renewable sources which are Hydroelectric and Wind. When comparing these significant contributors Hydroelectric and Wind to smaller contributors like solar and biomass, which collectively account for only 2-3% of the overall production each year.

## *Bayesian model for Electricity Consumption*
"""

import pymc as pm
from scipy.stats.distributions import gamma
import arviz as az

with pm.Model() as consumption_model:
    # Prior distribution for parameters of the gamma distribution
    expalpha = pm.Exponential('alpha', 1)
    expbeta = pm.Exponential('beta', 1)

    # Likelihood (gamma distribution)
    consumption = pm.Gamma('consumption', alpha=expalpha, beta=expbeta, observed=df.Consumption)

with consumption_model:
  trace = pm.sample(1000, tune=1000)

# Plot posterior distributions
az.plot_posterior(trace.posterior)

# Summarize the trace
print(pm.summary(trace))
az.plot_trace(trace)

print(pm.summary(trace))

trace

alpha = trace.posterior['alpha'].mean()
beta = trace.posterior['beta'].mean()
alpha, beta

alpha = trace.posterior['alpha'].values.mean()
beta = trace.posterior['beta'].values.mean()
df.Consumption.hist(density=True, bins=20, alpha=0.5, label='data PDF Hist')
x = np.linspace(2000, 10000)
plt.plot(x, gamma.pdf(x, alpha, scale=1/beta), 'r-', label='Gamma PDF')
plt.legend()
plt.xlabel('Consumption')
plt.ylabel('Density')
plt.title('Histogram with Gamma PDF')
plt.grid(True)
plt.show()

with consumption_model:
    #pp_trace = pm.sample_ppc(trace)
    pp_trace = pm.sample_posterior_predictive(trace)

pp_trace.posterior_predictive['consumption'].shape

posterior_consumption = pp_trace.posterior_predictive['consumption'][1][500]

posterior_consumption

posterior_consumption_df = posterior_consumption.to_dataframe()

posterior_consumption_df

import matplotlib.pyplot as plt

# Assuming 'consumption' is the column you want to plot
consumption_column = posterior_consumption_df['consumption']

# Plotting histogram with density normalization
plt.hist(consumption_column, bins=30, edgecolor='black', density=True)
plt.title('Posterior predictive Consumption')
plt.xlabel('Consumption in MW')
plt.ylabel('Probability Density')
plt.show()

def meanAbsolutErrorAaPercentage(real, predicted):
    real = np.array(real)
    predicted = np.array(predicted)

    return np.mean(np.abs((real - predicted) / real)) * 100

dfReal = df["Consumption"]
dfPredicted = posterior_consumption_df["consumption"]

print(f"percentage error: {meanAbsolutErrorAaPercentage(dfReal, dfPredicted):.4f}")

"""## *Bayesian model for Hydroelectric production*"""

# Define the PyMC model
with pm.Model() as Hydroelectric_production_model:
    # Prior distribution for parameters of the gamma distribution
    expalpha = pm.Exponential('alpha', 1)
    expbeta = pm.Exponential('beta', 1)

    # Likelihood (gamma distribution)
    Hydroelectric_production = pm.Gamma('Hydroelectric_production', alpha=expalpha, beta=expbeta, observed=df.Hydroelectric)

with Hydroelectric_production_model:
  trace = pm.sample(1000, tune=1000)

# Plot posterior distributions
az.plot_posterior(trace.posterior)

# Summarize the trace
print(pm.summary(trace))
az.plot_trace(trace)

alpha = trace.posterior['alpha'].mean()
beta = trace.posterior['beta'].mean()
df.Hydroelectric.hist(density=True, bins=20, alpha=0.5, label='data PDF Hist')
x = np.linspace(0, 4500)
plt.plot(x, gamma.pdf(x, alpha, scale=1/beta), 'r-', label='Gamma PDF')
plt.legend()
plt.xlabel('Hydroelectric Production in MW')
plt.ylabel('Density')
plt.title('Histogram with Gamma PDF')
plt.grid(True)
plt.show()

with Hydroelectric_production_model:
    #pp_trace = pm.sample_ppc(trace)
    pp_trace = pm.sample_posterior_predictive(trace)

pp_trace.posterior_predictive['Hydroelectric_production'].shape

posterior_Hydroelectric_production = pp_trace.posterior_predictive['Hydroelectric_production'][1][500]

posterior_Hydroelectric_production

posterior_Hydroelectric_production_df = posterior_Hydroelectric_production.to_dataframe()

posterior_Hydroelectric_production_df

import matplotlib.pyplot as plt

# Assuming 'consumption' is the column you want to plot
Hydroelectric_production_column = posterior_Hydroelectric_production_df['Hydroelectric_production']

# Plotting histogram with density normalization
plt.hist(Hydroelectric_production_column, bins=30, edgecolor='black', density=True)
plt.title('Posterior predictive Hydroelectric Production')
plt.xlabel('Hydroelectric production in MW')
plt.ylabel('Probability Density')
plt.show()

"""## *Bayesian model for Electricity production from Wind energy*"""

# Define the PyMC model
with pm.Model() as Wind_production_model:
    # Prior distribution for parameters of the gamma distribution
    expalpha = pm.Exponential('alpha', 1)
    expbeta = pm.Exponential('beta', 1)

    # Likelihood
    Wind_production = pm.Gamma('Wind_production', alpha=expalpha, beta=expbeta, observed=df.Wind)

with Wind_production_model:
  trace = pm.sample(1000, tune=1000)

# Plot posterior distributions
az.plot_posterior(trace.posterior)

# Summarize the trace
print(pm.summary(trace))
az.plot_trace(trace)

alpha = trace.posterior['alpha'].mean()
beta = trace.posterior['beta'].mean()
df.Wind.hist(density=True, bins=20, alpha=0.5, label='data PDF Hist')
x = np.linspace(0, 8000)
plt.plot(x, gamma.pdf(x, alpha, scale=1/beta), 'r-', label='Gamma PDF')
plt.legend()
plt.xlabel('Wind Electricity Production')
plt.ylabel('Density')
plt.title('Histogram with Gamma PDF')
plt.grid(True)
plt.show()

with Wind_production_model:
    #pp_trace = pm.sample_ppc(trace)
    pp_trace = pm.sample_posterior_predictive(trace)

pp_trace.posterior_predictive['Wind_production'].shape

posterior_Wind_production = pp_trace.posterior_predictive['Wind_production'][1][500]

posterior_Wind_production

posterior_Wind_production_df = posterior_Wind_production.to_dataframe()
posterior_Wind_production_df

Wind_production_column = posterior_Wind_production_df['Wind_production']

# Plotting histogram with density normalization
plt.hist(Wind_production_column, bins=30, edgecolor='black', density=True)
plt.title('Posterior predictive production from Wind Energy')
plt.xlabel('Production in MW')
plt.ylabel('Probability Density')
plt.show()

"""Creating the predictive_df with posterior predictive values of Comsumption and Production from Hydroelectric and Wind for 2024"""

predictive_df = pd.DataFrame(pd.date_range(start='2024-01-01', end='2024-12-31', freq='H'), columns=['DateTime'])

predictive_df['Consumption'] = posterior_consumption_df['consumption']
predictive_df['Hydroelectric'] = posterior_Hydroelectric_production_df['Hydroelectric_production']
predictive_df['Wind'] = posterior_Wind_production_df['Wind_production']

predictive_df

total_consumption = predictive_df['Consumption'].sum()
print(total_consumption)
# Calculate the total Hydroelectric and Wind production
total_hydroelectric = predictive_df['Hydroelectric'].sum()
total_wind = predictive_df['Wind'].sum()
print(total_hydroelectric)
print(total_wind)
# Calculate percentages in relation to total consumption
hydroelectric_percentage = (total_hydroelectric / total_consumption) * 100
wind_percentage = (total_wind / total_consumption) * 100

# Remaining percentage for Consumption after deducting Hydroelectric and Wind
consumption_remaining = 100 - (hydroelectric_percentage + wind_percentage)

# Pie chart data
labels = ['Hydroelectric', 'Wind', 'Remaining Consumption']
sizes = [hydroelectric_percentage, wind_percentage, consumption_remaining]
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = (0.1, 0.1, 0.1)  # explode 1st slice

# Plotting the pie chart for Consumption, Hydroelectric, and Wind
plt.figure(figsize=(8, 5))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Consumption Covered by Hydroelectric and Wind for 2024')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

total_consumption = int(predictive_df['Consumption'].sum())
print(f"The total projected consumption is: {total_consumption:,} MW")

# Calculate the total Hydroelectric and Wind production
total_hydroelectric = int(predictive_df['Hydroelectric'].sum())
total_wind = int(predictive_df['Wind'].sum())
print(f"The total projected Hydroelectric production is: {total_hydroelectric:,} MW")
print(f"The total projected Wind production is: {total_wind:,} MW")

"""# Conclusion

Looking at the consumption predictions for 2024 and biggest contributors among renewable sources which are Hydroelectric and Wind power. Together, they make up 38% of the total energy. Hydroelectric power covers 27%, and Wind power covers 11%.

Predicting electricity consumption and production from highest contributors among renewable sources like hydroelectric and wind power is crucial for informed decision-making in energy generation. By accurately forecasting these factors, it becomes possible to plan and allocate resources effectively.

The accurate prediction of electricity consumption and production from renewable sources like hydroelectric and wind power serves as a cornerstone for informed decision-making in energy management.
"""