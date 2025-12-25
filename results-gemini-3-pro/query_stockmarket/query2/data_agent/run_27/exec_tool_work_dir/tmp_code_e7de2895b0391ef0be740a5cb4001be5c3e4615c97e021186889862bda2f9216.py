code = """import json

with open('var_function-call-6291273035979822157', 'r') as f:
    tickers_data = json.load(f)

tickers = [item['Symbol'] for item in tickers_data]
print(f"Total tickers: {len(tickers)}")
print(f"First 10 tickers: {tickers[:10]}")

print("__RESULT__:")
print(json.dumps(tickers))"""

env_args = {'var_function-call-6291273035979822157': 'file_storage/function-call-6291273035979822157.json'}

exec(code, env_args)
