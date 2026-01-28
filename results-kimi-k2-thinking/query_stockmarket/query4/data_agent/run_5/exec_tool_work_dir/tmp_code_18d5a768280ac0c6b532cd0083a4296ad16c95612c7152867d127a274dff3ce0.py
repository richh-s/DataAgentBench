code = """import json

# Load common symbols
execute_result = locals()['var_functions.execute_python:12']
common_symbols = execute_result['common_symbols']
symbols_map = execute_result['symbols_map']

print(f"Processing {len(common_symbols)} NYSE non-ETF symbols...")
print(f"Sample symbols: {common_symbols[:10]}")

# We'll query individual stocks to analyze 2017 data
# For efficiency, we'll do this in batches and track top performers

# Store results for stocks with more up days than down days
stock_performance = []
test_count = 0

for symbol in common_symbols[:50]:  # Test with first 50 to see performance
    try:
        # Query this symbol's 2017 data
        query = f"SELECT Date, Open, Close FROM '{symbol}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        result = query_db("stocktrade_database", query)
        
        # Count will be returned as json or filepath
        if isinstance(result, str) and '.json' in result:
            with open(result, 'r') as f:
                data = json.load(f)
        else:
            data = result
            
        if data and len(data) > 0:
            up_days = sum(1 for row in data if row['Close'] > row['Open'])
            down_days = sum(1 for row in data if row['Close'] < row['Open'])
            total_days = len(data)
            
            if up_days > down_days:
                stock_performance.append({
                    'symbol': symbol,
                    'up_days': up_days,
                    'down_days': down_days,
                    'difference': up_days - down_days,
                    'total_days': total_days,
                    'company_name': symbols_map.get(symbol, 'N/A')
                })
                
        test_count += 1
        if test_count % 10 == 0:
            print(f"Processed {test_count} symbols...")
            
    except Exception as e:
        print(f"Error processing {symbol}: {e}")
        continue

print(f"Found {len(stock_performance)} stocks with more up days than down days in first 50")
if stock_performance:
    # Sort by difference
    sorted_stocks = sorted(stock_performance, key=lambda x: x['difference'], reverse=True)
    print(f"Top 5 so far: {sorted_stocks[:5]}")

result = {
    'stocks_found': len(stock_performance),
    'top_stocks': sorted_stocks[:5] if stock_performance else []
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'total_symbols': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_count': 234, 'trade_count': 2753, 'common_count': 234, 'common_symbols': ['MGR', 'TCP', 'BKH', 'DGX', 'UTL', 'SRC', 'AIV', 'KW', 'H', 'SLF', 'PFE', 'TGP', 'ZNH', 'CTS', 'RES', 'CMI', 'IT', 'EBS', 'WSM', 'IBM']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'symbol_count': 234, 'sample_symbols': ['PRSP', 'EGO', 'RBC', 'CIA', 'BV', 'VRT', 'ROG', 'EMP', 'AMP', 'SBR']}}

exec(code, env_args)
