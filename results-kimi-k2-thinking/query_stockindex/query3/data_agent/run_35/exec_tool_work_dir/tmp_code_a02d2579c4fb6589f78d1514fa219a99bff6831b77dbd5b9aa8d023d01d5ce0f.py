code = """import json

# Load price data from file
file_path = locals()['var_functions.query_db:32']
with open(file_path, 'r') as f:
    price_data = json.load(f)

# Group data by index and sort by date
indices_data = {}
for record in price_data:
    idx = record['Index']
    if idx not in indices_data:
        indices_data[idx] = []
    indices_data[idx].append({
        'Date': record['Date'],
        'CloseUSD': float(record['CloseUSD'])
    })

# Calculate monthly DCA returns for each index
dca_results = []

for idx, data in indices_data.items():
    # Sort by date
    records = sorted(data, key=lambda x: x['Date'])
    
    # Group by month-year
    monthly_data = {}
    for rec in records:
        date_str = rec['Date']
        month_key = date_str[:7]  # YYYY-MM
        if month_key not in monthly_data:
            monthly_data[month_key] = []
        monthly_data[month_key].append(rec)
    
    # Get last price for each month
    monthly_prices = []
    for month_key in sorted(monthly_data.keys()):
        if month_key >= '2000-01':  # Start from 2000
            month_records = monthly_data[month_key]
            if month_records:
                last_price = month_records[-1]['CloseUSD']
                monthly_prices.append(last_price)
    
    # Need at least 12 months
    if len(monthly_prices) < 12:
        continue
    
    # DCA calculation: $100 invested each month
    total_invested = len(monthly_prices) * 100
    total_shares = sum([100.0 / price for price in monthly_prices])
    
    # Final value
    final_value = total_shares * monthly_prices[-1]
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    # Annualized return
    years = len(monthly_prices) / 12.0
    annualized = ((final_value / total_invested) ** (1.0 / years) - 1) * 100 if years > 0 else 0
    
    dca_results.append({
        'index': idx,
        'total_return_pct': return_pct,
        'annualized_return_pct': annualized,
        'total_invested': total_invested,
        'final_value': final_value,
        'num_months': len(monthly_prices)
    })

# Sort by total return
dca_results.sort(key=lambda x: x['total_return_pct'], reverse=True)

# Print top 10
print('DCA returns since 2000:')
for i, res in enumerate(dca_results[:10]):
    print(str(i+1) + '. ' + res['index'] + ': ' + str(round(res['total_return_pct'], 1)) + '% total')

print('\n---BEGIN PRINT FORMAT---')
print('__RESULT__:')
print(json.dumps(dca_results[:10]))
print('---END PRINT FORMAT---')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:28': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'record_count': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'record_count': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'record_count': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'record_count': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'record_count': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'record_count': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'record_count': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '5869'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
