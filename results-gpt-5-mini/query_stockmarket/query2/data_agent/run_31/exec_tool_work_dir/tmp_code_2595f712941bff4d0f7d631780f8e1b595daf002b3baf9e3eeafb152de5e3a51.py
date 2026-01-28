code = """import json
symbols = json.load(open(var_call_h8yS9HOG4cLI010qfpi0ZWHS))
chunk_size = 100
sqls = []
for i in range(0, len(symbols), chunk_size):
    chunk = symbols[i:i+chunk_size]
    selects = []
    for s in chunk:
        tbl = s.replace '"', '""' if False else s
        sel = f"SELECT '{s}' AS Symbol FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        selects.append(sel)
    sql = '\nUNION ALL\n'.join(selects) + ';'
    sqls.append(sql)
print("__RESULT__:")
print(json.dumps(sqls))"""

env_args = {'var_call_nkeAYvg53uExQmoxgksjf11P': 'file_storage/call_nkeAYvg53uExQmoxgksjf11P.json', 'var_call_IVsTNURPyVMjtErO88g5xAxA': 'file_storage/call_IVsTNURPyVMjtErO88g5xAxA.json', 'var_call_h8yS9HOG4cLI010qfpi0ZWHS': 'file_storage/call_h8yS9HOG4cLI010qfpi0ZWHS.json', 'var_call_nxUZalitLvjFZ3D0ZYNwHkzQ': [], 'var_call_4RyJ1RwPDvZIWpvWUSNkZT4l': {'count': 1435, 'first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
