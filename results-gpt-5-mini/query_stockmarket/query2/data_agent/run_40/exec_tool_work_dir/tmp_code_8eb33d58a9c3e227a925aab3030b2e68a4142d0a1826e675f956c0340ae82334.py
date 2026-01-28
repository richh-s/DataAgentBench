code = """import json
# Load the symbols list generated earlier
with open(var_call_vOvpTPTh22GcZEIT2EmmuKDH, 'r') as f:
    data = json.load(f)
symbols = data.get('symbols_in_trade_db', [])

# Build SQL safely
selects = []
for s in symbols:
    # ensure s contains no double quotes
    s_clean = s.replace('"', '""')
    selects.append("SELECT '{}' AS Symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s_clean, s_clean))

if selects:
    sql = 'SELECT DISTINCT Symbol FROM (\n' + '\nUNION ALL\n'.join(selects) + '\n) as t;'
else:
    sql = "SELECT DISTINCT NULL AS Symbol WHERE false;"

print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_Xbn6LlMeaJI4TuDuO6U1lrKA': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_call_uujsuC1CCLMoXiLygvLHw84R': 'file_storage/call_uujsuC1CCLMoXiLygvLHw84R.json', 'var_call_NMGGKIDoDKAikS77E1C3am3R': 'file_storage/call_NMGGKIDoDKAikS77E1C3am3R.json', 'var_call_vOvpTPTh22GcZEIT2EmmuKDH': 'file_storage/call_vOvpTPTh22GcZEIT2EmmuKDH.json', 'var_call_uliy6p2kjUKT69HBvTrOr4xu': {'sql': None}, 'var_call_zwn7rCYIwfjvoR9DwWkEmGSP': [], 'var_call_ZJwti9h2OYtm4ThrSzozOPcW': [], 'var_call_G0OBuRAc8G2jPeWrehsuBusM': [], 'var_call_qr2J6P2hE42hM1MkvL3sh4tW': [], 'var_call_xt0lsWVvc76rrAYHiG2L9IxB': [], 'var_call_gTrOBs5kYInADNjzcjcUkf8R': []}

exec(code, env_args)
