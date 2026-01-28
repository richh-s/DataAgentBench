code = """import json, pandas as pd
rows = var_call_9zGGMHlO3rEVI7OAxOcG3O4T

df = pd.DataFrame(rows)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

asia = {'N225','HSI','000001.SS','399001.SZ','TWII','NSEI'}
df_asia = df[df['Index'].isin(asia)].copy()

top = df_asia.sort_values('avg_intraday_vol', ascending=False).iloc[0]
res = {
  'Index': top['Index'],
  'avg_intraday_vol': float(top['avg_intraday_vol']),
  'avg_intraday_vol_pct': float(top['avg_intraday_vol']*100.0)
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_5nvdSdLuZLMPN6DWbDyPmXm7': ['index_info'], 'var_call_g1Vqn6SrpR40shNCBVwZVymr': ['index_trade'], 'var_call_iKiHvfhXg0y9wnZ4fe0mTA3Z': [{'Index': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_k30VXbnZCy3oC39IOSzEQJKO': [{'Index': 'NSEI', 'n': '120'}, {'Index': 'HSI', 'n': '119'}, {'Index': 'IXIC', 'n': '115'}, {'Index': 'N100', 'n': '111'}, {'Index': 'J203.JO', 'n': '107'}, {'Index': 'GDAXI', 'n': '107'}, {'Index': 'GSPTSE', 'n': '106'}, {'Index': 'N225', 'n': '105'}, {'Index': 'NYA', 'n': '104'}, {'Index': '399001.SZ', 'n': '101'}, {'Index': 'TWII', 'n': '99'}, {'Index': '000001.SS', 'n': '98'}, {'Index': 'SSMI', 'n': '97'}], 'var_call_9zGGMHlO3rEVI7OAxOcG3O4T': [{'Index': 'IXIC', 'avg_intraday_vol': '0.018396922846873384'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01754961385149785'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014688234063144042'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014161525969530046'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.014082512769161384'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014043436205293046'}, {'Index': 'N225', 'avg_intraday_vol': '0.013420362105889214'}, {'Index': 'N100', 'avg_intraday_vol': '0.013102109556857611'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01267113951326394'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639'}]}

exec(code, env_args)
