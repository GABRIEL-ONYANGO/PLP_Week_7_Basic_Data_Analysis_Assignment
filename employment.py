#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Loading and Exploring the Dataset
try:
    # Load dataset
    df = pd.read_csv(r"C:\Users\USER\Desktop\Customer\employment_data.csv")
    print("Dataset loaded successfully!\n")
    
    # Display first few rows
    print("First 5 rows of the dataset:\n", df.head())

    # Check data types and missing values
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())

    # Clean dataset - fill or drop missing values
    df_cleaned = df.dropna()  # Alternatively, use df.fillna(value)
    print(f"\nData after cleaning: {df_cleaned.shape[0]} rows remaining.")
except FileNotFoundError:
    print("Error: 'employment_data.csv' not found.")
except Exception as e:
    print("An error occurred:", str(e))

# Task 2: Basic Data Analysis
try:
    print("\nBasic Statistical Summary:\n", df_cleaned.describe())

    # Assuming 'Series_reference' is a categorical column and 'Data_value' is numerical
    if 'Series_reference' in df_cleaned.columns and 'Data_value' in df_cleaned.columns:
        series_reference_data_value = df_cleaned.groupby('Series_reference')['Data_value'].mean()
        print("\nAverage Salary by Department:\n", series_reference_data_value)
    else:
        print("\nColumns 'Series_reference' and/or 'Data_value' not found for grouping.")
except Exception as e:
    print("Error during analysis:", str(e))

# Task 3: Data Visualization
try:
    sns.set(style="whitegrid")

    # 1. Line Chart ('Period' and 'Data_value' columns)
    if 'Period' in df_cleaned.columns and 'Data_value' in df_cleaned.columns:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df_cleaned, x='Period', y='Data_value')
        plt.title('Total Data Value Over Period')
        plt.xlabel('Period')
        plt.ylabel('Data_value')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 2. Bar Chart (Average Data_value by Series_reference)
    if 'Series_reference' in df_cleaned.columns and 'Data_value' in df_cleaned.columns:
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df_cleaned, x='Series_reference', y='Data_value', estimator='mean', ci=None)
        plt.title('Average Data_value per Series_reference')
        plt.xlabel('Series_reference')
        plt.ylabel('Average Data_value')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 3. Histogram ('Data_value')
    if 'Salary' in df_cleaned.columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(data=df_cleaned, x='Data_value', bins=20, kde=True)
        plt.title('Data_value Distribution')
        plt.xlabel('Data_value')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    # 4. Scatter Plot ('Period' vs 'Data_value')
    if 'Period' in df_cleaned.columns and 'Data_value' in df_cleaned.columns:
        plt.figure(figsize=(8, 4))
        sns.scatterplot(data=df_cleaned, x='Period', y='Data_value')
        plt.title('Data_value vs Period')
        plt.xlabel('Period')
        plt.ylabel('Data_value')
        plt.tight_layout()
        plt.show()
except Exception as e:
    print("Error during visualization:", str(e))