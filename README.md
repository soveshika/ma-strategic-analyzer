## Finance Context
Observed patterns, with possible explanations:
- Deal activity rose sharply after 2009, coinciding with the near-zero interest rate period. This dataset contains no financing data, so the link is contextual.
- Of the 341 rows where a country is recorded, 248 are the United States. Note that 77% of rows have no country recorded at all.
- Deal volume falls after 1999 and after 2008, consistent with wider market cycles.

## How to Run
```bash
# Clone the repo
git clone <your-repo-url>
cd ma_predictor

# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run in order
python3 explore.py          # (optional) inspect the raw data
python3 db_setup.py         # build the SQLite database
python3 sql_queries.py      # run core queries
python3 analysis.py         # print the strategic insights report
python3 visualizations.py   # generate the 4 charts
```

## Author
Built by Sonu Ravish — MSc Strategy Business Management | AI Engineer Aspirant
