code = """import json

# Load symbols from stockinfo
with open(locals()['var_function-call-15554006225660693874'], 'r') as f:
    stock_info = json.load(f)
    
# Extract symbols (some might be duplicates? listing exchange='N' should be unique per symbol usually)
# Also build a map Symbol -> Name for later use
symbol_map = {item['Symbol']: item['Company Description'] for item in stock_info}
candidate_symbols = set(symbol_map.keys())

# Load tables from stocktrade
with open(locals()['var_function-call-9442049365035450544'], 'r') as f:
    tables = json.load(f)

# Find intersection
valid_symbols = [s for s in candidate_symbols if s in tables]

# Construct SQL query
sqls = []
for sym in valid_symbols:
    # Double quote table name
    table_name = f'"{sym}"' 
    # Query part
    q = f"""
    SELECT '{sym}' as Symbol, 
           SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, 
           SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays 
    FROM {table_name} 
    WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'
    """
    sqls.append(q)

final_query = " UNION ALL ".join(sqls)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-7665505920426729345': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-15554006225660693874': 'file_storage/function-call-15554006225660693874.json', 'var_function-call-3837883820293415021': 234, 'var_function-call-9442049365035450544': 'file_storage/function-call-9442049365035450544.json'}

exec(code, env_args)
