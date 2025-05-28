import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read the CSV file
df = pd.read_csv('StudentsPerformance.csv')

# Create a function to generate box plots for each factor
def create_score_boxplots(df, factor, title):
    fig = make_subplots(rows=1, cols=3, 
                       subplot_titles=('Math Scores', 'Reading Scores', 'Writing Scores'))
    
    # Math scores
    fig.add_trace(
        go.Box(y=df['math score'], x=df[factor], name='Math'),
        row=1, col=1
    )
    
    # Reading scores
    fig.add_trace(
        go.Box(y=df['reading score'], x=df[factor], name='Reading'),
        row=1, col=2
    )
    
    # Writing scores
    fig.add_trace(
        go.Box(y=df['writing score'], x=df[factor], name='Writing'),
        row=1, col=3
    )
    
    fig.update_layout(
        title_text=f'Test Scores Distribution by {title}',
        height=600,
        showlegend=False
    )
    
    return fig

# Create a function to generate bar charts for average scores
def create_average_score_bars(df, factor, title):
    # Calculate average scores for each category
    avg_scores = df.groupby(factor)[['math score', 'reading score', 'writing score']].mean().reset_index()
    
    # Melt the dataframe for easier plotting
    avg_scores_melted = pd.melt(avg_scores, 
                               id_vars=[factor],
                               value_vars=['math score', 'reading score', 'writing score'],
                               var_name='Subject',
                               value_name='Average Score')
    
    # Create the bar chart
    fig = px.bar(avg_scores_melted, 
                 x=factor, 
                 y='Average Score',
                 color='Subject',
                 barmode='group',
                 title=f'Average Test Scores by {title}')
    
    return fig

# Generate visualizations for each factor
factors = {
    'gender': 'Gender',
    'race/ethnicity': 'Race/Ethnicity',
    'parental level of education': 'Parental Education',
    'test preparation course': 'Test Preparation Course'
}

# Create and save all visualizations
for factor, title in factors.items():
    # Create safe filename by replacing problematic characters
    safe_factor = factor.replace('/', '_').replace(' ', '_')
    
    # Create box plots
    box_fig = create_score_boxplots(df, factor, title)
    box_fig.write_html(f'boxplot_{safe_factor}.html')
    
    # Create bar charts
    bar_fig = create_average_score_bars(df, factor, title)
    bar_fig.write_html(f'barchart_{safe_factor}.html')

# Create a summary statistics table
summary_stats = df.groupby('gender')[['math score', 'reading score', 'writing score']].agg(['mean', 'median', 'std']).round(2)
summary_stats.to_html('gender_summary_stats.html')

# Print some basic statistics
print("\nGender-based Analysis:")
print(df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().round(2))

print("\nRace/Ethnicity Analysis:")
print(df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean().round(2))

print("\nParental Education Analysis:")
print(df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().round(2))

print("\nTest Preparation Course Analysis:")
print(df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().round(2)) 