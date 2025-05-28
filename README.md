# Student Performance Visualization Dashboard

This project analyzes and visualizes student performance data across different demographic factors and test scores. The analysis includes gender-based performance, race/ethnicity comparisons, parental education impact, and test preparation course effectiveness.

## Project Structure

```
visualization-dashboard/
├── StudentsPerformance.csv    # Dataset containing student performance data
├── visualization_analysis.py  # Main analysis script
├── env.yaml          # Conda environment configuration
└── README.md                 # This file
```

## Generated Visualizations

The script generates the following interactive HTML visualizations:
- Box plots showing score distributions
- Bar charts showing average scores
- Summary statistics tables

## Setup Instructions

### 1. Install Conda
If you haven't installed Conda yet, download and install it from [Anaconda's website](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

### 2. Create and Activate the Environment

```bash
# Create the conda environment from the yaml file
conda env create -f env.yaml

# Activate the environment
conda activate datavisuals
```

### 3. Run the Analysis

```bash
# Run the visualization script
python visualization_analysis.py
```

## Generated Files

After running the script, the following HTML files will be generated:
- `boxplot_gender.html`
- `barchart_gender.html`
- `boxplot_race_ethnicity.html`
- `barchart_race_ethnicity.html`
- `boxplot_parental_level_of_education.html`
- `barchart_parental_level_of_education.html`
- `boxplot_test_preparation_course.html`
- `barchart_test_preparation_course.html`
- `gender_summary_stats.html`

## Data Analysis

The analysis includes:
1. Gender-based performance analysis
2. Race/Ethnicity group comparisons
3. Impact of parental education level
4. Effect of test preparation courses

Each visualization is interactive and allows you to:
- Hover over data points to see exact values
- Zoom in/out
- Pan across the visualization
- Download the plot as a PNG file
- Toggle different elements on/off

## Requirements

- Python 3.9
- pandas 2.1.0
- plotly 5.17.0

All dependencies are automatically installed when creating the conda environment from the `environment.yaml` file.

## Troubleshooting

If you encounter any issues:

1. Make sure you have activated the correct conda environment:
   ```bash
   conda activate datavisuals
   ```

2. Verify that all files are in the correct directory:
   ```bash
   ls
   ```

3. Check if the CSV file is properly formatted and accessible:
   ```bash
   head -n 5 StudentsPerformance.csv
   ```

4. If you need to update the environment:
   ```bash
   conda env update -f environment.yaml
   ``` 