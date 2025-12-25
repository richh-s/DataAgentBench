code = """import json
path = locals()['var_function-call-5516898449549523767']
with open(path) as f: syms = json.load(f)
queries = []
# Increase batch size to cover all in fewer strings if possible, but keep it safe. 100 is ok.
for i in range(0, len(syms), 100):
    batch = syms[i:i+100]
    parts = []
    for s in batch:
        parts.append("SELECT '" + s + "' as Symbol FROM \"" + s + "\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1")
    queries.append(" UNION ALL ".join(parts))
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-13690384345775752249': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9917169383885839858': 'file_storage/function-call-9917169383885839858.json', 'var_function-call-12815242675246571232': 'file_storage/function-call-12815242675246571232.json', 'var_function-call-18203547688103422521': {'count': 1435, 'sample': ['AXJL', 'PHYS', 'BUYN', 'SCAP', 'FXR', 'AUSF', 'EGPT', 'FEZ', 'KMED', 'JPGE', 'IDHQ', 'RUSL', 'IAK', 'EWJ', 'KBA', 'GDXJ', 'IQSU', 'EFAX', 'URTH', 'JPNL']}, 'var_function-call-323069020816069390': [{'Date': '2006-06-16'}, {'Date': '2006-06-19'}, {'Date': '2006-06-20'}, {'Date': '2006-06-21'}, {'Date': '2006-06-22'}], 'var_function-call-5516898449549523767': 'file_storage/function-call-5516898449549523767.json'}

exec(code, env_args)
