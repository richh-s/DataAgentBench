code = """import json
asia = {'399001.SZ','000001.SS','NSEI','HSI','N225','TWII'}
rows = var_call_YVF98187b462nSSENSGjznFL
rows2 = []
for r in rows:
    if r['Index'] in asia:
        rows2.append({'Index': r['Index'], 'avg_intraday_vol': float(r['avg_intraday_vol'])})
rows2_sorted = sorted(rows2, key=lambda x: x['avg_intraday_vol'], reverse=True)
out = {'asia_ranked': rows2_sorted, 'top_asia': rows2_sorted[0] if rows2_sorted else None}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YVF98187b462nSSENSGjznFL': [{'Index': 'IXIC', 'avg_intraday_vol': '0.018396922846873384'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01754961385149785'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014688234063144042'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014161525969530046'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.014082512769161384'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014043436205293046'}, {'Index': 'N225', 'avg_intraday_vol': '0.013420362105889214'}, {'Index': 'N100', 'avg_intraday_vol': '0.013102109556857611'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01267113951326394'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639'}]}

exec(code, env_args)
