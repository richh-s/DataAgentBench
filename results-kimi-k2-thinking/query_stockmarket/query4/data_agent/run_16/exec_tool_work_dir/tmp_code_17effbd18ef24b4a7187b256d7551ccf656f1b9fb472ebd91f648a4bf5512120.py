code = """import json

# Load the full symbol list with company names
symbols_file = locals()['var_functions.query_db:0']

with open(symbols_file, 'r') as f:
    symbols_data = json.load(f)

# Create mapping
symbol_to_company = {rec['Symbol']: rec['Company Description'] for rec in symbols_data}
symbols = list(symbol_to_company.keys())

results = []
processed = 0

for symbol in symbols:
    try:
        query = f"""SELECT 
            COUNT(CASE WHEN Close > Open THEN 1 END) as up_days,
            COUNT(CASE WHEN Close < Open THEN 1 END) as down_days
            FROM {symbol} 
            WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"""
        
        # Execute query through the tool
        import subprocess, json
        # Since we can't call query_db from here directly, we'll simulate and collect SQL
        results.append({
            'symbol': symbol,
            'query': query
        })
        
    except Exception as e:
        results.append({
            'symbol': symbol,
            'error': str(e)
        })
    
    processed += 1
    if processed >= 10:
        break

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'processed': processed,
    'sample_queries': [r['query'] for r in results[:3]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_non_etf': 234, 'present_in_trade_db': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:8': [{'Symbol': 'AEFC', 'Company': 'None'}, {'Symbol': 'AIN', 'Company': 'None'}, {'Symbol': 'AIV', 'Company': 'None'}, {'Symbol': 'AIZP', 'Company': 'None'}, {'Symbol': 'AJRD', 'Company': 'None'}], 'var_functions.query_db:10': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'High': '15.701873779296877', 'Low': '14.988152503967283', 'Close': '15.107105255126951', 'Adj Close': '8.918145179748535', 'Volume': '2292200'}, {'Date': '1987-10-01', 'Open': '15.107105255126951', 'High': '15.345012664794922', 'Low': '14.988152503967283', 'Close': '15.345012664794922', 'Adj Close': '9.05859375', 'Volume': '468200'}, {'Date': '1987-10-02', 'Open': '15.345012664794922', 'High': '15.701873779296877', 'Low': '15.107105255126951', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '371600'}, {'Date': '1987-10-05', 'Open': '15.701873779296877', 'High': '15.701873779296877', 'Low': '15.226058959960938', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '121300'}, {'Date': '1987-10-06', 'Open': '15.58292007446289', 'High': '15.58292007446289', 'Low': '15.226058959960938', 'Close': '15.463966369628906', 'Adj Close': '9.128814697265623', 'Volume': '159300'}], 'var_functions.execute_python:14': {'count': 234, 'example': ['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.']}, 'var_functions.query_db:16': [{'total_2017': '251', 'up_days': '143', 'down_days': '101'}]}

exec(code, env_args)
