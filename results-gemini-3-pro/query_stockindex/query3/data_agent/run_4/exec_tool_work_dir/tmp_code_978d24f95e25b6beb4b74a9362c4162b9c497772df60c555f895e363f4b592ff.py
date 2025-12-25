code = """import pandas as pd
import json
import datetime

# Load data
file_path = locals()['var_function-call-15093468966041299533']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Dates
# The dates are mixed format. pd.to_datetime should handle it.
# We will use dayfirst=False as defaults, but some might be day first?
# "31 Dec 1986", "January 02, 1987", "1987-01-05"
# All look like standard US or unambiguous formats.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Sort by Date
df = df.sort_values(['Index', 'Date'])

# Define function to calculate DCA return
def calculate_dca_return(group):
    # Resample to monthly. We take the first available data point of each month.
    # To do this, we can set index to Date, then resample.
    # But we have multiple indices. We are inside a groupby, so 'Index' is constant.
    g = group.set_index('Date')
    # Resample to Month Start ('MS'). 
    # But real trading might not happen on 1st. We want the first trading day.
    # We can use 'resample(...).first()' which gives the first valid value in that bin.
    monthly_data = g.resample('MS').first()
    
    # Drop NaNs if any (e.g. empty months?)
    monthly_data = monthly_data.dropna(subset=['Adj Close'])
    
    if monthly_data.empty:
        return None
    
    # Investment strategy: Buy fixed amount (e.g. 1 unit of currency) every month.
    # Units bought = 1 / Price
    monthly_data['Units'] = 1.0 / monthly_data['Adj Close']
    
    total_units = monthly_data['Units'].sum()
    total_invested = len(monthly_data) * 1.0
    
    # Final value = Total Units * Last Available Price
    # We should use the last price of the entire dataset for this index, not just the monthly firsts.
    # Actually, the 'current' value of the portfolio is based on the latest price.
    last_price = group.iloc[-1]['Adj Close']
    
    final_value = total_units * last_price
    
    roi = (final_value - total_invested) / total_invested
    
    return roi

# Calculate returns
results = []
indices = df['Index'].unique()

for idx in indices:
    group = df[df['Index'] == idx]
    roi = calculate_dca_return(group)
    if roi is not None:
        results.append({'Index': idx, 'ROI': roi})

# Sort results
results_df = pd.DataFrame(results).sort_values('ROI', ascending=False)

# Mapping (based on previous analysis)
mapping = {
    "J203.JO": {"Exchange": "Johannesburg Stock Exchange", "Country": "South Africa"},
    "N225": {"Exchange": "Tokyo Stock Exchange", "Country": "Japan"},
    "GSPTSE": {"Exchange": "Toronto Stock Exchange", "Country": "Canada"},
    "NSEI": {"Exchange": "National Stock Exchange of India", "Country": "India"},
    "GDAXI": {"Exchange": "Frankfurt Stock Exchange", "Country": "Germany"},
    "IXIC": {"Exchange": "NASDAQ", "Country": "United States"},
    "HSI": {"Exchange": "Hong Kong Stock Exchange", "Country": "Hong Kong"},
    "NYA": {"Exchange": "New York Stock Exchange", "Country": "United States"},
    "000001.SS": {"Exchange": "Shanghai Stock Exchange", "Country": "China"},
    "SSMI": {"Exchange": "SIX Swiss Exchange", "Country": "Switzerland"},
    "TWII": {"Exchange": "Taiwan Stock Exchange", "Country": "Taiwan"},
    "N100": {"Exchange": "Euronext", "Country": "Europe"}, # Or France/Netherlands/Belgium...
    "399001.SZ": {"Exchange": "Shenzhen Stock Exchange", "Country": "China"}
}

top_5 = results_df.head(5).copy()
top_5['Country'] = top_5['Index'].map(lambda x: mapping.get(x, {}).get('Country', 'Unknown'))
top_5['ROI_Percent'] = top_5['ROI'] * 100

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-5293628446074717249': ['index_info'], 'var_function-call-5293628446074718162': ['index_trade'], 'var_function-call-4876716323590813781': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4876716323590814276': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-15582080887316221947': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15582080887316220318': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15093468966041299533': 'file_storage/function-call-15093468966041299533.json'}

exec(code, env_args)
