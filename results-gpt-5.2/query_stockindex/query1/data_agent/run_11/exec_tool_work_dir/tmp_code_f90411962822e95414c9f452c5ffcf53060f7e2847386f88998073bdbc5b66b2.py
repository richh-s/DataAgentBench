code = """import pandas as pd, json, re

def parse_date(s):
    if s is None:
        return pd.NaT
    s=str(s)
    s=re.sub(r'\s+at\s+\d{1,2}:\d{2}\s+(AM|PM)\s*',' ',s)
    s=re.sub(r'\s+at\s+\d{1,2}:\d{2}:\d{2}\s*',' ',s)
    s=s.replace('00:00','')
    s=s.strip().replace('  ',' ')
    return pd.to_datetime(s, errors='coerce')

# quick test on sample
sample = pd.DataFrame(var_call_LTeScfm9ZIUGxqdRJ8qXDFgS)
sample['dt']=sample['Date'].map(parse_date)
out = sample[['Index','Date','dt']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_Bd3juBN2NQZFyeVmWB1F45vQ': ['index_info'], 'var_call_kzTE364IS4JZuzVvapCZs3bA': ['index_trade'], 'var_call_b4OULgk8Dr1djgNy1jK8XyBa': [{'Index': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_call_LTeScfm9ZIUGxqdRJ8qXDFgS': [{'Index': 'N225', 'Date': 'September 30, 2020 at 12:00 AM', 'Open': '23478.84961', 'High': '23522.38086', 'Low': '23170.89063', 'Close': '23185.11914'}, {'Index': 'N225', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '8713.910156', 'High': '8756.0', 'Low': '8653.620117', 'Close': '8700.290039'}, {'Index': 'N225', 'Date': 'September 30, 2010 at 12:00 AM', 'Open': '9554.830078', 'High': '9566.839844', 'Low': '9369.349609', 'Close': '9369.349609'}, {'Index': 'N225', 'Date': 'September 30, 2009 at 12:00 AM', 'Open': '10105.16992', 'High': '10138.04004', 'Low': '10063.69043', 'Close': '10133.23047'}, {'Index': 'N225', 'Date': 'September 30, 1993 at 12:00 AM', 'Open': '20097.60938', 'High': '20158.32031', 'Low': '20032.19922', 'Close': '20105.71094'}]}

exec(code, env_args)
