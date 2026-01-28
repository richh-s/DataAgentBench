code = """import json
import pandas as pd

df = pd.DataFrame(var_call_ROzF0MwEdNqdC4npVJZOO2WR)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

asia = {'N225','HSI','000001.SS','399001.SZ','NSEI','TWII'}
df_asia = df[df['Index'].isin(asia)].sort_values('avg_intraday_vol', ascending=False)
res = {
  'top_asia_index': None if df_asia.empty else df_asia.iloc[0]['Index'],
  'avg_intraday_vol': None if df_asia.empty else float(df_asia.iloc[0]['avg_intraday_vol']),
  'asia_ranking': df_asia.to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_0W1orLIqKq3WKTJ4YDkbna26': [], 'var_call_ag4A46vkp2VW1noKWLTRwR2C': [], 'var_call_ByJwVEVlgLjl8M26yh0XsTGv': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}], 'var_call_ROzF0MwEdNqdC4npVJZOO2WR': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.01832021126510304'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014931673425125858'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}, {'Index': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'Index': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'Index': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}]}

exec(code, env_args)
