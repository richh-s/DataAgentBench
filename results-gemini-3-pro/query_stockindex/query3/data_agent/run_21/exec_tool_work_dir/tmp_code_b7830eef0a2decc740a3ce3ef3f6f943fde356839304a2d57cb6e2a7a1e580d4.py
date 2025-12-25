code = """import pandas as pd
import json
import dateutil.parser

# Load data
file_path = locals()['var_function-call-5694327615127927862']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are mixed format. pd.to_datetime with infer_datetime_format might be slow or fail.
# Let's try flexible parsing.
# The formats seem to be "DD Mon YYYY, HH:MM" or "Month DD, YYYY at HH:MM AM/PM"
# We can just use pd.to_datetime(..., format='mixed') which is available in newer pandas, 
# but if the environment is older, we might need dateutil.
# Let's try basic pd.to_datetime first.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback if format='mixed' is not supported or fails
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01'].copy()
df = df.sort_values(['Index', 'Date'])

# Define function to calculate return
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    if sub.empty:
        continue
    
    # Identify monthly investment dates
    # We want the first available trading day of each month
    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    
    # Group by YearMonth and take the first entry
    monthly_investments = sub.groupby('YearMonth').first().reset_index()
    
    # Investment calculation
    monthly_amount = 100.0
    monthly_investments['Units'] = monthly_amount / monthly_investments['Adj Close']
    
    total_units = monthly_investments['Units'].sum()
    total_invested = len(monthly_investments) * monthly_amount
    
    # Final value
    # Using the last available price in the dataset for that index
    final_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * final_price
    
    roi = (final_value - total_invested) / total_invested if total_invested > 0 else 0
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'FinalValue': final_value,
        'TotalInvested': total_invested
    })

# Sort by ROI
results_df = pd.DataFrame(results)
top_5 = results_df.sort_values('ROI', ascending=False).head(5)

# Mapping
mapping = {
    "NYA": "United States",
    "IXIC": "United States",
    "HSI": "Hong Kong",
    "000001.SS": "China",
    "N225": "Japan",
    "GDAXI": "Germany",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "399001.SZ": "China",
    "TWII": "Taiwan",
    "SSMI": "Switzerland",
    "N100": "Europe",
    "J203.JO": "South Africa"
}

final_output = []
for _, row in top_5.iterrows():
    idx_name = row['Index']
    country = mapping.get(idx_name, "Unknown")
    final_output.append({
        "Index": idx_name,
        "Country": country,
        "ROI_Percent": round(row['ROI'] * 100, 2)
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-18349591448005712191': ['index_info'], 'var_function-call-18349591448005709844': ['index_trade'], 'var_function-call-14289002518235645643': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-14289002518235643914': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-1388220677746674582': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-5694327615127927862': 'file_storage/function-call-5694327615127927862.json'}

exec(code, env_args)
