## Running the Analysis and Generating the Report

### 1. Set Up the Environment
If you haven't already, create and activate the conda environment:

```bash
conda env create -f env.yaml
conda activate datavisuals
```

### 2. Run the Visualization Script
This will generate all required high-resolution PNG figures in the `figures/` directory:

```bash
python student_performance_dashboard.py
```

### 3. Compile the LaTeX Report
Make sure you have a LaTeX distribution installed (e.g., TeX Live, MiKTeX, or use Overleaf). The LaTeX file is `Student_Performance_Report.tex`.

- **If using the command line:**
  1. Ensure the `figures/` folder (with all PNGs) is in the same directory as the `.tex` file.
  2. Run:
     ```bash
     pdflatex Student_Performance_Report.tex
     ```
- **If using Overleaf:**
  1. Upload `Student_Performance_Report.tex` and the entire `figures/` folder.
  2. Click "Recompile" to generate the PDF.

### 4. Output
- The PDF report will be generated, including all summary statistics, key insights, and visualizations.

## Troubleshooting
- If you see errors about missing image files, make sure you have run `student_performance_dashboard.py` and that the `figures/` directory contains all required PNGs.
- If you update the data or code, rerun the script and recompile the LaTeX report. 