code = """import json
import pandas as pd

with open(locals()['var_function-call-12878043852616683498'], 'r') as f:
    nyse_non_etf_stocks = json.load(f)

nyse_non_etf_stocks_df = pd.DataFrame(nyse_non_etf_stocks)

# Filter out the first row which seems to be headers again. It has Symbol: "Symbol" and Company Description: "Company Description"
nyse_non_etf_stocks_df = nyse_non_etf_stocks_df[nyse_non_etf_stocks_df['Symbol'] != 'Symbol']

# Convert to a dictionary for easier lookup
stock_info_dict = nyse_non_etf_stocks_df.set_index('Symbol').to_dict(orient='index')

print("__RESULT__:")
print(json.dumps(stock_info_dict))"""

env_args = {'var_function-call-15043543411406400120': [], 'var_function-call-10707248306571797415': ['stockinfo'], 'var_function-call-3590572963787279885': [{'cid': '0', 'name': 'Nasdaq Traded', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Symbol', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Listing Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Market Category', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'ETF', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Round Lot Size', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'Test Issue', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Financial Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'NextShares', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'Company Description', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15219700771644574740': [{"'Listing Exchange'": 'Listing Exchange'}], 'var_function-call-12878043852616683498': 'file_storage/function-call-12878043852616683498.json'}

exec(code, env_args)
