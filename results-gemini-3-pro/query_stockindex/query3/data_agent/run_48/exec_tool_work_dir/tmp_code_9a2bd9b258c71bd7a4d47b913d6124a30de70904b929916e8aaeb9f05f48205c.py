code = """import pandas as pd
import json

# Load the data
with open('var_function-call-16915743951299197497.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Date
# The formats are mixed. pd.to_datetime is usually smart enough.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)

# Filter for >= 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01', tz='UTC')]

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with missing CloseUSD or Date
df = df.dropna(subset=['CloseUSD', 'Date'])

# List of all indices
indices = df['Index'].unique()

results = []

for idx in indices:
    sub_df = df[df['Index'] == idx].sort_values('Date')
    
    if sub_df.empty:
        continue
        
    # We want to invest monthly. 
    # Let's create a 'Month' column to identify unique months
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    
    # Group by YearMonth and take the first entry (first trading day of the month)
    monthly_investments = sub_df.groupby('YearMonth').first().reset_index()
    
    # Calculate investment
    monthly_investment_amount = 100.0
    monthly_investments['Units_Bought'] = monthly_investment_amount / monthly_investments['CloseUSD']
    
    total_units = monthly_investments['Units_Bought'].sum()
    total_invested = len(monthly_investments) * monthly_investment_amount
    
    # Final value
    # We should use the very last available price for the index, not necessarily the first day of the last month.
    # The simulation implies holding until "now" or end of data.
    last_price = sub_df.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    overall_return_pct = ((final_value - total_invested) / total_invested) * 100
    
    results.append({
        'Index': idx,
        'Return_Pct': overall_return_pct,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Start_Date': sub_df.iloc[0]['Date'],
        'End_Date': sub_df.iloc[-1]['Date']
    })

# Sort by Return_Pct descending
results_df = pd.DataFrame(results).sort_values('Return_Pct', ascending=False)

print("__RESULT__:")
print(results_df.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-14617990700424002054': ['index_info'], 'var_function-call-4135645301445920250': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-16673487984124826334': ['index_trade'], 'var_function-call-3415968944644571791': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-6580303457518588185': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-7063044302034232475': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15938523053680967718': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-2457982519986606704': [{'count_star()': '104224'}], 'var_function-call-16915743951299197497': 'file_storage/function-call-16915743951299197497.json'}

exec(code, env_args)
