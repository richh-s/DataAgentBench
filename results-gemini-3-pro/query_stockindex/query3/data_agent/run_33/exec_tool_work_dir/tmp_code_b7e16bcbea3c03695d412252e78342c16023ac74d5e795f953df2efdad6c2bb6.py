code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-12731797609713319278'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Try converting with specific format, coerce errors just in case
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce') 
# Note: format='mixed' is available in newer pandas. If environment is old, this might fail.
# The environment says Python 3.12, so pandas should be new.
# If 'mixed' fails, I will try without it but with errors='coerce'.

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])

# Sort
df = df.sort_values(['Index', 'Date'])

results = []

for idx, group in df.groupby('Index'):
    # Resample to get first trading day of each month
    group = group.copy()
    group['Month'] = group['Date'].dt.to_period('M')
    
    # Take the first entry for each month
    monthly_investments = group.drop_duplicates(subset='Month', keep='first')
    
    # Calculate units bought ($1 per month)
    monthly_investments = monthly_investments[monthly_investments['CloseUSD'] > 0]
    
    units = (1 / monthly_investments['CloseUSD']).sum()
    total_invested = len(monthly_investments)
    
    # Get final price (last available date in the dataset)
    if not group.empty:
        final_price = group.iloc[-1]['CloseUSD']
        final_date = group.iloc[-1]['Date']
        
        final_value = units * final_price
        
        overall_return = (final_value - total_invested) / total_invested if total_invested > 0 else 0
        
        results.append({
            'Index': idx,
            'Return': overall_return,
            'FinalValue': final_value,
            'TotalInvested': total_invested,
            # Convert timestamp to string for JSON serialization
            'Start': str(monthly_investments.iloc[0]['Date']) if not monthly_investments.empty else None,
            'End': str(final_date)
        })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-16286307264463492830': ['index_info'], 'var_function-call-16286307264463494683': ['index_trade'], 'var_function-call-12146826697668835484': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-1648360365740439576': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1648360365740441073': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5799821590587801299': [{'Index': 'J203.JO', 'usd_count': '1854', 'close_count': '1854', 'total': '1854'}, {'Index': 'N225', 'usd_count': '7979', 'close_count': '7979', 'total': '7979'}, {'Index': 'GSPTSE', 'usd_count': '6506', 'close_count': '6506', 'total': '6506'}, {'Index': 'NSEI', 'usd_count': '2577', 'close_count': '2577', 'total': '2577'}, {'Index': 'GDAXI', 'usd_count': '5590', 'close_count': '5590', 'total': '5590'}, {'Index': 'IXIC', 'usd_count': '7351', 'close_count': '7351', 'total': '7351'}, {'Index': 'NYA', 'usd_count': '7960', 'close_count': '7960', 'total': '7960'}, {'Index': 'HSI', 'usd_count': '5604', 'close_count': '5604', 'total': '5604'}, {'Index': 'N100', 'usd_count': '4245', 'close_count': '4245', 'total': '4245'}, {'Index': '399001.SZ', 'usd_count': '4355', 'close_count': '4355', 'total': '4355'}, {'Index': '000001.SS', 'usd_count': '4354', 'close_count': '4354', 'total': '4354'}, {'Index': 'SSMI', 'usd_count': '5188', 'close_count': '5188', 'total': '5188'}, {'Index': 'TWII', 'usd_count': '4385', 'close_count': '4385', 'total': '4385'}], 'var_function-call-12731797609713319278': 'file_storage/function-call-12731797609713319278.json'}

exec(code, env_args)
