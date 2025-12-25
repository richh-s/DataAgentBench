code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-7669815343368743674'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Fix date parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD', 'Date'])

# Monthly investment simulation
results = []
indices = df['Index'].unique()

for idx in indices:
    sub_df = df[df['Index'] == idx].sort_values('Date')
    
    # Group by Year-Month and take first entry
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    monthly_invest = sub_df.groupby('YearMonth').first().reset_index()
    
    # Calculate shares bought ($1 per month)
    monthly_invest['Shares'] = 1.0 / monthly_invest['CloseUSD']
    
    total_shares = monthly_invest['Shares'].sum()
    total_invested = len(monthly_invest)
    
    # Final value
    last_price = sub_df.iloc[-1]['CloseUSD']
    final_value = total_shares * last_price
    
    # ROI = (Final Value - Total Invested) / Total Invested
    if total_invested > 0:
        roi = (final_value - total_invested) / total_invested
    else:
        roi = 0
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Start_Date': sub_df['Date'].iloc[0],
        'End_Date': sub_df['Date'].iloc[-1]
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('ROI', ascending=False)

# Mapping
country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Europe',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

results_df['Country'] = results_df['Index'].map(country_map)

print("__RESULT__:")
print(results_df[['Index', 'Country', 'ROI', 'Start_Date', 'End_Date']].head(10).to_json(orient='records', date_format='iso'))"""

env_args = {'var_function-call-13441364534165871433': ['index_info'], 'var_function-call-13441364534165871896': ['index_trade'], 'var_function-call-8023527505821607131': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8023527505821609228': [{'IndexSymbol': 'J203.JO'}, {'IndexSymbol': 'N225'}, {'IndexSymbol': 'GSPTSE'}, {'IndexSymbol': 'NSEI'}, {'IndexSymbol': 'GDAXI'}, {'IndexSymbol': 'IXIC'}, {'IndexSymbol': 'HSI'}, {'IndexSymbol': 'NYA'}, {'IndexSymbol': '000001.SS'}, {'IndexSymbol': 'SSMI'}, {'IndexSymbol': 'TWII'}, {'IndexSymbol': 'N100'}, {'IndexSymbol': '399001.SZ'}], 'var_function-call-7669815343368743674': 'file_storage/function-call-7669815343368743674.json'}

exec(code, env_args)
