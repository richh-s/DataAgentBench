code = """import json

# Load stockinfo
path_info = locals()['var_function-call-2286584878412773018']
with open(path_info, 'r') as f:
    stock_info = json.load(f)

# Load trade tables
path_tables = locals()['var_function-call-3031587922303399521']
with open(path_tables, 'r') as f:
    trade_tables = json.load(f)

available_tables = set(trade_tables)

valid_symbols = [entry['Symbol'] for entry in stock_info if entry['Symbol'] in available_tables]

chunk_size = 60
chunks = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

queries = []
dq = chr(34) # double quote
sq = chr(39) # single quote

for chunk in chunks:
    subqueries = []
    for sym in chunk:
        # Construct query without using complex escaping in the string literal
        # SELECT 'SYM' ... FROM "SYM" ...
        # Date LIKE '2017-%'
        q = "SELECT {sq}{sym}{sq} as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM {dq}{sym}{dq} WHERE Date LIKE {sq}2017-%{sq}".format(sq=sq, dq=dq, sym=sym)
        subqueries.append(q)
    
    full_query = " UNION ALL ".join(subqueries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-2286584878412773018': 'file_storage/function-call-2286584878412773018.json', 'var_function-call-3031587922303399521': 'file_storage/function-call-3031587922303399521.json', 'var_function-call-6367072852195291206': 234, 'var_function-call-8288512070747572073': 'file_storage/function-call-8288512070747572073.json'}

exec(code, env_args)
