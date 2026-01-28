code = """import json, pandas as pd

data = var_call_WdoDIe6z33aou3cRgr452hlq
# cast numeric strings
for r in data:
    r['avg_intraday_vol'] = float(r['avg_intraday_vol'])
    r['n_days'] = int(r['n_days'])

# Asia indices based on geographic knowledge
asia = {'N225','NSEI','HSI','399001.SZ','000001.SS','TWII'}

df = pd.DataFrame([r for r in data if r['idx'] in asia])
res = df.sort_values('avg_intraday_vol', ascending=False).head(1).to_dict(orient='records')[0]

out = {
    'index': res['idx'],
    'avg_intraday_volatility': res['avg_intraday_vol'],
    'n_days': res['n_days']
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CXhbp6mp8Dj2fUnHz8A9utQ6': ['index_info'], 'var_call_D5lYpYzIHhF8LiIGSZGtoNFZ': ['index_trade'], 'var_call_WdoDIe6z33aou3cRgr452hlq': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774', 'n_days': '107'}, {'idx': 'N225', 'avg_intraday_vol': '0.013420362105889214', 'n_days': '105'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639', 'n_days': '106'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.01754961385149785', 'n_days': '120'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373', 'n_days': '107'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014688234063144042', 'n_days': '119'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014161525969530046', 'n_days': '104'}, {'idx': 'N100', 'avg_intraday_vol': '0.013102109556857611', 'n_days': '111'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015', 'n_days': '101'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.014082512769161384', 'n_days': '98'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014043436205293046', 'n_days': '97'}, {'idx': 'TWII', 'avg_intraday_vol': '0.01267113951326394', 'n_days': '99'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.018396922846873384', 'n_days': '115'}]}

exec(code, env_args)
