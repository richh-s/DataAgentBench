code = """import pandas as pd
import json
import dateutil.parser

# Load data
with open(locals()['var_function-call-782064260025852418'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Print unique indices to see what we are dealing with
print("Unique Indices:", df['Index'].unique())

# Attempt to parse dates. 
# Since formats are mixed, we can use pd.to_datetime with errors='coerce' and infer_datetime_format=True, 
# or apply dateutil.parser.parse. dateutil is slower but safer for mixed formats.
# Let's try pd.to_datetime first as it is faster.
# However, given the specific formats like "January 02, 1987 at 12:00 AM", pandas might struggle without a format string or flexible parsing.
# Let's use a custom parser or dateutil.
from dateutil import parser
def parse_date(d):
    try:
        return parser.parse(d)
    except:
        return None

# To speed up, we can find unique date strings and parse them once
unique_dates = df['Date'].unique()
date_map = {d: parse_date(d) for d in unique_dates}
df['Date'] = df['Date'].map(date_map)

# Filter >= 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Sort
df = df.sort_values(by=['Index', 'Date'])

# Check for nulls in CloseUSD
print("Null CloseUSD count:", df['CloseUSD'].isnull().sum())

# Ensure CloseUSD is float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with missing CloseUSD or Price <= 0
df = df[df['CloseUSD'] > 0]

# Strategy: Monthly investment.
# We need to pick one day per month. Let's pick the first available trading day of each month.
df['YearMonth'] = df['Date'].dt.to_period('M')

# Group by Index and YearMonth, take the first entry
monthly_investments = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate returns for each index
results = []
for idx in monthly_investments['Index'].unique():
    idx_data = monthly_investments[monthly_investments['Index'] == idx]
    
    # Check if data covers a reasonable range (e.g. starts near 2000 if available)
    # The prompt says "since 2000". If an index started later, we calculate from when it started.
    
    # Investment details
    investments = idx_data['CloseUSD'].tolist() # Price at each investment
    # Assume $1 investment each month
    # Units bought = 1 / Price
    units = [1/p for p in investments]
    total_units = sum(units)
    total_invested = len(units) # $1 * number of months
    
    if total_invested == 0:
        continue
        
    # Final value
    # We need the latest price available in the dataset for this index, not just the monthly first.
    # But usually the monthly first of the last month is close enough, or we can get the absolute last date.
    last_price = df[df['Index'] == idx].iloc[-1]['CloseUSD']
    
    final_value = total_units * last_price
    
    # ROI
    roi = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'ROI': roi
    })

results_df = pd.DataFrame(results).sort_values(by='ROI', ascending=False)

print("__RESULT__:")
print(json.dumps(results_df.head(10).to_dict(orient='records')))"""

env_args = {'var_function-call-6614466468539824704': ['index_info'], 'var_function-call-6614466468539823285': ['index_trade'], 'var_function-call-4749975929176175058': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4749975929176178023': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-5062678747963144670': [{'count_star()': '104224'}], 'var_function-call-782064260025852418': 'file_storage/function-call-782064260025852418.json'}

exec(code, env_args)
