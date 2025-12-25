code = """import json

# Load symbols
path1 = locals()['var_function-call-9762896799442664376']
with open(path1, 'r') as f:
    d1 = json.load(f)
    syms = set([x['Symbol'] for x in d1])

# Load tables
path2 = locals()['var_function-call-15346480681916956948']
with open(path2, 'r') as f:
    tbls = set(json.load(f))

valid = list(syms.intersection(tbls))

queries = []
for s in valid:
    # SQL: SELECT 'SYM' as Symbol, COUNT(*) as Days FROM "SYM" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)
    # Escape quotes if necessary? Usually tickers don't have quotes.
    # We use double quotes for table identifier "s"
    # We use single quotes for string literal 's'
    q = "SELECT '" + s + "' as Symbol, COUNT(*) as Days FROM \"" + s + "\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

final_q = " UNION ALL ".join(queries) + " ORDER BY Days DESC LIMIT 5"

print('__RESULT__:')
print(json.dumps(final_q))"""

env_args = {'var_function-call-9762896799442664376': 'file_storage/function-call-9762896799442664376.json', 'var_function-call-7368161656916448319': 86, 'var_function-call-15346480681916956948': 'file_storage/function-call-15346480681916956948.json'}

exec(code, env_args)
