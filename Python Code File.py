# ==============================================================================
# IBM SkillsBuild Internship: Data Analytics & AI
# File Name: Rahul_DataAnalyticsProject.py
# Author: Rahul
# Description: Data Cleaning, Exploratory Data Analysis (EDA), & Visualization
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual aesthetic
sns.set_theme(style="whitegrid")

def main():
    print("==================================================")
    print(" IBM SkillsBuild Data Analytics & AI Internship ")
    print(" Project Submission by: Rahul ")
    print("==================================================\n")
    
    print("--- 1. Generating Analytical Dataset ---")
    np.random.seed(42)
    data = {
        'CustomerID': range(101, 201),
        'Age': np.random.randint(18, 65, size=100),
        'Annual_Income_k$': np.random.randint(15, 137, size=100),
        'Spending_Score': np.random.randint(1, 100, size=100),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], size=100)
    }
    df = pd.DataFrame(data)
    print("Dataset loaded successfully. Total Records:", df.shape[0])
    
    print("\n--- 2. Data Cleaning & Preprocessing ---")
    print(df.info())
    print("\nMissing values check:")
    print(df.isnull().sum())
    
    print("\nSummary Statistics:")
    print(df.describe())

    print("\n--- 3. Exploratory Data Analysis (EDA) ---")
    
    # 1. Distribution Plot
    plt.figure(figsize=(8, 4))
    sns.histplot(df['Annual_Income_k$'], kde=True, color='skyblue')
    plt.title("Annual Income Distribution - Rahul")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("income_distribution.png")
    print("Saved visualization: income_distribution.png")

    # 2. Spending vs Income Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Annual_Income_k$', y='Spending_Score', hue='Category', s=80)
    plt.title("Income vs Spending Score by Category - Rahul")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.tight_layout()
    plt.savefig("income_vs_spending.png")
    print("Saved visualization: income_vs_spending.png")

    # 3. Correlation Heatmap
    plt.figure(figsize=(6, 4))
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='Blues', fmt='.2f')
    plt.title("Feature Correlation Matrix - Rahul")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    print("Saved visualization: correlation_heatmap.png")

    print("\n--- 4. Summary Insights ---")
    avg_spending = df.groupby('Category')['Spending_Score'].mean()
    print("Average Spending Score per Category:")
    print(avg_spending)
    print("\nProject Analysis Completed Successfully by Rahul!")

if __name__ == "__main__":
    main()