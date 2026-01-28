code = """import json, pandas as pd
rows = var_call_fYwBVKbmeTZuRgjzzzXRLSDC
# Asia indices (inferred): China (399001.SZ, 000001.SS), India (NSEI), Hong Kong (HSI), Japan (N225), Taiwan (TWII)
asia = {'399001.SZ','000001.SS','NSEI','HSI','N225','TWII'}
df = pd.DataFrame(rows)
df['avg_intraday_volatility'] = df['avg_intraday_volatility'].astype(float)
df_asia = df[df['idx'].isin(asia)].sort_values('avg_intraday_volatility', ascending=False)
res = {
    'top_asia_index': df_asia.iloc[0]['idx'],
    'avg_intraday_volatility': float(df_asia.iloc[0]['avg_intraday_volatility']),
    'n_days': int(df_asia.iloc[0]['n_days']),
    'asia_ranking': df_asia.assign(n_days=df_asia['n_days'].astype(int)).to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ubzNL84IdJ4PKzw46TqIrMia': ['index_info'], 'var_call_hwvd12Y4JmgOfjNXNBxzi2Rk': ['index_trade'], 'var_call_8SMYD2KIDcDI1CnvOoDw8eTw': [], 'var_call_TlAcGpFudpWsV71jzgAdAiJs': [{'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': '16 Jan 2014, 00:00', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}, {'Date': '27 Sep 2013, 00:00', 'n': '10'}, {'Date': '2017-06-14 00:00:00', 'n': '10'}, {'Date': '2012-06-18 00:00:00', 'n': '10'}, {'Date': '2012-05-25 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': 'April 15, 2005 at 12:00 AM', 'n': '10'}, {'Date': '2013-05-21 00:00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': 'July 12, 2010 at 12:00 AM', 'n': '10'}, {'Date': '2020-03-27 00:00:00', 'n': '9'}, {'Date': '16 Mar 2009, 00:00', 'n': '9'}, {'Date': '2003-06-25 00:00:00', 'n': '9'}, {'Date': '2016-04-12 00:00:00', 'n': '9'}, {'Date': '2001-11-14 00:00:00', 'n': '9'}], 'var_call_fYwBVKbmeTZuRgjzzzXRLSDC': [{'idx': '399001.SZ', 'avg_intraday_volatility': '0.01834068808057066', 'n_days': '342'}, {'idx': 'IXIC', 'avg_intraday_volatility': '0.01832021126510304', 'n_days': '355'}, {'idx': 'J203.JO', 'avg_intraday_volatility': '0.01786200640333148', 'n_days': '354'}, {'idx': 'NSEI', 'avg_intraday_volatility': '0.017071504307908447', 'n_days': '349'}, {'idx': 'GDAXI', 'avg_intraday_volatility': '0.0166079612749325', 'n_days': '357'}, {'idx': 'HSI', 'avg_intraday_volatility': '0.014931673425125858', 'n_days': '348'}, {'idx': 'NYA', 'avg_intraday_volatility': '0.014652738733651685', 'n_days': '355'}, {'idx': 'N100', 'avg_intraday_volatility': '0.014407669280062476', 'n_days': '363'}, {'idx': 'SSMI', 'avg_intraday_volatility': '0.014125090041703366', 'n_days': '345'}, {'idx': '000001.SS', 'avg_intraday_volatility': '0.013781104973401202', 'n_days': '340'}, {'idx': 'N225', 'avg_intraday_volatility': '0.013426763944978347', 'n_days': '344'}, {'idx': 'TWII', 'avg_intraday_volatility': '0.013225469311378092', 'n_days': '339'}, {'idx': 'GSPTSE', 'avg_intraday_volatility': '0.012534163736615827', 'n_days': '355'}]}

exec(code, env_args)
