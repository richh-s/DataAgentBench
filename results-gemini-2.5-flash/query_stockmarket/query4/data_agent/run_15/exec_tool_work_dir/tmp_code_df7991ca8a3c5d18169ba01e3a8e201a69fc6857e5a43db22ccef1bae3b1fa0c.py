code = """import pandas as pd
import json

# Load the full JSON result from the file
with open(locals()['var_function-call-15034420442826133404'], 'r') as f:
    nyse_non_etf_stocks = json.load(f)

# Extract symbols and company descriptions
stock_info_df = pd.DataFrame(nyse_non_etf_stocks)
symbols = stock_info_df['Symbol'].tolist()
company_descriptions = stock_info_df.set_index('Symbol')['Company Description'].to_dict()

# Print the first 5 symbols to check
__RESULT__:
print(json.dumps({'symbols_count': len(symbols), 'first_5_symbols': symbols[:5], 'first_5_company_descriptions': {k: company_descriptions[k] for k in symbols[:5]}}))"""

env_args = {'var_function-call-15034420442826133404': 'file_storage/function-call-15034420442826133404.json'}

exec(code, env_args)
