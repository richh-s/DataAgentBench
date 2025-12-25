code = """import json

# Load previous results
with open(locals()['var_function-call-16619216267788933502'], 'r') as f:
    candidates = json.load(f)
with open(locals()['var_function-call-7766385081012407064'], 'r') as f:
    tables = json.load(f)

table_set = set(tables)
valid_symbols = [c['Symbol'] for c in candidates if c['Symbol'] in table_set]

# Construct query
subqueries = []
for sym in valid_symbols:
    # Use double quotes for table identifiers if needed, but symbols seem to be uppercase letters. 
    # To be safe, I'll wrap in quotes.
    # Date is str, assuming 'YYYY-MM-DD'.
    q = f"""
    SELECT 
        '{sym}' as Symbol, 
        SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, 
        SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays 
    FROM "{sym}" 
    WHERE Date LIKE '2017-%'
    """
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-16619216267788933502': 'file_storage/function-call-16619216267788933502.json', 'var_function-call-7766385081012407064': 'file_storage/function-call-7766385081012407064.json', 'var_function-call-9364681288924485365': 234}

exec(code, env_args)
