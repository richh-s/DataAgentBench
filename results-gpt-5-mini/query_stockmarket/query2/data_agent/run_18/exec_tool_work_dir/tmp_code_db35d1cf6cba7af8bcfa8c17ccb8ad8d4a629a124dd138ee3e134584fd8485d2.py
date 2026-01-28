code = """import json
p = var_call_6FNmhOdhP9KwXPGUfbhrXhEJ
with open(p, 'r') as f:
    symbols = json.load(f)
parts = []
for s in symbols:
    part = 'SELECT "' + s + '" AS Symbol, MAX("Adj Close") AS max_adj FROM "' + s + '" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\''
    parts.append(part)
union_sql = '\nUNION ALL\n'.join(parts)
sql = 'SELECT Symbol, max_adj FROM (\n' + union_sql + '\n) AS t WHERE max_adj > 200 ORDER BY Symbol;'
out = {'sql': sql, 'num_symbols': len(symbols)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UpHwLqrnxP6jMvmuilhtHEYp': 'file_storage/call_UpHwLqrnxP6jMvmuilhtHEYp.json', 'var_call_HViMBQGu5fIjjUvgP8uMwvKu': 'file_storage/call_HViMBQGu5fIjjUvgP8uMwvKu.json', 'var_call_SH4wBNP6R0eZxAoJaEawqLeK': {'count': 1435, 'sample_first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_call_6FNmhOdhP9KwXPGUfbhrXhEJ': 'file_storage/call_6FNmhOdhP9KwXPGUfbhrXhEJ.json'}

exec(code, env_args)
