## Finance Context
Each insight is grounded in financial theory:
- Post-2008 acquisition surge linked to **Quantitative Easing** and near-zero interest rates
- Geographic concentration reflects **Silicon Valley ecosystem** dominance in tech innovation
- Deal activity cycles directly correlate with **capital market conditions**

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
Built by Sonu Ravish — MSc Finance | AI Engineer Aspirant