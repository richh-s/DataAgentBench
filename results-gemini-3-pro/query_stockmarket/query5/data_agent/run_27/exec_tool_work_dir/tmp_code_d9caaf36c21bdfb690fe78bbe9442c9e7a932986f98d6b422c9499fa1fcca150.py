code = """import json

# Load the result from stockinfo query
with open(locals()['var_function_call_11393603106395449050'], 'r') as f:
    stockinfo_list = json.load(f)

# Load the result from list_db
with open(locals()['var_function_call_11393603106395449519'], 'r') as f:
    table_list = json.load(f)

# Extract symbols
nasdaq_capital_symbols = {item['Symbol'] for item in stockinfo_list}
available_tables = set(table_list)

# Intersection
target_symbols = list(nasdaq_capital_symbols.intersection(available_tables))
target_symbols.sort()

print("__RESULT__:")
print(json.dumps({
    "count": len(target_symbols),
    "sample_symbols": target_symbols[:10],
    "all_symbols": target_symbols
}))"""

env_args = {'var_function-call-11393603106395449050': 'file_storage/function-call-11393603106395449050.json', 'var_function-call-11393603106395449519': 'file_storage/function-call-11393603106395449519.json', 'var_function-call-17289981033040106678': [{'Date': '2018-04-18', 'Open': '5.75', 'High': '7.5', 'Low': '5.010000228881836', 'Close': '6.300000190734863', 'Adj Close': '6.300000190734863', 'Volume': '291800'}, {'Date': '2018-04-19', 'Open': '6.800000190734863', 'High': '8.859999656677246', 'Low': '6.684000015258789', 'Close': '8.479999542236328', 'Adj Close': '8.479999542236328', 'Volume': '299600'}, {'Date': '2018-04-20', 'Open': '13.260000228881836', 'High': '14.989999771118164', 'Low': '7.590000152587891', 'Close': '7.788000106811523', 'Adj Close': '7.788000106811523', 'Volume': '830400'}, {'Date': '2018-04-23', 'Open': '7.5', 'High': '8.579999923706055', 'Low': '7.010000228881836', 'Close': '8.399999618530273', 'Adj Close': '8.399999618530273', 'Volume': '102600'}, {'Date': '2018-04-24', 'Open': '8.119999885559082', 'High': '8.640000343322754', 'Low': '7.28000020980835', 'Close': '8.449999809265137', 'Adj Close': '8.449999809265137', 'Volume': '87600'}]}

exec(code, env_args)
