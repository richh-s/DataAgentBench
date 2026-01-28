code = """import json
# var_call_HhMqjPV7dcYfUfUjzvrv00Ho is list of dicts with strings for numbers
rows = var_call_HhMqjPV7dcYfUfUjzvrv00Ho
asia = {
  'N225': 'Nikkei 225 (Japan)',
  'HSI': 'Hang Seng Index (Hong Kong)',
  '000001.SS': 'Shanghai Composite (China)',
  '399001.SZ': 'Shenzhen Component (China)',
  'NSEI': 'NIFTY 50 (India)',
  'TWII': 'Taiwan Weighted (Taiwan)'
}
# find highest avg among asia in rows
best = None
for r in rows:
    idx = r['Index']
    if idx in asia:
        avg = float(r['avg_intraday_vol'])
        if (best is None) or (avg > best['avg']):
            best = {'Index': idx, 'Name': asia[idx], 'avg': avg, 'n_days': int(r['n_days'])}
result = json.dumps(best)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_PGkzZfSOvw7TP0G2RPPaWCQP': ['index_info'], 'var_call_ct9mcMJldDoLXQdbZhfHmoz8': ['index_trade'], 'var_call_2Xcja96KJ6Djk2wEtVAvRvrZ': [], 'var_call_vONhR4fhOY1ggGspSyKw9sTN': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_HhMqjPV7dcYfUfUjzvrv00Ho': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066', 'n_days': '342'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.01832021126510304', 'n_days': '355'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148', 'n_days': '354'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.017071504307908447', 'n_days': '349'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325', 'n_days': '357'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014931673425125858', 'n_days': '348'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014652738733651685', 'n_days': '355'}, {'Index': 'N100', 'avg_intraday_vol': '0.014407669280062476', 'n_days': '363'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014125090041703366', 'n_days': '345'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013781104973401202', 'n_days': '340'}, {'Index': 'N225', 'avg_intraday_vol': '0.013426763944978347', 'n_days': '344'}, {'Index': 'TWII', 'avg_intraday_vol': '0.013225469311378092', 'n_days': '339'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827', 'n_days': '355'}]}

exec(code, env_args)
