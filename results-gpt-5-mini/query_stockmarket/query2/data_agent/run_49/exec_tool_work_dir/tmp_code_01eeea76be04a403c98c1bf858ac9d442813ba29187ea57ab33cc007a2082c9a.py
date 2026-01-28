code = """import json
with open(var_call_n7eyBtU9JJA5p4IL6Klc9EyV, 'r') as f:
    data = json.load(f)
symbols = data['symbols_to_check']

chunk_size = 250
chunks = [symbols[i:i+chunk_size] for i in range(0, len(symbols), chunk_size)]
sqls = []
for chunk in chunks:
    parts = []
    for s in chunk:
        parts.append("SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
    sql = ' UNION ALL '.join(parts) + ' ORDER BY Symbol;'
    sqls.append(sql)

print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_RWOznzhcAB1bqpucDN0isQ8n': 'file_storage/call_RWOznzhcAB1bqpucDN0isQ8n.json', 'var_call_J6gHfxFPYsOEKD6kPD74HU0X': 'file_storage/call_J6gHfxFPYsOEKD6kPD74HU0X.json', 'var_call_n7eyBtU9JJA5p4IL6Klc9EyV': 'file_storage/call_n7eyBtU9JJA5p4IL6Klc9EyV.json', 'var_call_us9VTGKcI5dFIGrFrPcnV5Iq': {'sql_list_count': 8, 'sql_list_sample_first_len': 27652}, 'var_call_E6pzyfJ84827TUyoSs5QQLrT': {'num_sqls': 6}, 'var_call_RV4EDKgTIMzIL5OIDPk4n9h1': {'num_sqls': 6, 'files_created': 6}, 'var_call_M9sT5va7Md5qmBDFiLGoiNCs': [], 'var_call_ni5AubE3rYUu4oy6SWMmPVPW': [], 'var_call_1JH0d6KixJpP2r4AMEB1iw87': {'note': 'Ready to run batch queries; proceeding outside of this python step.'}, 'var_call_bi6iCiiAJH1mRHjGNj5KBS0S': [], 'var_call_zM2j1b81Lde8fW3ukaWjttNh': []}

exec(code, env_args)
