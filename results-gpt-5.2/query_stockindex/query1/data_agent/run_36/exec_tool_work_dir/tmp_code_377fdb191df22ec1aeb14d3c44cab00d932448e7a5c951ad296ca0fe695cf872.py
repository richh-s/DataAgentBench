code = """import json
asia = {
  'HSI': 'Hong Kong',
  '000001.SS': 'China (Shanghai)',
  '399001.SZ': 'China (Shenzhen)',
  'N225': 'Japan',
  'NSEI': 'India',
  'TWII': 'Taiwan',
  'KOSPI': 'South Korea'
}
rows = var_call_oDveS6wDsn6OrU8oohVXJxfh
asia_rows = [r for r in rows if r['idx'] in asia]
# find max
best = max(asia_rows, key=lambda r: float(r['avg_intraday_vol']))
out = {
  'idx': best['idx'],
  'avg_intraday_vol': float(best['avg_intraday_vol']),
  'country_or_market': asia[best['idx']]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8hDlaIU1R6MmbUPyvvn2ks2s': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_tLBuRGnCpzTonph5yunwXfTA': [], 'var_call_IrfHTlZzalbPprOFenkTx696': [{'Date': '31 Dec 1986, 00:00', 'd1': 'NaT', 'd2': '1986-12-31 00:00:00', 'd3': 'NaT'}, {'Date': 'January 02, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '1987-01-05 00:00:00', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '06 Jan 1987, 00:00', 'd1': 'NaT', 'd2': '1987-01-06 00:00:00', 'd3': 'NaT'}, {'Date': '07 Jan 1987, 00:00', 'd1': 'NaT', 'd2': '1987-01-07 00:00:00', 'd3': 'NaT'}, {'Date': '1987-01-08 00:00:00', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '1987-01-09 00:00:00', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '1987-01-12 00:00:00', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '1987-01-13 00:00:00', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '1987-01-14 00:00:00', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': 'January 15, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': 'January 16, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': 'January 19, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '20 Jan 1987, 00:00', 'd1': 'NaT', 'd2': '1987-01-20 00:00:00', 'd3': 'NaT'}, {'Date': 'January 21, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '22 Jan 1987, 00:00', 'd1': 'NaT', 'd2': '1987-01-22 00:00:00', 'd3': 'NaT'}, {'Date': 'January 23, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': 'January 26, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}, {'Date': '27 Jan 1987, 00:00', 'd1': 'NaT', 'd2': '1987-01-27 00:00:00', 'd3': 'NaT'}, {'Date': 'January 28, 1987 at 12:00 AM', 'd1': 'NaT', 'd2': 'NaT', 'd3': 'NaT'}], 'var_call_Apb1GocQLWfkD9vEbA5zjoJp': [{'Date': '31 Dec 1986, 00:00', 'dt': '1986-12-31 00:00:00'}, {'Date': 'January 02, 1987 at 12:00 AM', 'dt': '1987-01-02 00:00:00'}, {'Date': '1987-01-05 00:00:00', 'dt': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00', 'dt': '1987-01-06 00:00:00'}, {'Date': '07 Jan 1987, 00:00', 'dt': '1987-01-07 00:00:00'}], 'var_call_oDveS6wDsn6OrU8oohVXJxfh': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.018320211265103033'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125852'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}]}

exec(code, env_args)
