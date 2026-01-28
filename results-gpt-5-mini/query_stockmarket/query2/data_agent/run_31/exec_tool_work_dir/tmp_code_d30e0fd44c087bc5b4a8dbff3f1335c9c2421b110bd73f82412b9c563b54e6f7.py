code = """import json
symbols = json.load(open(var_call_h8yS9HOG4cLI010qfpi0ZWHS))
selects = []
for s in symbols:
    # Build a safe SELECT for each table
    sel = 'SELECT "{}" AS Symbol FROM "{}" WHERE "Date" >= \'2015-01-01\' AND "Date" <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'.format(s, s)
    selects.append(sel)
sql = '\nUNION ALL\n'.join(selects) + ';' if selects else "SELECT '' AS Symbol WHERE 1=0;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_nkeAYvg53uExQmoxgksjf11P': 'file_storage/call_nkeAYvg53uExQmoxgksjf11P.json', 'var_call_IVsTNURPyVMjtErO88g5xAxA': 'file_storage/call_IVsTNURPyVMjtErO88g5xAxA.json', 'var_call_h8yS9HOG4cLI010qfpi0ZWHS': 'file_storage/call_h8yS9HOG4cLI010qfpi0ZWHS.json', 'var_call_nxUZalitLvjFZ3D0ZYNwHkzQ': [], 'var_call_4RyJ1RwPDvZIWpvWUSNkZT4l': {'count': 1435, 'first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_call_pmrVB1mzB2rSgNfUPOa9EA7L': []}

exec(code, env_args)
