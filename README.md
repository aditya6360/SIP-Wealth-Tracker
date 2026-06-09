# SIP Market Analytics & Wealth Tracker

A Python-based ETL pipeline that tracks and analyzes Systematic Investment Plans (SIP) 
across major Indian market assets over a 5-year period.

## Features
- Automated data extraction for Nifty 50, Gold, and Crude Oil (1,250+ trading days)
- Normalized value comparison to identify long-term growth trends
- SQLite database integration for storing and querying SIP investment records
- Data visualizations for asset performance comparison

## Tech Stack
- Python (Pandas, yfinance)
- SQLite
- Matplotlib / Seaborn

## Key Insights
- Compared 5-year returns across 3 asset classes using normalized indexing
- Identified growth trends to support data-driven investment decisions

## How to Run
```bash
pip install pandas yfinance matplotlib
python sip_tracker.py
```
