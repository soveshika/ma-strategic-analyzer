# M&A Strategic Intelligence Analyzer

## Overview
A data analysis project combining SQL, Python and Finance domain 
knowledge to analyze 1,455 real M&A transactions from 14 major 
tech companies including Microsoft, Google, Apple and Amazon.

## Key Findings
- **Microsoft** is the most aggressive acquirer with 258 deals
- **Dot-com crash (2000)** caused a 51% drop in deal activity
- **Post-2008 QE era** drove acquisitions to a peak of 100 deals in 2014
- **248 deals** targeted US companies — reflecting Silicon Valley dominance

## Tech Stack
- **Python** — Data analysis and visualization
- **SQL (SQLite)** — Database design and querying
- **Pandas** — Data manipulation
- **Matplotlib & Seaborn** — Visualizations

## Project Structure
```
ma_predictor/
├── explore.py          # Initial data exploration
├── db_setup.py         # SQL database creation
├── sql_queries.py      # Financial SQL queries
├── visualizations.py   # 4 analytical charts
├── analysis.py         # Strategic insights report
└── README.md           # Project documentation
```

## Finance Context
Each insight is grounded in financial theory:
- Post-2008 acquisition surge linked to **Quantitative Easing** 
  and near-zero interest rates
- Geographic concentration reflects **Silicon Valley ecosystem** 
  dominance in tech innovation
- Deal activity cycles directly correlate with **capital market 
  conditions**

## How to Run
```bash
# Clone the repo
git clone <your-repo-url>

# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run in order
python3 db_setup.py
python3 sql_queries.py
python3 analysis.py
python3 visualizations.py
```

## Author
Built by [Your Name] — MSc Finance | AI Engineer Aspirant