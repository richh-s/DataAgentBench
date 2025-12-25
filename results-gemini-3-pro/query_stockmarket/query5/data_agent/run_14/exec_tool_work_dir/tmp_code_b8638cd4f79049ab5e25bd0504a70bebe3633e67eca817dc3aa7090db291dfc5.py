code = """import json

# Load the result from the ticker extraction step
path_tickers = locals()['var_function-call-12166660516732642610']

with open(path_tickers, 'r') as f:
    data = json.load(f)

tickers = data['tickers']
mid = len(tickers) // 2
batch1 = tickers[:mid]

queries = []
dq = chr(34)

for t in batch1:
    q = "SELECT '{0}' as Symbol, COUNT(*) as NumDays FROM {1}{0}{1} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)".format(t, dq)
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-13634932259963143763': 'file_storage/function-call-13634932259963143763.json', 'var_function-call-13634932259963145996': 'file_storage/function-call-13634932259963145996.json', 'var_function-call-12166660516732642610': 'file_storage/function-call-12166660516732642610.json', 'var_function-call-14611251066521441883': 'file_storage/function-call-14611251066521441883.json'}

exec(code, env_args)
