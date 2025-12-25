code = """import pandas as pd
import json
import dateutil.parser

# Load data
file_path = locals()['var_function-call-12827950368100656920']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# robust date parsing
# Since formats are mixed, we can try using dateutil or pandas flexibility
# Let's try pandas first. It handles many formats.
# Some formats: "31 Dec 1986, 00:00", "January 02, 1987 at 12:00 AM", "1987-01-05 00:00:00"
# "06 Jan 1987, 00:00"
# pd.to_datetime with format='mixed' (if available) or inferred.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback to applying dateutil.parser.parse if 'mixed' is not supported in installed pandas version
    from dateutil import parser
    df['Date'] = df['Date'].apply(lambda x: parser.parse(x))

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01'].copy()
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Create YearMonth
df['YearMonth'] = df['Date'].dt.to_period('M')

# Get first trading day of each month for each index
monthly_investments = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate investment
monthly_investments['Units'] = 100.0 / monthly_investments['CloseUSD']
monthly_investments['Invested'] = 100.0

# Aggregate per index
results = []
indices = df['Index'].unique()

for idx in indices:
    idx_data = monthly_investments[monthly_investments['Index'] == idx]
    total_units = idx_data['Units'].sum()
    total_invested = idx_data['Invested'].sum()
    
    # Get last price
    # We use the full df to find the very last available price, not just the first of the last month
    last_price = df[df['Index'] == idx].iloc[-1]['CloseUSD']
    
    portfolio_value = total_units * last_price
    
    roi = (portfolio_value - total_invested) / total_invested if total_invested > 0 else 0
    
    results.append({
        'Index': idx,
        'Total_Invested': total_invested,
        'Final_Value': portfolio_value,
        'ROI': roi,
        'ROI_Percent': roi * 100,
        'Start_Date': idx_data['Date'].min().strftime('%Y-%m-%d'),
        'End_Date': df[df['Index'] == idx].iloc[-1]['Date'].strftime('%Y-%m-%d')
    })

results_df = pd.DataFrame(results).sort_values('ROI', ascending=False)

print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-6913882852831468956': ['index_info'], 'var_function-call-9794522280364578224': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3114065141326309353': ['index_trade'], 'var_function-call-13532260489223867404': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-6723670047784191364': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-9646600457132397225': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8079314028453376951': [{'count_star()': '104224'}], 'var_function-call-12827950368100656920': 'file_storage/function-call-12827950368100656920.json'}

exec(code, env_args)
