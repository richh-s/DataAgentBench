code = """import json
with open(locals()['var_function-call-10667966384812128504'], 'r') as f:
    nasdaq_capital_market_stocks = json.load(f)

symbols_and_descriptions = {item['Symbol']: item['Company Description'] for item in nasdaq_capital_market_stocks}
print('__RESULT__:')
print(json.dumps(symbols_and_descriptions))"""

env_args = {'var_function-call-10667966384812128504': 'file_storage/function-call-10667966384812128504.json'}

exec(code, env_args)
