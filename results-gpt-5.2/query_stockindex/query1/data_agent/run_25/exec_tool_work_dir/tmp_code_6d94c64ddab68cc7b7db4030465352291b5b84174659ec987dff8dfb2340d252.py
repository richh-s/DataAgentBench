code = """import json
asia = {
 'N225':'Japan (Tokyo Stock Exchange) - Nikkei 225',
 'HSI':'Hong Kong - Hang Seng Index',
 '000001.SS':'China (Shanghai) - SSE Composite',
 '399001.SZ':'China (Shenzhen) - SZSE Component',
 'TWII':'Taiwan - TAIEX',
 'NSEI':'India - NIFTY 50'
}
rows = var_call_rMeJCmq2DpABi9wMIdQPm5hd
asia_rows=[]
for r in rows:
    idx=r['Index']
    if idx in asia:
        asia_rows.append({
            'Index': idx,
            'name': asia[idx],
            'avg_intraday_vol': float(r['avg_intraday_vol']),
            'n_days': int(r['n_days'])
        })
asia_rows_sorted = sorted(asia_rows, key=lambda x: x['avg_intraday_vol'], reverse=True)
best = asia_rows_sorted[0] if asia_rows_sorted else None
out={'best':best,'asia_ranking':asia_rows_sorted}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_I9clHpcDVErbjmg95pgGJPia': ['index_info'], 'var_call_TDZHTOBdtawZ9JidJ0BoLEzX': ['index_trade'], 'var_call_zPbk26zngWMNCYBs4f3U5Nb5': [{'Index': 'NYA', 'n_rows': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N225', 'n_rows': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'IXIC', 'n_rows': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GSPTSE', 'n_rows': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'n_rows': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'GDAXI', 'n_rows': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'SSMI', 'n_rows': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n_rows': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'n_rows': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'n_rows': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'N100', 'n_rows': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NSEI', 'n_rows': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'J203.JO', 'n_rows': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_rMeJCmq2DpABi9wMIdQPm5hd': [{'Index': 'IXIC', 'avg_intraday_vol': '0.018396922846873384', 'n_days': '115'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015', 'n_days': '101'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01754961385149785', 'n_days': '120'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774', 'n_days': '107'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373', 'n_days': '107'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014688234063144042', 'n_days': '119'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014161525969530046', 'n_days': '104'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.014082512769161384', 'n_days': '98'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014043436205293046', 'n_days': '97'}, {'Index': 'N225', 'avg_intraday_vol': '0.013420362105889214', 'n_days': '105'}, {'Index': 'N100', 'avg_intraday_vol': '0.013102109556857611', 'n_days': '111'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01267113951326394', 'n_days': '99'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639', 'n_days': '106'}]}

exec(code, env_args)
