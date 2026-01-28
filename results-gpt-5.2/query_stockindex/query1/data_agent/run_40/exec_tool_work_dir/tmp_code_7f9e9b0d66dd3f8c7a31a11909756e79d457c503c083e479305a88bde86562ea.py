code = """import json
asia = {
  'N225','HSI','000001.SS','399001.SZ','NSEI','TWII'
}
rows = var_call_GqLDW4ob4dmEPG5zjPL11KwI
asia_rows = [r for r in rows if r['idx'] in asia]
asia_rows_sorted = sorted(asia_rows, key=lambda r: float(r['avg_intraday_vol']), reverse=True)
res = {
  'highest_asia_index': asia_rows_sorted[0]['idx'] if asia_rows_sorted else None,
  'avg_intraday_vol': float(asia_rows_sorted[0]['avg_intraday_vol']) if asia_rows_sorted else None,
  'n_days': int(asia_rows_sorted[0]['n_days']) if asia_rows_sorted else None,
  'asia_ranking_top': [
    {'idx': r['idx'], 'avg_intraday_vol': float(r['avg_intraday_vol']), 'n_days': int(r['n_days'])}
    for r in asia_rows_sorted
  ]
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ZVmZEu770mZujtJ9IswbEW13': [], 'var_call_9TJLrMKPOWhuJCTbb7DzLL22': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_hYRuQtzzWYmb6QAcDRwhN3cT': [{'Date': '31 Dec 1986, 00:00', 'parsed': '1986-12-31 00:00:00'}, {'Date': 'January 02, 1987 at 12:00 AM', 'parsed': '1987-01-02 00:00:00'}, {'Date': '1987-01-05 00:00:00', 'parsed': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00', 'parsed': '1987-01-06 00:00:00'}, {'Date': '07 Jan 1987, 00:00', 'parsed': '1987-01-07 00:00:00'}, {'Date': '1987-01-08 00:00:00', 'parsed': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00', 'parsed': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00', 'parsed': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00', 'parsed': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00', 'parsed': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM', 'parsed': '1987-01-15 00:00:00'}, {'Date': 'January 16, 1987 at 12:00 AM', 'parsed': '1987-01-16 00:00:00'}, {'Date': 'January 19, 1987 at 12:00 AM', 'parsed': '1987-01-19 00:00:00'}, {'Date': '20 Jan 1987, 00:00', 'parsed': '1987-01-20 00:00:00'}, {'Date': 'January 21, 1987 at 12:00 AM', 'parsed': '1987-01-21 00:00:00'}, {'Date': '22 Jan 1987, 00:00', 'parsed': '1987-01-22 00:00:00'}, {'Date': 'January 23, 1987 at 12:00 AM', 'parsed': '1987-01-23 00:00:00'}, {'Date': 'January 26, 1987 at 12:00 AM', 'parsed': '1987-01-26 00:00:00'}, {'Date': '27 Jan 1987, 00:00', 'parsed': '1987-01-27 00:00:00'}, {'Date': 'January 28, 1987 at 12:00 AM', 'parsed': '1987-01-28 00:00:00'}], 'var_call_GqLDW4ob4dmEPG5zjPL11KwI': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066', 'n_days': '342'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.018320211265103033', 'n_days': '355'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148', 'n_days': '354'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447', 'n_days': '349'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325', 'n_days': '357'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125852', 'n_days': '348'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685', 'n_days': '355'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476', 'n_days': '363'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366', 'n_days': '345'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202', 'n_days': '340'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347', 'n_days': '344'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092', 'n_days': '339'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827', 'n_days': '355'}]}

exec(code, env_args)
