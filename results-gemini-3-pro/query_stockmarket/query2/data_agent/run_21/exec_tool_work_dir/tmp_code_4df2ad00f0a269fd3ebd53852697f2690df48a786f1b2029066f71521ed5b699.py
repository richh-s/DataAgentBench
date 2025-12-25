code = """import json
path = locals()['var_function-call-18022116377589170118']
with open(path) as f:
    queries = json.load(f)

# Re-generate to be safe with smaller batch
# We need to reload symbols to be precise? 
# No, let's just take the first query from the list (which was batch 100) and split it?
# The list has queries for 100-size batches.
# queries[0] covers first 100.
# Let's just print queries[0] and see if it fits.
# It should be around 120 * 100 = 12000 chars. Might be truncated.
# Let's split it.

q1 = queries[0]
# Split by UNION ALL
parts = q1.split(" UNION ALL ")
# Take first 50
small_q = " UNION ALL ".join(parts[:50])
print("__RESULT__:")
print(json.dumps(small_q))"""

env_args = {'var_function-call-13690384345775752249': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9917169383885839858': 'file_storage/function-call-9917169383885839858.json', 'var_function-call-12815242675246571232': 'file_storage/function-call-12815242675246571232.json', 'var_function-call-18203547688103422521': {'count': 1435, 'sample': ['AXJL', 'PHYS', 'BUYN', 'SCAP', 'FXR', 'AUSF', 'EGPT', 'FEZ', 'KMED', 'JPGE', 'IDHQ', 'RUSL', 'IAK', 'EWJ', 'KBA', 'GDXJ', 'IQSU', 'EFAX', 'URTH', 'JPNL']}, 'var_function-call-323069020816069390': [{'Date': '2006-06-16'}, {'Date': '2006-06-19'}, {'Date': '2006-06-20'}, {'Date': '2006-06-21'}, {'Date': '2006-06-22'}], 'var_function-call-5516898449549523767': 'file_storage/function-call-5516898449549523767.json', 'var_function-call-18022116377589170118': 'file_storage/function-call-18022116377589170118.json', 'var_function-call-7001729309268249408': 'file_storage/function-call-7001729309268249408.json'}

exec(code, env_args)
