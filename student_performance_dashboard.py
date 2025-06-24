import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style and color palette
tableau20 = [
    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)
]
tableau20 = [(r/255., g/255., b/255.) for r, g, b in tableau20]
sns.set_palette(tableau20)
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Open Sans', 'DejaVu Sans']
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 13
plt.rcParams['axes.edgecolor'] = 'lightgrey'
plt.rcParams['axes.linewidth'] = 1
plt.rcParams['grid.color'] = 'lightgrey'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.5
plt.rcParams['figure.dpi'] = 120


os.makedirs('figures', exist_ok=True)

# 1. Data Loading and Cleaning

df = pd.read_csv('StudentsPerformance.csv')


# 2. Summary Statistics
# ---------------------
summary = df.describe(include='all')
summary.to_csv('figures/summary_statistics.csv')
print("Summary statistics saved to figures/summary_statistics.csv")

# 3. Visualizations
# -----------------

def save_fig(fig, name):
    fig.savefig(f'figures/{name}.png', bbox_inches='tight', dpi=300)
    plt.close(fig)

# 1. Box Plot: Scores by Gender
def boxplot_scores_by_gender(df):
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    for i, subject in enumerate(['math score', 'reading score', 'writing score']):
        sns.boxplot(x='gender', y=subject, data=df, ax=axes[i])
        axes[i].set_title(f'{subject.title()} by Gender')
        axes[i].set_xlabel('Gender')
        axes[i].set_ylabel('Score')
    fig.suptitle('Score Distributions by Gender', fontsize=18)
    save_fig(fig, 'boxplot_scores_by_gender')

# 2. Box Plot: Scores by Test Preparation Course
def boxplot_scores_by_testprep(df):
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    for i, subject in enumerate(['math score', 'reading score', 'writing score']):
        sns.boxplot(x='test preparation course', y=subject, data=df, ax=axes[i])
        axes[i].set_title(f'{subject.title()} by Test Preparation')
        axes[i].set_xlabel('Test Preparation Course')
        axes[i].set_ylabel('Score')
    fig.suptitle('Score Distributions by Test Preparation Course', fontsize=18)
    save_fig(fig, 'boxplot_scores_by_testprep')

# 3. Bar Chart: Average scores by Parental Level of Education
def barchart_avg_scores_by_parent_edu(df):
    avg_scores = df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_scores.plot(x='parental level of education', kind='bar', ax=ax)
    ax.set_title('Average Scores by Parental Level of Education')
    ax.set_xlabel('Parental Level of Education')
    ax.set_ylabel('Average Score')
    plt.xticks(rotation=30, ha='right')
    save_fig(fig, 'barchart_avg_scores_by_parent_edu')

# 4. Bar Chart: Average scores by Lunch Type
def barchart_avg_scores_by_lunch(df):
    avg_scores = df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 6))
    avg_scores.plot(x='lunch', kind='bar', ax=ax)
    ax.set_title('Average Scores by Lunch Type')
    ax.set_xlabel('Lunch Type')
    ax.set_ylabel('Average Score')
    save_fig(fig, 'barchart_avg_scores_by_lunch')

# 5. Bar Chart: Average scores by Race/Ethnicity
def barchart_avg_scores_by_race(df):
    avg_scores = df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_scores.plot(x='race/ethnicity', kind='bar', ax=ax)
    ax.set_title('Average Scores by Race/Ethnicity')
    ax.set_xlabel('Race/Ethnicity')
    ax.set_ylabel('Average Score')
    save_fig(fig, 'barchart_avg_scores_by_race')

# 6. Distribution Plot (Histogram): Score distributions
def histograms_scores(df):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for i, subject in enumerate(['math score', 'reading score', 'writing score']):
        sns.histplot(df[subject], kde=True, ax=axes[i], bins=20)
        axes[i].set_title(f'{subject.title()} Distribution')
        axes[i].set_xlabel('Score')
        axes[i].set_ylabel('Count')
    fig.suptitle('Score Distributions', fontsize=18)
    save_fig(fig, 'histograms_scores')

# 7. Correlation Heatmap
def correlation_heatmap(df):
    corr = df[['math score', 'reading score', 'writing score']].corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap='Blues', vmin=0, vmax=1, square=True, ax=ax)
    ax.set_title('Correlation Heatmap of Scores')
    save_fig(fig, 'correlation_heatmap')

# 8. Grouped Bar Chart: Test Preparation Effect on Scores by Gender
def grouped_barchart_testprep_by_gender(df):
    avg_scores = df.groupby(['gender', 'test preparation course'])[['math score', 'reading score', 'writing score']].mean().reset_index()
    melted = avg_scores.melt(id_vars=['gender', 'test preparation course'], var_name='Subject', value_name='Average Score')
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(data=melted, x='Subject', y='Average Score', hue='test preparation course', errorbar=None, ax=ax)
    ax.set_title('Test Preparation Effect on Scores by Gender')
    ax.set_xlabel('Subject')
    ax.set_ylabel('Average Score')
    ax.legend(title='Test Preparation Course')
    save_fig(fig, 'grouped_barchart_testprep_by_gender')

# ---- Run all visualizations ----
boxplot_scores_by_gender(df)
boxplot_scores_by_testprep(df)
barchart_avg_scores_by_parent_edu(df)
barchart_avg_scores_by_lunch(df)
barchart_avg_scores_by_race(df)
histograms_scores(df)
correlation_heatmap(df)
grouped_barchart_testprep_by_gender(df)
