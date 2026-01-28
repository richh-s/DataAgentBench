code = """import json, pandas as pd
rows = var_call_5l0FXrOf7T9pWqKypsgdTxhT

df = pd.DataFrame(rows)
if df.empty:
    out = {"error": "No data after 2020"}
else:
    df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)
    df['n_days'] = df['n_days'].astype(int)
    asia = {
        'N225': 'Japan',
        'HSI': 'Hong Kong',
        '000001.SS': 'China (Shanghai)',
        '399001.SZ': 'China (Shenzhen)',
        'TWII': 'Taiwan',
        'NSEI': 'India'
    }
    df_asia = df[df['idx'].isin(asia.keys())].copy()
    df_asia['market'] = df_asia['idx'].map(asia)
    df_asia = df_asia.sort_values('avg_intraday_vol', ascending=False)
    top = df_asia.iloc[0].to_dict() if not df_asia.empty else None
    out = {
        "top_asia_index": top,
        "asia_ranking": df_asia[['idx','market','avg_intraday_vol','n_days']].to_dict(orient='records'),
        "note": "intraday volatility computed as avg((High-Low)/Open) for trading days with parsed Date >= 2020-01-01"
    }
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aF8luPpIymu1mqWCodqFTCJB': ['index_info'], 'var_call_98pLbmwheLLoQZ3xxBfuAQSf': ['index_trade'], 'var_call_ZT4pSCiwF3M9Sf9zvkxUVL2M': [], 'var_call_D6J2biKx6UW46QW5YqlKLq1p': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_5l0FXrOf7T9pWqKypsgdTxhT': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066', 'n_days': '342'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304', 'n_days': '355'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148', 'n_days': '354'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447', 'n_days': '349'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325', 'n_days': '357'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858', 'n_days': '348'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685', 'n_days': '355'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476', 'n_days': '363'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366', 'n_days': '345'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202', 'n_days': '340'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347', 'n_days': '344'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092', 'n_days': '339'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827', 'n_days': '355'}]}

exec(code, env_args)
