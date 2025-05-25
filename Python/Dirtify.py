import pandas as pd
import numpy as np
import random

# Load the clean dataset
df = pd.read_csv('EternaEmployees.csv')

random_seed = 42
random.seed(random_seed)
np.random.seed(random_seed)

# Function to introduce missing values
def introduce_missing_values(df, columns, missing_percentage):
    """
    Introduce missing values (NaN) into specified columns.
    :param df: DataFrame
    :param columns: List of columns to introduce missing values into
    :param missing_percentage: Percentage of missing values to introduce (0 to 1)
    """
    for col in columns:
        # Randomly select rows to set as NaN
        num_missing = int(len(df) * missing_percentage)
        missing_indices = random.sample(range(len(df)), num_missing)
        df.loc[missing_indices, col] = np.nan
    return df

# Function to introduce typos in text columns
def introduce_typos(df, columns, typo_probability):
    """
    Introduce typos into text columns.
    :param df: DataFrame
    :param columns: List of text columns to introduce typos into
    :param typo_probability: Probability of introducing a typo in each cell (0 to 1)
    """
    for col in columns:
        for i in range(len(df)):
            if random.random() < typo_probability:
                # Randomly replace a character in the string
                text = df.at[i, col]
                if isinstance(text, str) and len(text) > 1:
                    typo_index = random.randint(0, len(text) - 1)
                    typo_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                    df.at[i, col] = text[:typo_index] + typo_char + text[typo_index + 1:]
    return df

# Function to introduce outliers in numeric columns
def introduce_outliers(df, columns, outlier_percentage):
    """
    Introduce outliers into numeric columns.
    :param df: DataFrame
    :param columns: List of numeric columns to introduce outliers into
    :param outlier_percentage: Percentage of outliers to introduce (0 to 1)
    """
    for col in columns:
        num_outliers = int(len(df) * outlier_percentage)
        outlier_indices = random.sample(range(len(df)), num_outliers)
        for i in outlier_indices:
            # Multiply the value by a random factor between 2 and 3
            df.at[i, col] *= (round((random.uniform(2, 3))/1000))*1000
    return df

# Function to introduce duplicate rows
def introduce_duplicates(df, duplicate_percentage):
    """
    Introduce duplicate rows into the DataFrame.
    :param df: DataFrame
    :param duplicate_percentage: Percentage of rows to duplicate (0 to 1)
    """
    num_duplicates = int(len(df) * duplicate_percentage)
    duplicate_indices = random.sample(range(len(df)), num_duplicates)
    duplicates = df.iloc[duplicate_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    return df

# Function to introduce inconsistent formatting
def introduce_inconsistent_formatting(df, columns, chance):
    """
    Introduce inconsistent formatting (e.g., mixed case, extra spaces) into text columns.
    :param df: DataFrame
    :param columns: List of text columns to introduce inconsistent formatting into
    """
    for col in columns:
        for i in range(len(df)):
            if random.random() < chance:  # 5% chance of introducing inconsistent formatting
                text = df.at[i, col]
                if isinstance(text, str):
                    # Randomly change case or add extra spaces
                    if random.random() < 0.5:
                        if random.random() < 0.5:
                            df.at[i, col] = text.upper()
                        else:
                            df.at[i, col] = text.lower()
                    else:
                        df.at[i, col] = '  ' + text + '  '
    return df

# Introduce missing values
df = introduce_missing_values(df, ['city', 'department', 'education_level', 'salary'], missing_percentage=0.01)

# Introduce typos
df = introduce_typos(df, ['city', 'job_title'], typo_probability=0.01)

# Introduce outliers
df = introduce_outliers(df, ['salary'], outlier_percentage=0.02)

# Introduce duplicates
df = introduce_duplicates(df, duplicate_percentage=0.01)

# Introduce inconsistent formatting
df = introduce_inconsistent_formatting(df, ['first_name', 'last_name', 'city', 'job_title'], 0.05)

# Save the dirty dataset to a new CSV file
df.to_csv('EternaEmployees_Dirty.csv', index=False)

print("Dirty dataset created and saved as 'EternaEmployees_Dirty.csv'.")