code = """import json
import duckdb

# Get the list of NASDAQ Capital Market stocks
result_file = 'file_storage/functions.query_db:0.json'
with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Connect to DuckDB database
conn = duckdb.connect(database='file_storage/stocktrade_database.duckdb', read_only=True)

# Query to get all table names (stock symbols) in the database
tables_result = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'").fetchall()
available_symbols = [row[0] for row in tables_result]

print('Total NASDAQ Capital Market stocks:', len(nasdaq_capital_stocks))
print('Total available stock tables:', len(available_symbols))

# Filter NASDAQ Capital Market stocks to only those with data in stocktrade_database
nasdaq_symbols = [stock['Symbol'] for stock in nasdaq_capital_stocks]
available_nasdaq_symbols = [sym for sym in nasdaq_symbols if sym in available_symbols]

print('NASDAQ Capital stocks with trade data:', len(available_nasdaq_symbols))

# Create company description map
company_map = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_capital_stocks}

# For each stock, calculate the number of days in 2019 with intraday range > 20% of low
volatility_counts = []

for i, symbol in enumerate(available_nasdaq_symbols[:10]):  # Process first 10 for testing
    try:
        # Query 2019 data for this stock
        query = f"SELECT Date, High, Low FROM \"{symbol}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'"
        result = conn.execute(query).fetchall()
        
        if result:  # Only process if we have data
            count_high_volatility = 0
            total_days = len(result)
            
            for row in result:
                high = float(row[1])
                low = float(row[2])
                
                # Check if intraday range exceeds 20% of low price
                # (High - Low) / Low > 0.20 or High > Low * 1.20
                if low > 0 and high > low * 1.20:
                    count_high_volatility += 1
            
            volatility_counts.append({
                'symbol': symbol,
                'company': company_map[symbol],
                'high_vol_days': count_high_volatility,
                'total_days': total_days
            })
            
            print(f"{symbol}: {count_high_volatility}/{total_days} high volatility days")
    except Exception as e:
        print(f"Error processing {symbol}: {e}")

conn.close()

result_data = {
    'processed_stocks': len(volatility_counts),
    'sample_results': volatility_counts[:5]
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:8': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:10': {'total_stocks': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)
