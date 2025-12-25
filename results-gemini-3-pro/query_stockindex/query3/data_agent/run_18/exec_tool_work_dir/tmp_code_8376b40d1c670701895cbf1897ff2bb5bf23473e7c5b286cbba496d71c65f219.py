code = """import pandas as pd
import json
import dateutil.parser

# Load the data
file_path = locals()['var_function-call-14002920760052114969']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates flexibly
def parse_date(date_str):
    try:
        return dateutil.parser.parse(date_str)
    except:
        return None

df['Date'] = df['Date'].apply(parse_date)

# Filter for data since 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Sort by Index and Date
df = df.sort_values(by=['Index', 'Date'])

# Check for missing CloseUSD
# If CloseUSD is missing, we might have to use Close, but mixed currencies is bad.
# Let's count missing CloseUSD per index
missing_usd = df[df['CloseUSD'].isna()]['Index'].value_counts()
print("Missing CloseUSD counts:")
print(missing_usd)

# We will proceed with CloseUSD. If mostly missing for an index, we might drop it or use Close if reasonable.
# Assuming CloseUSD is available or we can fallback to Close if it's USD (e.g. US indices).
# IXIC and NYA are US indices, so Close == CloseUSD (roughly).
# For others, we need CloseUSD.

# Simulate monthly investment
# Strategy: Invest 100 units of currency (USD) on the first available trading day of each month.
# 1. Group by Index and Year-Month. Pick the first entry.
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_df = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate portfolio value
results = []
indices = monthly_df['Index'].unique()

for idx in indices:
    sub_df = monthly_df[monthly_df['Index'] == idx].sort_values('Date')
    
    # Check start date
    start_date = sub_df['Date'].iloc[0]
    # We want indices available since early 2000. Let's say, started in 2000.
    if start_date.year > 2000:
        print(f"Index {idx} starts late: {start_date}")
        # Depending on strictness, we might exclude. Query: "investments in all indices since 2000".
        # This implies we only care about those present. Or maybe "If an investor had made... in all indices (that were available)".
        # Let's calculate for all and see. If the return is high despite shorter period, it might be wrong interpretation.
        # But usually "since 2000" implies the full period.
        # Let's keep them but note.
    
    invested = 0
    units = 0
    
    # Use CloseUSD if valid, else Close?
    # Let's check if CloseUSD is valid.
    # We will use 'CloseUSD' column.
    
    # Determine the series to use
    # If CloseUSD is full of NaNs, we can't compare.
    
    sub_df['Price'] = sub_df['CloseUSD']
    # If Price is NaN, forward fill? Or drop?
    # sub_df['Price'] = sub_df['Price'].ffill() 
    
    # Filter out rows with NaN price
    valid_months = sub_df.dropna(subset=['Price'])
    
    for _, row in valid_months.iterrows():
        price = row['Price']
        units += 100.0 / price
        invested += 100.0
        
    # Final value
    # We need the current price (last available in the dataset, not just the last month investment)
    # The last available price in the full daily dataset for this index.
    last_price_row = df[df['Index'] == idx].iloc[-1]
    final_price = last_price_row['CloseUSD']
    
    if pd.isna(final_price):
         # Try using the last valid price
         final_price = df[df['Index'] == idx].dropna(subset=['CloseUSD']).iloc[-1]['CloseUSD']

    final_value = units * final_price
    total_return_pct = ((final_value - invested) / invested) * 100
    
    results.append({
        'Index': idx,
        'Total_Invested': invested,
        'Final_Value': final_value,
        'Return_Pct': total_return_pct,
        'Start_Date': start_date,
        'End_Date': last_price_row['Date']
    })

results_df = pd.DataFrame(results).sort_values(by='Return_Pct', ascending=False)
print("__RESULT__:")
print(results_df[['Index', 'Return_Pct', 'Start_Date']].to_json(orient='records', date_format='iso'))"""

env_args = {'var_function-call-15045155276809644361': ['index_info'], 'var_function-call-15045155276809645240': ['index_trade'], 'var_function-call-8875709257747002473': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-8875709257747005048': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-15054097013438635701': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15054097013438633364': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14791774478946530287': [{'count_star()': '104224'}], 'var_function-call-14002920760052114969': 'file_storage/function-call-14002920760052114969.json'}

exec(code, env_args)
