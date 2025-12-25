code = """import json

# Load valid ETFs
with open(locals()['var_function-call-3767063324109208335'], 'r') as f:
    valid_etfs = json.load(f)

# Batch 1: 0 to 400 (let's try 400 to reduce steps)
batch = valid_etfs[0:400]

queries = []
for symbol in batch:
    # Use quotes for symbol table name just in case, though they seem clean.
    # Use "Adj Close" in double quotes.
    # Check 2015.
    q = f"SELECT '{symbol}' as Symbol FROM \"{symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-4802881243625228792': 'file_storage/function-call-4802881243625228792.json', 'var_function-call-16540620887605966298': 'file_storage/function-call-16540620887605966298.json', 'var_function-call-3767063324109208335': 'file_storage/function-call-3767063324109208335.json', 'var_function-call-15698500669381180607': 1435, 'var_function-call-5404336224704908885': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}], 'var_function-call-10637479535566839517': [{'Date': '2018-08-17', 'Open': '11.800000190734863', 'High': '11.81999969482422', 'Low': '11.770000457763672', 'Close': '11.81999969482422', 'Adj Close': '11.81999969482422', 'Volume': '52400'}]}

exec(code, env_args)
