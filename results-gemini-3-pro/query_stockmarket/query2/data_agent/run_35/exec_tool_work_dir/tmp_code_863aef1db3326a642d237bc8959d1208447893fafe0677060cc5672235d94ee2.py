code = """import json
import os

key = 'var_function-call-17759206541062733528'
# Load valid symbols
with open(locals()[key], 'r') as f:
    valid_symbols = json.load(f)

# Batch settings
start_index = 0
batch_size = 110
end_index = min(start_index + batch_size, len(valid_symbols))
batch_symbols = valid_symbols[start_index:end_index]

# Generate Query
parts = []
for sym in batch_symbols:
    # Use quotes for table name
    part = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE \"Adj Close\" > 200 AND Date GLOB '2015*' LIMIT 1"
    parts.append(part)

query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps({
    "query": query,
    "next_index": end_index,
    "total": len(valid_symbols)
}))"""

env_args = {'var_function-call-2090132530202969507': 'file_storage/function-call-2090132530202969507.json', 'var_function-call-2090132530202970712': 'file_storage/function-call-2090132530202970712.json', 'var_function-call-17759206541062733528': 'file_storage/function-call-17759206541062733528.json', 'var_function-call-11518138145490088997': 1435, 'var_function-call-8082552596352152953': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}]}

exec(code, env_args)
