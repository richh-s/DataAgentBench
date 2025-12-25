code = """import json
import os

# Load all valid symbols
path = locals()['var_function-call-11973061372010644575']
with open(path, 'r') as f:
    all_symbols = json.load(f)

# Batch size
batch_size = 80 

# Check if we have processed any (simulated state)
# We will just print the query for the FIRST batch now.
# We can't easily maintain state across tool calls without re-reading variables or files.
# I will output the SQL for symbols 0 to 80.

batch_symbols = all_symbols[:80]

queries = []
q_quote = chr(34)
s_quote = chr(39)
for s in batch_symbols:
    q = "SELECT " + s_quote + s + s_quote + " as Symbol FROM " + q_quote + s + q_quote + " WHERE " + q_quote + "Adj Close" + q_quote + " > 200 AND Date >= " + s_quote + "2015-01-01" + s_quote + " AND Date <= " + s_quote + "2015-12-31" + s_quote + " LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435, 'var_function-call-2000411894810468263': 'test', 'var_function-call-12527035195204984051': 1435, 'var_function-call-1928971542841167320': 'file_storage/function-call-1928971542841167320.json', 'var_function-call-13502002390751631329': False}

exec(code, env_args)
