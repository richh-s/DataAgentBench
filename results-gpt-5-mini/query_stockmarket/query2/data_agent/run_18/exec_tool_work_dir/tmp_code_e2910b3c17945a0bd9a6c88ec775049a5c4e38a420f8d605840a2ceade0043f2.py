code = """import json
p1 = var_call_UpHwLqrnxP6jMvmuilhtHEYp
p2 = var_call_HViMBQGu5fIjjUvgP8uMwvKu
with open(p1, 'r') as f:
    etfs = json.load(f)
with open(p2, 'r') as f:
    tables = json.load(f)
symbols = [r['Symbol'] for r in etfs]
common = sorted([s for s in symbols if s in tables])
print('__RESULT__:')
print(json.dumps(common))"""

env_args = {'var_call_UpHwLqrnxP6jMvmuilhtHEYp': 'file_storage/call_UpHwLqrnxP6jMvmuilhtHEYp.json', 'var_call_HViMBQGu5fIjjUvgP8uMwvKu': 'file_storage/call_HViMBQGu5fIjjUvgP8uMwvKu.json', 'var_call_SH4wBNP6R0eZxAoJaEawqLeK': {'count': 1435, 'sample_first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
