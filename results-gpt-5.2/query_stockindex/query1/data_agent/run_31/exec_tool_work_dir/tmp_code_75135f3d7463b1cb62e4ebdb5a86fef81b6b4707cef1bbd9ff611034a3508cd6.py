code = """import json
asia = {
 'N225': 'Japan (Nikkei 225)',
 'HSI': 'Hong Kong (Hang Seng)',
 '000001.SS': 'China (Shanghai Composite)',
 '399001.SZ': 'China (Shenzhen Component)',
 'NSEI': 'India (NIFTY 50)',
 'TWII': 'Taiwan (TSEC Weighted)'
}
rows = var_call_RI1K9gtC1LFv7uklwgqbMn4w
# coerce numeric
for r in rows:
    r['avg_intraday_vol'] = float(r['avg_intraday_vol'])
    r['n_days'] = int(r['n_days'])
asia_rows = [r for r in rows if r['idx'] in asia]
asia_rows.sort(key=lambda x: x['avg_intraday_vol'], reverse=True)
best = asia_rows[0]
answer = {
 'index_symbol': best['idx'],
 'index_name_region': asia[best['idx']],
 'avg_intraday_volatility': best['avg_intraday_vol'],
 'n_days_used': best['n_days'],
 'metric': '(High-Low)/Open averaged over trading days since 2020-01-01'
}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_VQv4V6LhkJnlySYoNK061ZYV': ['index_trade'], 'var_call_23w8tNMfHrbKZRKA9mpCLybS': [], 'var_call_6eeFSgiJRmuVmFpGZBIjcYVW': [], 'var_call_6I7fCdFdSpWpyE6fNpDKvZyt': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_RI1K9gtC1LFv7uklwgqbMn4w': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066', 'n_days': '342'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304', 'n_days': '355'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148', 'n_days': '354'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447', 'n_days': '349'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325', 'n_days': '357'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858', 'n_days': '348'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685', 'n_days': '355'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476', 'n_days': '363'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366', 'n_days': '345'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202', 'n_days': '340'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347', 'n_days': '344'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092', 'n_days': '339'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827', 'n_days': '355'}]}

exec(code, env_args)
