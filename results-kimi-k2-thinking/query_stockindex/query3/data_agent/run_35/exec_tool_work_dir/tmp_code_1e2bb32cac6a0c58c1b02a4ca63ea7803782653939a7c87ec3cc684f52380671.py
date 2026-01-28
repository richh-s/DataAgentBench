code = """import json

# Load the data from the file
file_path = 'var_functions.query_db:10'
with open(file_path, 'r') as f:
    price_data = json.load(f)

# Group data by index
indices_data = {}
for record in price_data:
    idx = record['Index']
    if idx not in indices_data:
        indices_data[idx] = []
    indices_data[idx].append({
        'Date': record['Date'],
        'CloseUSD': float(record['CloseUSD'])
    })

# Check which indices have data from 2000 onwards
indices_from_2000 = []
for idx, data in indices_data.items():
    min_date = min([r['Date'] for r in data])
    if min_date <= '2000-12-31':
        indices_from_2000.append(idx)

# Calculate returns for monthly DCA investment
monthly_dca_results = []

for idx in indices_from_2000:
    data = indices_data[idx]
    # Sort by date
    records = sorted(data, key=lambda x: x['Date'])
    
    # Group by month-year for monthly DCA
    monthly_data = {}
    for rec in records:
        date_str = rec['Date']
        month_key = date_str[:7]
        if month_key not in monthly_data:
            monthly_data[month_key] = []
        monthly_data[month_key].append(rec)
    
    # For each month, use the last available price for that month
    monthly_investments = []
    for month_key in sorted(monthly_data.keys()):
        month_records = monthly_data[month_key]
        last_record = month_records[-1]
        monthly_investments.append({
            'date': month_key,
            'price': last_record['CloseUSD']
        })
    
    if len(monthly_investments) < 12:
        continue
    
    # Calculate DCA return: invest $100 each month
    total_invested = 0
    total_shares = 0
    
    for investment in monthly_investments:
        total_invested += 100
        shares = 100.0 / investment['price']
        total_shares += shares
    
    # Current value (using last price)
    last_price = monthly_investments[-1]['price']
    current_value = total_shares * last_price
    total_return = current_value - total_invested
    return_percent = (total_return / total_invested) * 100
    
    # Calculate annualized return
    years = len(monthly_investments) / 12.0
    if years > 0:
        annualized_return = ((current_value / total_invested) ** (1.0 / years) - 1) * 100
    else:
        annualized_return = 0
    
    monthly_dca_results.append({
        'index': idx,
        'total_return_pct': return_percent,
        'annualized_return_pct': annualized_return,
        'total_invested': total_invested,
        'current_value': current_value,
        'num_months': len(monthly_investments),
        'years': years
    })

# Sort by total return percentage
monthly_dca_results.sort(key=lambda x: x['total_return_pct'], reverse=True)

# Print top results
print('\nTop indices by DCA returns:')
for i, result in enumerate(monthly_dca_results[:10]):
    print(str(i+1) + '. ' + result['index'] + ': ' + str(round(result['total_return_pct'], 2)) + '% total')

# Return results as JSON
result_json = json.dumps(monthly_dca_results)
print('---BEGIN PRINT FORMAT---')
print('__RESULT__:')
print(result_json)
print('---END PRINT FORMAT---')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
