code = """import json
rows = var_call_XV0PJnVJKM7728ye7g9XYh06
# Define Asia indices in this dataset (based on common tickers)
asia = {
  '399001.SZ':'China (Shenzhen Component)',
  '000001.SS':'China (Shanghai Composite)',
  'HSI':'Hong Kong (Hang Seng)',
  'N225':'Japan (Nikkei 225)',
  'TWII':'Taiwan (TAIEX)',
  'NSEI':'India (NIFTY 50)'
}
filtered = []
for r in rows:
    idx = r['Index']
    if idx in asia:
        filtered.append({
            'Index': idx,
            'Name': asia[idx],
            'avg_intraday_vol': float(r['avg_intraday_vol']),
            'n_days': int(r['n_days'])
        })
filtered_sorted = sorted(filtered, key=lambda x: x['avg_intraday_vol'], reverse=True)
top = filtered_sorted[0] if filtered_sorted else None
out = {'top_asia': top, 'asia_ranking': filtered_sorted}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IZDska0qZFrnyVVV5Czj3VPA': ['index_info'], 'var_call_uyDsiBsO8DJnfQJMXcFwaGFA': ['index_trade'], 'var_call_HlOUDrYVWOQH2nfAMArelrZG': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_XV0PJnVJKM7728ye7g9XYh06': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066', 'n_days': '342'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.01832021126510304', 'n_days': '355'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148', 'n_days': '354'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.017071504307908447', 'n_days': '349'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325', 'n_days': '357'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014931673425125858', 'n_days': '348'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014652738733651685', 'n_days': '355'}, {'Index': 'N100', 'avg_intraday_vol': '0.014407669280062476', 'n_days': '363'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014125090041703366', 'n_days': '345'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013781104973401202', 'n_days': '340'}, {'Index': 'N225', 'avg_intraday_vol': '0.013426763944978347', 'n_days': '344'}, {'Index': 'TWII', 'avg_intraday_vol': '0.013225469311378092', 'n_days': '339'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827', 'n_days': '355'}]}

exec(code, env_args)
