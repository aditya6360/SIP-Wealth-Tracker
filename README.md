# SIP Wealth Tracker & Market Analytics 📈💰

An end-to-end Data Engineering and Analytics project focused on financial markets. This project tracks a Systematic Investment Plan (SIP) in index funds (NiftyBees) and analyzes the broader market impact involving Gold and Crude Oil over a 5-year period.

## Project Overview
- **ETL Pipeline**: Extracted 5 years of historical market data. Transformed daily ticker data into monthly SIP investment logic (₹5000/month).
- **Market Analysis**: Normalized prices of Nifty 50, Gold, and Crude Oil to a base of 100 to visualize comparative growth and market impacts.
- **Database Storage**: Stored historical investment records into an SQLite database (`wealth_tracker.sqlite`).

## Technologies Used
- **Python** (Pandas, yfinance, Matplotlib)
- **SQL** (SQLite)
- **Power BI** (For Dashboarding - *Add your Power BI screenshot here*)

## Files Included
- `sip_etl_project.py`: ETL script that calculates SIP logic and generates monthly portfolios.
- `data_analsis_2026.py`: Script to fetch and normalize historical data (Nifty, Gold, Crude Oil) using `yfinance` API.
- `sip_sql.py`: Handles database interaction for the wealth tracker.
- `niftybees_5yr_data.csv` & `cleaned_market_data.csv`: Raw and cleaned datasets.
- `sip_portfolio_ready.csv`: Final processed dataset for BI tools.
- `wealth_tracker.sqlite`: Database file storing the SIP portfolio.

## How to Run
```bash
python sip_etl_project.py
python data_analsis_2026.py
```
