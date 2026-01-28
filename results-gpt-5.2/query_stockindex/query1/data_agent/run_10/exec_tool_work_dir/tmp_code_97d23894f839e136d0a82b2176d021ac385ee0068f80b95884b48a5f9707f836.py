code = """import json
import pandas as pd

data = var_call_5jnWcMOjU6O9dx3JQypxsVhT

df = pd.DataFrame(data)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

asia = {
    'HSI': 'Hong Kong (Hang Seng Index)',
    '000001.SS': 'China (Shanghai Composite)',
    '399001.SZ': 'China (Shenzhen Component)',
    'N225': 'Japan (Nikkei 225)',
    'NSEI': 'India (NIFTY 50)',
    'TWII': 'Taiwan (TSEC Weighted Index)',
}

df_asia = df[df['idx'].isin(asia.keys())].copy()
if df_asia.empty:
    out = {"error": "No Asia indices found in computed results."}
else:
    top = df_asia.sort_values('avg_intraday_vol', ascending=False).iloc[0]
    out = {
        "index_symbol": top['idx'],
        "index_name": asia[top['idx']],
        "avg_intraday_volatility_since_2020": float(top['avg_intraday_vol'])
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vuc5brvUV3AostmzwU1v6HoJ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_XKzDCt3iNE9zAeMgKxJAOFJW': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_5jnWcMOjU6O9dx3JQypxsVhT': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}]}

exec(code, env_args)
