code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load the trade data
trade_data_file = locals()['var_functions.query_db:10']
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame and convert date
df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df_filtered = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Map indices to countries (from our previous analysis)
index_mapping = {
    "000001.SS": {"country": "China", "name": "Shanghai Composite"},
    "399001.SZ": {"country": "China", "name": "Shenzhen Component"},
    "GDAXI": {"country": "Germany", "name": "DAX"},
    "GSPTSE": {"country": "Canada", "name": "S&P/TSX Composite"},
    "HSI": {"country": "Hong Kong", "name": "Hang Seng Index"},
    "IXIC": {"country": "USA", "name": "NASDAQ Composite"},
    "J203.JO": {"country": "South Africa", "name": "FTSE/JSE All Share"},
    "N100": {"country": "Netherlands", "name": "Euronext 100"},
    "N225": {"country": "Japan", "name": "Nikkei 225"},
    "NSEI": {"country": "India", "name": "NIFTY 50"},
    "NYA": {"country": "USA", "name": "NYSE Composite"},
    "SSMI": {"country": "Switzerland", "name": "Swiss Market Index"},
    "TWII": {"country": "Taiwan", "name": "TAIEX"}
}

# For each index, calculate Dollar-Cost Averaging (DCA) returns
# Assume $100 invested at the beginning of each month
monthly_investment = 100.0

dca_results = []

for idx in df_filtered['Index'].unique():
    idx_data = df_filtered[df_filtered['Index'] == idx].copy()
    
    # Sort by date
    idx_data = idx_data.sort_values('Date')
    
    # Extract year-month for grouping
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    
    # Get first trading day of each month (for monthly investment)
    monthly_data = idx_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_data) < 12:  # Need at least 1 year of data
        continue
    
    # Calculate DCA
    total_investment = 0.0
    total_units = 0.0
    
    for _, row in monthly_data.iterrows():
        price = float(row['CloseUSD'])
        if price > 0:
            units_bought = monthly_investment / price
            total_units += units_bought
            total_investment += monthly_investment
    
    # Calculate final value
    final_price = float(monthly_data.iloc[-1]['CloseUSD'])
    final_value = total_units * final_price
    
    # Calculate total return
    total_return = (final_value - total_investment) / total_investment if total_investment > 0 else 0
    
    dca_results.append({
        'Index': idx,
        'Country': index_mapping.get(idx, {}).get('country', 'Unknown'),
        'Name': index_mapping.get(idx, {}).get('name', idx),
        'TotalReturn': total_return,
        'NumMonths': len(monthly_data),
        'FinalValue': final_value,
        'TotalInvestment': total_investment
    })

# Create DataFrame and sort by total return
dca_df = pd.DataFrame(dca_results)
dca_df = dca_df.sort_values('TotalReturn', ascending=False)

# Get top 5
top_5 = dca_df.head(5)

print("Top 5 indices by DCA return since 2000:")
print(top_5[['Index', 'Name', 'Country', 'TotalReturn']].to_string(index=False))

print("__RESULT__:")
print(top_5[['Index', 'Name', 'Country', 'TotalReturn']].to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'Open': '1368.692993', 'High': '1407.517944', 'Low': '1361.213989', 'Close': '1406.370972', 'Adj Close': '1406.370972', 'CloseUSD': '225.01935552'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'Open': '1407.828979', 'High': '1433.780029', 'Low': '1398.322998', 'Close': '1409.682007', 'Adj Close': '1409.682007', 'CloseUSD': '225.54912112'}, {'Index': '000001.SS', 'Date': '2000-01-10 00:00:00', 'Open': '1531.712036', 'High': '1546.723022', 'Low': '1506.404053', 'Close': '1545.112061', 'Adj Close': '1545.112061', 'CloseUSD': '247.21792976'}, {'Index': '000001.SS', 'Date': '2000-01-12 00:00:00', 'Open': '1473.760986', 'High': '1489.280029', 'Low': '1434.995972', 'Close': '1438.02002', 'Adj Close': '1438.02002', 'CloseUSD': '230.0832032'}, {'Index': '000001.SS', 'Date': '2000-01-14 00:00:00', 'Open': '1426.223999', 'High': '1433.473999', 'Low': '1401.706055', 'Close': '1408.848022', 'Adj Close': '1408.848022', 'CloseUSD': '225.41568352'}, {'Index': '000001.SS', 'Date': '2000-01-19 00:00:00', 'Open': '1425.874023', 'High': '1443.671997', 'Low': '1425.142944', 'Close': '1440.723999', 'Adj Close': '1440.723999', 'CloseUSD': '230.51583984'}, {'Index': '000001.SS', 'Date': '2000-01-20 00:00:00', 'Open': '1443.093994', 'High': '1466.901001', 'Low': '1443.093994', 'Close': '1466.863037', 'Adj Close': '1466.863037', 'CloseUSD': '234.69808592'}, {'Index': '000001.SS', 'Date': '2000-01-27 00:00:00', 'Open': '1490.447021', 'High': '1506.921997', 'Low': '1485.234009', 'Close': '1506.766968', 'Adj Close': '1506.766968', 'CloseUSD': '241.08271488'}, {'Index': '000001.SS', 'Date': '2000-01-28 00:00:00', 'Open': '1514.557983', 'High': '1536.345947', 'Low': '1510.744995', 'Close': '1534.996948', 'Adj Close': '1534.996948', 'CloseUSD': '245.59951168'}, {'Index': '000001.SS', 'Date': '2000-02-14 00:00:00', 'Open': '1591.444946', 'High': '1674.131958', 'Low': '1587.817993', 'Close': '1673.942993', 'Adj Close': '1673.942993', 'CloseUSD': '267.83087888'}, {'Index': '000001.SS', 'Date': '2000-02-16 00:00:00', 'Open': '1674.936035', 'High': '1695.880981', 'Low': '1649.698975', 'Close': '1693.109009', 'Adj Close': '1693.109009', 'CloseUSD': '270.89744144'}, {'Index': '000001.SS', 'Date': '2000-02-17 00:00:00', 'Open': '1734.267944', 'High': '1770.880005', 'Low': '1615.629028', 'Close': '1640.649048', 'Adj Close': '1640.649048', 'CloseUSD': '262.50384768'}, {'Index': '000001.SS', 'Date': '2000-02-29 00:00:00', 'Open': '1728.135986', 'High': '1733.140991', 'Low': '1678.349976', 'Close': '1714.578003', 'Adj Close': '1714.578003', 'CloseUSD': '274.33248048'}, {'Index': '000001.SS', 'Date': '2000-03-01 00:00:00', 'Open': '1720.597046', 'High': '1721.140015', 'Low': '1692.509033', 'Close': '1704.85498', 'Adj Close': '1704.85498', 'CloseUSD': '272.7767968'}, {'Index': '000001.SS', 'Date': '2000-03-03 00:00:00', 'Open': '1728.35498', 'High': '1750.64502', 'Low': '1721.704956', 'Close': '1738.020996', 'Adj Close': '1738.020996', 'CloseUSD': '278.08335936'}, {'Index': '000001.SS', 'Date': '2000-03-06 00:00:00', 'Open': '1756.312988', 'High': '1762.828979', 'Low': '1678.744019', 'Close': '1681.084961', 'Adj Close': '1681.084961', 'CloseUSD': '268.97359376'}, {'Index': '000001.SS', 'Date': '2000-03-08 00:00:00', 'Open': '1699.462036', 'High': '1726.042969', 'Low': '1690.116943', 'Close': '1726.032959', 'Adj Close': '1726.032959', 'CloseUSD': '276.16527344'}, {'Index': '000001.SS', 'Date': '2000-03-13 00:00:00', 'Open': '1706.769043', 'High': '1729.006958', 'Low': '1706.348999', 'Close': '1728.886963', 'Adj Close': '1728.886963', 'CloseUSD': '276.62191408'}, {'Index': '000001.SS', 'Date': '2000-03-15 00:00:00', 'Open': '1680.296021', 'High': '1695.161987', 'Low': '1676.543945', 'Close': '1681.470947', 'Adj Close': '1681.470947', 'CloseUSD': '269.03535152'}, {'Index': '000001.SS', 'Date': '2000-03-27 00:00:00', 'Open': '1736.696045', 'High': '1776.020996', 'Low': '1736.696045', 'Close': '1775.91394', 'Adj Close': '1775.91394', 'CloseUSD': '284.1462304'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': [{'Index': '000001.SS', 'Exchange': 'Shanghai Stock Exchange', 'Country': 'China', 'Name': 'Shanghai Composite'}, {'Index': '399001.SZ', 'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China', 'Name': 'Shenzhen Component'}, {'Index': 'GDAXI', 'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany', 'Name': 'DAX'}, {'Index': 'GSPTSE', 'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada', 'Name': 'S&P/TSX Composite'}, {'Index': 'HSI', 'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong', 'Name': 'Hang Seng Index'}, {'Index': 'IXIC', 'Exchange': 'NASDAQ', 'Country': 'USA', 'Name': 'NASDAQ Composite'}, {'Index': 'J203.JO', 'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa', 'Name': 'FTSE/JSE All Share'}, {'Index': 'N100', 'Exchange': 'Euronext', 'Country': 'Netherlands', 'Name': 'Euronext 100'}, {'Index': 'N225', 'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan', 'Name': 'Nikkei 225'}, {'Index': 'NSEI', 'Exchange': 'National Stock Exchange of India', 'Country': 'India', 'Name': 'NIFTY 50'}, {'Index': 'NYA', 'Exchange': 'New York Stock Exchange', 'Country': 'USA', 'Name': 'NYSE Composite'}, {'Index': 'SSMI', 'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland', 'Name': 'Swiss Market Index'}, {'Index': 'TWII', 'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan', 'Name': 'TAIEX'}], 'var_functions.execute_python:20': {'total_records': 21342, 'date_min': '2000-01-03 00:00:00', 'date_max': '2021-06-02 00:00:00', 'unique_indices': 13, 'sample_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI']}}

exec(code, env_args)
