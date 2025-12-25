code = """import json

path = locals()['var_function-call-3732280635417606766']
with open(path, 'r') as f:
    symbols = json.load(f)

symbols.sort()
symbols = symbols[:10]

queries = []
# Create one single query for these 10
parts = []
s_date = "2015-01-01"
e_date = "2015-12-31"

for s in symbols:
    q = 'SELECT \'{0}\' as Symbol, MAX("Adj Close") as MaxPrice FROM "{0}" WHERE Date >= \'{1}\' AND Date <= \'{2}\''.format(s, s_date, e_date)
    parts.append(q)

full_query = " UNION ALL ".join(parts)
# Wrap in outer query to filter
final_query = "SELECT * FROM (" + full_query + ") WHERE MaxPrice > 200"

print("__RESULT__:")
print(json.dumps([final_query]))"""

env_args = {'var_function-call-5139739992729438025': 'file_storage/function-call-5139739992729438025.json', 'var_function-call-8590673828826687227': 'file_storage/function-call-8590673828826687227.json', 'var_function-call-5113928090904780528': 'file_storage/function-call-5113928090904780528.json', 'var_function-call-5191216881659803828': 'Done', 'var_function-call-3732280635417606766': 'file_storage/function-call-3732280635417606766.json', 'var_function-call-17840319870052003305': ['SELECT * FROM "HEWU" LIMIT 1']}

exec(code, env_args)
