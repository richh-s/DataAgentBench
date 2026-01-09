code = """import json
import pandas as pd

df = pd.DataFrame(var_call_GgraVtRhfzNoLf5xcgfms1p0)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Define Asia-region indices present in results (inferred from symbols)
asia = {
    '399001.SZ': 'China (Shenzhen Component)',
    'NSEI': 'India (NIFTY 50)',
    'HSI': 'Hong Kong (Hang Seng)',
    '000001.SS': 'China (Shanghai Composite)',
    'N225': 'Japan (Nikkei 225)',
    'TWII': 'Taiwan (TSEC Weighted)',
}

df_asia = df[df['idx'].isin(asia.keys())].copy()
# pick max
winner = df_asia.sort_values('avg_intraday_vol', ascending=False).iloc[0]
answer_obj = {
    'winner_index_symbol': winner['idx'],
    'winner_index_name_inferred': asia[winner['idx']],
    'avg_intraday_volatility_since_2020': float(winner['avg_intraday_vol']),
    'asia_ranking': df_asia.sort_values('avg_intraday_vol', ascending=False)
        .assign(index_name=lambda d: d['idx'].map(asia))
        [['idx','index_name','avg_intraday_vol']]
        .to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(answer_obj))"""

env_args = {'var_call_RLJubG1vH9rhxwrpTPMvTbWv': ['index_info'], 'var_call_RYcTqXqGgiYXrPE5NOHk495Z': ['index_trade'], 'var_call_htJ5a4VtuUOYBCRSyCHWHEtY': [{'raw_date': '31 Dec 1986, 00:00'}, {'raw_date': 'January 02, 1987 at 12:00 AM'}, {'raw_date': '1987-01-05 00:00:00'}, {'raw_date': '06 Jan 1987, 00:00'}, {'raw_date': '07 Jan 1987, 00:00'}, {'raw_date': '1987-01-08 00:00:00'}, {'raw_date': '1987-01-09 00:00:00'}, {'raw_date': '1987-01-12 00:00:00'}, {'raw_date': '1987-01-13 00:00:00'}, {'raw_date': '1987-01-14 00:00:00'}, {'raw_date': 'January 15, 1987 at 12:00 AM'}, {'raw_date': 'January 16, 1987 at 12:00 AM'}, {'raw_date': 'January 19, 1987 at 12:00 AM'}, {'raw_date': '20 Jan 1987, 00:00'}, {'raw_date': 'January 21, 1987 at 12:00 AM'}, {'raw_date': '22 Jan 1987, 00:00'}, {'raw_date': 'January 23, 1987 at 12:00 AM'}, {'raw_date': 'January 26, 1987 at 12:00 AM'}, {'raw_date': '27 Jan 1987, 00:00'}, {'raw_date': 'January 28, 1987 at 12:00 AM'}], 'var_call_GgraVtRhfzNoLf5xcgfms1p0': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}]}

exec(code, env_args)
