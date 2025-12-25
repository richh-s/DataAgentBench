code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-11697284118037657579']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Date
# The date formats are mixed. pd.to_datetime with 'mixed' might work.
# If pandas version is old, it might fail.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback for older pandas or strict parsing
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True, errors='coerce')

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01'].copy()
df = df.sort_values(by=['Index', 'Date'])

# Check for indices with very little data
counts = df.groupby('Index').size()
# We keep all for now.

# Function to calculate monthly investment return
def calculate_return(group):
    # Resample to get the first trading day of each month
    # We can create a 'YearMonth' column and drop duplicates keeping the first
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_investments = group.drop_duplicates(subset=['YearMonth'], keep='first')
    
    # Investment details
    monthly_amount = 100.0
    
    # We use CloseUSD if available and non-zero.
    # Check if CloseUSD is valid
    # Some rows might have None or 0.
    # Convert CloseUSD to numeric, coercing errors
    prices = pd.to_numeric(monthly_investments['CloseUSD'], errors='coerce')
    
    # If too many NaNs, maybe fallback to Close?
    # But we want to compare across countries, so USD is best.
    # If USD is missing, we can't compare fairly.
    # Let's drop NaNs
    valid_prices = prices.dropna()
    
    if valid_prices.empty:
        return None
        
    # Total Invested
    total_invested = len(valid_prices) * monthly_amount
    
    # Units bought
    units = (monthly_amount / valid_prices).sum()
    
    # Final Value
    # Get the last available price in the dataset for this index (not just monthly)
    last_price_row = group.iloc[-1]
    last_price = pd.to_numeric(last_price_row['CloseUSD'], errors='coerce')
    
    if pd.isna(last_price):
        # Try to find the last valid price
        last_price = pd.to_numeric(group['CloseUSD'], errors='coerce').dropna().iloc[-1]
        
    final_value = units * last_price
    
    overall_return_pct = (final_value - total_invested) / total_invested * 100
    
    return {
        'Index': group['Index'].iloc[0],
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Return_Pct': overall_return_pct,
        'Start_Date': valid_prices.index[0], # This is just the index in the filtered df, not useful
        'Real_Start_Date': monthly_investments['Date'].iloc[0].strftime('%Y-%m-%d')
    }

results = []
for idx, group in df.groupby('Index'):
    res = calculate_return(group)
    if res:
        results.append(res)

results_df = pd.DataFrame(results)
top_5 = results_df.sort_values(by='Return_Pct', ascending=False).head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-1790763280778497569': ['index_info'], 'var_function-call-1790763280778495504': ['index_trade'], 'var_function-call-7252033416612146088': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-7252033416612146097': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-6979576781361856157': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-6979576781361854250': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-11697284118037657579': 'file_storage/function-call-11697284118037657579.json'}

exec(code, env_args)
