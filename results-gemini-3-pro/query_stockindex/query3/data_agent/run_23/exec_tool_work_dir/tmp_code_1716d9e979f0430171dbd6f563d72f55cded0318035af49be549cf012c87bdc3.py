code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-17603083438239921190']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are in mixed formats. pd.to_datetime should handle them.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)

# Filter since 2000
df = df[df['Date'] >= '2000-01-01']

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Define a function to calculate DCA return
def calculate_dca_return(group):
    # Resample to get the first trading day of each month
    # We can do this by creating a 'YearMonth' column and taking the first entry
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_investments = group.groupby('YearMonth').first().reset_index()
    
    monthly_amount = 100.0
    total_invested = 0.0
    total_units = 0.0
    
    for idx, row in monthly_investments.iterrows():
        price = float(row['CloseUSD'])
        if price > 0:
            units = monthly_amount / price
            total_units += units
            total_invested += monthly_amount
            
    # Final value
    last_price = float(group.iloc[-1]['CloseUSD'])
    final_value = total_units * last_price
    
    if total_invested == 0:
        return 0.0
        
    total_return_pct = (final_value - total_invested) / total_invested * 100
    return total_return_pct

# Apply to each index
results = []
for index_name, group in df.groupby('Index'):
    ret = calculate_dca_return(group.copy())
    results.append({'Index': index_name, 'Return': ret})

results_df = pd.DataFrame(results)
top_5 = results_df.sort_values('Return', ascending=False).head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-17173805272911110927': ['index_info'], 'var_function-call-11258561944770114786': ['index_trade'], 'var_function-call-5975765643861245394': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-13490034723944491712': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-15317456688879250410': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-11613631020039136316': [{'count_star()': '104224'}], 'var_function-call-17603083438239921190': 'file_storage/function-call-17603083438239921190.json'}

exec(code, env_args)
