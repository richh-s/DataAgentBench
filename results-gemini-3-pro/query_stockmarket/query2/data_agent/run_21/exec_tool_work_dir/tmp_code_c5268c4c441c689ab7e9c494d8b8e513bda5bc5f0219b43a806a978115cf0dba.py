code = """import json

# Access variables
path1 = locals()['var_function-call-9917169383885839858']
path2 = locals()['var_function-call-12815242675246571232']

# Read files
with open(path1, 'r') as f1:
    data1 = json.load(f1)
with open(path2, 'r') as f2:
    data2 = json.load(f2)

# Process
s1 = set()
for x in data1:
    s1.add(x['Symbol'])

s2 = set(data2)

inter = sorted(list(s1.intersection(s2)))

# Generate queries
queries = []
chunk_size = 100
for i in range(0, len(inter), chunk_size):
    chunk = inter[i:i+chunk_size]
    parts = []
    for sym in chunk:
        # Construct SQL
        sql = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(sym)
        parts.append(sql)
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-13690384345775752249': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9917169383885839858': 'file_storage/function-call-9917169383885839858.json', 'var_function-call-12815242675246571232': 'file_storage/function-call-12815242675246571232.json', 'var_function-call-18203547688103422521': {'count': 1435, 'sample': ['AXJL', 'PHYS', 'BUYN', 'SCAP', 'FXR', 'AUSF', 'EGPT', 'FEZ', 'KMED', 'JPGE', 'IDHQ', 'RUSL', 'IAK', 'EWJ', 'KBA', 'GDXJ', 'IQSU', 'EFAX', 'URTH', 'JPNL']}, 'var_function-call-323069020816069390': [{'Date': '2006-06-16'}, {'Date': '2006-06-19'}, {'Date': '2006-06-20'}, {'Date': '2006-06-21'}, {'Date': '2006-06-22'}]}

exec(code, env_args)
