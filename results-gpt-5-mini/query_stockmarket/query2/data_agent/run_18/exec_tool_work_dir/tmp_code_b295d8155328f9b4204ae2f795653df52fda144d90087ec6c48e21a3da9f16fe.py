code = """import json
p = var_call_6FNmhOdhP9KwXPGUfbhrXhEJ
with open(p, 'r') as f:
    symbols = json.load(f)
chunk_size = 200
chunks = [symbols[i:i+chunk_size] for i in range(0, len(symbols), chunk_size)]
queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        part = 'SELECT "{sym}" AS Symbol, MAX("Adj Close") AS max_adj FROM "{sym}" WHERE Date >= \"2015-01-01\" AND Date <= \"2015-12-31\"'.format(sym=s)
        parts.append(part)
    union_sql = '\nUNION ALL\n'.join(parts)
    sql = 'SELECT Symbol, max_adj FROM (\n' + union_sql + '\n) AS t WHERE max_adj > 200 ORDER BY Symbol;'
    queries.append(sql)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_UpHwLqrnxP6jMvmuilhtHEYp': 'file_storage/call_UpHwLqrnxP6jMvmuilhtHEYp.json', 'var_call_HViMBQGu5fIjjUvgP8uMwvKu': 'file_storage/call_HViMBQGu5fIjjUvgP8uMwvKu.json', 'var_call_SH4wBNP6R0eZxAoJaEawqLeK': {'count': 1435, 'sample_first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_call_6FNmhOdhP9KwXPGUfbhrXhEJ': 'file_storage/call_6FNmhOdhP9KwXPGUfbhrXhEJ.json'}

exec(code, env_args)
