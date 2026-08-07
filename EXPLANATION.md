# M&A Strategic Analyser — How It Works

A dataset of 1,455 acquisitions by 14 major technology companies,
loaded into SQLite and analysed for patterns in deal activity.

The question I wanted to answer: **do big tech acquisition patterns
follow the wider economic cycle?**

This file explains how the project is built, what I found, and — just
as importantly — what I got wrong along the way.

## Pipeline

The project runs as five separate scripts rather than one notebook:

| Script | Purpose |
|---|---|
| `explore.py` | Inspect the raw CSV. Run once, throwaway. |
| `db_setup.py` | Load the CSV into SQLite. Run once. |
| `sql_queries.py` | Core queries against the database. |
| `analysis.py` | Print the strategic insights report. |
| `visualizations.py` | Generate four charts. |

They are separate because they have different lifespans. Exploration is
disposable. The database build runs once. Analysis and charts get
re-run repeatedly while you refine them.

**Why SQLite and not just pandas?** For 1,455 rows, pandas alone would
be enough. I used SQL because the queries read more clearly as
statements of intent, and because it matches how this analysis would be
done at real scale.

## What I Learned About the Data

I took this dataset from Kaggle and assumed it was reliable because the
source looked legitimate.

In `explore.py` I ran a missing-value check:

```python
print(df.isnull().sum())
```

It returned zero missing values across every column, so I moved on to
writing the queries.

That check was misleading. In this file, missing data is not stored as
null — it is stored as the character `-`. Pandas treats `-` as a valid
string, so `isnull()` counts it as present data.

The real missing rates are:

| Column | Missing |
|---|---|
| Category | 99.3% |
| Country | 76.6% |
| Derived Products | 72.3% |
| Acquisition Price | 64.9% |
| Business | 18.8% |

The Price column has a second problem: 127 rows contain the word
`undisclosed`. Mixed with numbers, this forces the whole column to be
stored as text.

**Lesson:** `isnull()` only finds values that are actually null.
Placeholder characters have to be checked for separately.

## A Wrong Value in the Source Data

Only 383 of 1,455 rows have a usable numeric price — about 26%.

Sorting those by size revealed a problem. Twitter's acquisition of
Periscope is recorded at $50,100,000,000. That would make it the
second-largest deal in the entire dataset, above IBM/Red Hat and
Microsoft/LinkedIn.

Twitter paid roughly $50-100 million for Periscope. The recorded figure
is wrong by about three orders of magnitude — most likely a data entry
error in the original scrape.

My current scripts do not analyse deal prices, so no published result is
affected. But any future price analysis would need this row corrected or
removed first.

**Lesson:** sorting a numeric column by size is a fast way to find
entry errors. The largest and smallest values are where mistakes hide.

## Separating Observation From Explanation

Two of my original conclusions claimed more than the data could show.

**The geography claim.** I wrote that the results reflected Silicon
Valley's dominance in tech innovation. The count was correct — of the
341 rows with a country recorded, 248 are the United States. But 77% of
rows have no country at all. So the finding is really about which rows
happened to have a country filled in, not about global M&A patterns.

**The interest rate claim.** I wrote that the post-2009 rise was linked
to quantitative easing and cheap financing. The rise is real. But this
dataset contains no interest rate data, no financing cost data, and no
deal structure data. The explanation came from outside the data, not
from it.

Both explanations may well be correct. The problem was stating them as
if the analysis had demonstrated them.

**Lesson:** an observation is what the data shows. An explanation is
what I believe causes it. They need to be written as two separate
things.

## Re-reading the Timeline

My analysis script printed: "Acquisitions surged from 38 in 2009 to 100
in 2014." Both numbers are correct, but the sentence implies a steady
six-year climb. The actual yearly counts tell a different story:

| Year | Deals |
|---|---|
| 2009 | 38 |
| 2010 | 93 |
| 2011 | 95 |
| 2012 | 68 |
| 2013 | 85 |
| 2014 | 100 |

Almost the entire increase happens in a single year — 2009 to 2010.
After that the level holds roughly flat, with 2014 as a modest new high.

This matters, because a gradual six-year climb and a one-year jump
followed by a plateau have different possible causes. Quoting only the
first and last values hid that.

The dot-com pattern held up better: 41 deals in 1999, falling to 20 in
2000.

**Lesson:** quoting endpoints can describe a shape that isn't there.
Look at every year between them.

## What This Analysis Cannot Tell You

- **It covers 14 companies only.** Microsoft, Google, IBM, HP, Apple,
  Amazon, Facebook, Twitter, eBay, Adobe, Citrix, Red Hat, BlackBerry
  and Disney. Findings describe these companies, not the tech sector.

- **Deal counts are not deal value.** One $19bn acquisition counts the
  same as one small team hire. With price missing in 65% of rows, value
  cannot be measured.

- **Company size is not controlled for.** Microsoft leading on count
  partly reflects that Microsoft is large and old. Count alone does not
  measure how aggressive an acquirer is.

- **The data ends in 2021.** The COVID marker on the timeline chart has
  almost no data after it.

- **Recording is uneven.** Older entries carry less detail than recent
  ones, so apparent trends may partly reflect how the source was
  compiled.
