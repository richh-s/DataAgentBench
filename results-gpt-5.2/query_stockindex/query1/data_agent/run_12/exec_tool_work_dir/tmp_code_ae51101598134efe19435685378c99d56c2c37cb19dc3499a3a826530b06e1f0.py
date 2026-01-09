code = """import json, pandas as pd

df = pd.DataFrame(var_call_fuJbu96WmwrcUtX0dgEwNoL7)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Define Asia indices in this dataset
asia = {'N225','NSEI','HSI','000001.SS','399001.SZ','TWII'}
df_asia = df[df['Index'].isin(asia)].copy()

top = df_asia.sort_values('avg_intraday_vol', ascending=False).head(1)
res = {
    'index': top.iloc[0]['Index'],
    'avg_intraday_volatility': float(top.iloc[0]['avg_intraday_vol'])
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_u74Ga1M8FtZQMa3Ar62P7UJO': ['index_info'], 'var_call_Uu9P9XLKwkfmv0DYl5kBLAPQ': ['index_trade'], 'var_call_fw0uIKM5MbaoDM3tEon4Z4CN': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_fuJbu96WmwrcUtX0dgEwNoL7': [{'Index': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'Index': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.01832021126510304'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014931673425125858'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'Index': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'Index': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}]}

exec(code, env_args)
