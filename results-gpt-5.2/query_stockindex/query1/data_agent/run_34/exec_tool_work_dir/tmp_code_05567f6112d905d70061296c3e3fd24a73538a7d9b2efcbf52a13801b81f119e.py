code = """import json
asia = {
  '399001.SZ': 'Shenzhen Component (China)',
  'NSEI': 'NIFTY 50 (India)',
  'HSI': 'Hang Seng (Hong Kong)',
  '000001.SS': 'SSE Composite (China)',
  'TWII': 'Taiwan Weighted (Taiwan)',
  'N225': 'Nikkei 225 (Japan)'
}
rows = var_call_fVYyOqH5CQblbo1w4DfIViWZ
asia_rows = []
for r in rows:
    idx = r['Index']
    if idx in asia:
        asia_rows.append({'Index': idx, 'Name': asia[idx], 'avg_intraday_vol': float(r['avg_intraday_vol'])})
asia_rows_sorted = sorted(asia_rows, key=lambda x: x['avg_intraday_vol'], reverse=True)
result = {
    'top_asia_index': asia_rows_sorted[0] if asia_rows_sorted else None,
    'asia_ranking_in_toplist': asia_rows_sorted
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VGlyc54Tif1Nh1gIEO30b2kq': ['index_info'], 'var_call_oDpHQM228lClmCr9AS28oGAp': ['index_trade'], 'var_call_fVYyOqH5CQblbo1w4DfIViWZ': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.018367121551882994'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.018352634174080888'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.017949408823972023'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.017339709656220562'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.01670059829168851'}, {'Index': 'HSI', 'avg_intraday_vol': '0.015096167383143023'}, {'Index': 'N100', 'avg_intraday_vol': '0.01445236872292471'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014235196916380324'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.013976293824740756'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013797724957835671'}, {'Index': 'TWII', 'avg_intraday_vol': '0.013549346375859089'}, {'Index': 'N225', 'avg_intraday_vol': '0.013052566337351822'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.011917473847069163'}]}

exec(code, env_args)
