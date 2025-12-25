code = """import json

# Manually selected high price candidates and major ETFs
targets = [
    'SPY', 'IVV', 'VOO', 'DIA', 'GLD', 'IWM', 'QQQ', 
    'SSO', 'UPRO', 'SDS', 'TQQQ', 'SPXL', 'SPXS', 
    'UDOW', 'SDOW', 'URTY', 'SRTY', 'UVXY', 'SVXY',
    'VTI', 'VTV', 'VUG', 'IWB', 'IWF', 'IWD', 'IJH', 'IJR'
]

# Filter by valid symbols (must be in the NYSE Arca list)
path = locals()['var_function-call-11973061372010644575']
with open(path, 'r') as f:
    valid_symbols = set(json.load(f))

candidates = [t for t in targets if t in valid_symbols]

# Also add a random sample to check for "hidden" ones
import random
random.seed(42)
all_list = sorted(list(valid_symbols))
sample = random.sample(all_list, 50)
candidates.extend([s for s in sample if s not in candidates])

queries = []
q_quote = chr(34)
s_quote = chr(39)
for s in candidates:
    q = "SELECT " + s_quote + s + s_quote + " as Symbol FROM " + q_quote + s + q_quote + " WHERE " + q_quote + "Adj Close" + q_quote + " > 200 AND Date >= " + s_quote + "2015-01-01" + s_quote + " AND Date <= " + s_quote + "2015-12-31" + s_quote + " LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435, 'var_function-call-2000411894810468263': 'test', 'var_function-call-12527035195204984051': 1435, 'var_function-call-1928971542841167320': 'file_storage/function-call-1928971542841167320.json', 'var_function-call-13502002390751631329': False, 'var_function-call-17442318757823361204': 'file_storage/function-call-17442318757823361204.json', 'var_function-call-448095643459452714': 'file_storage/function-call-448095643459452714.json'}

exec(code, env_args)
