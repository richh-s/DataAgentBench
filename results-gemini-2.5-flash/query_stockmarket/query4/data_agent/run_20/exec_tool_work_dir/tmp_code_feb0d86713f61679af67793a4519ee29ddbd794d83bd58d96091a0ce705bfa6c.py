code = """import pandas as pd
import json

# Read the full result from the JSON file
with open(locals()['var_function-call-9091933901147881422'], 'r') as f:
    stockinfo_data = json.load(f)

# Convert to DataFrame for easier processing
stockinfo_df = pd.DataFrame(stockinfo_data)

# Extract symbols
nyse_non_etf_symbols = stockinfo_df['Symbol'].tolist()

print("__RESULT__:")
print(json.dumps(nyse_non_etf_symbols[:10])) # Print first 10 symbols to verify"""

env_args = {'var_function-call-9091933901147881422': 'file_storage/function-call-9091933901147881422.json'}

exec(code, env_args)
