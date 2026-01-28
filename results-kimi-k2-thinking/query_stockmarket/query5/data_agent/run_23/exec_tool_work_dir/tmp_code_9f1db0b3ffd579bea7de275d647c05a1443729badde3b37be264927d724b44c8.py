code = """import json
import pandas as pd

# Read the stockinfo results from the file
with open('var_functions.query_db:7', 'r') as f:
    stockinfo_result = json.load(f)

# Convert to DataFrame for easier handling
df_stocks = pd.DataFrame(stockinfo_result)
print(f"Found {len(df_stocks)} NASDAQ Capital Market stocks")
print("Sample:", df_stocks.head())

# Get ticker symbols
tickers = df_stocks['Symbol'].tolist()
print(f"Total tickers: {len(tickers)}")

# Print result in required format
result = json.dumps({
    'count': len(tickers),
    'tickers': tickers[:10]  # First 10 for preview
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:2': ['stockinfo'], 'var_functions.query_db:5': [{'cid': '0', 'name': 'Nasdaq Traded', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Symbol', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Listing Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Market Category', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'ETF', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Round Lot Size', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'Test Issue', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Financial Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'NextShares', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'Company Description', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
